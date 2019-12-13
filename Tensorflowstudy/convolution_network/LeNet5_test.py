import tensorflow as tf
from tensorflow.keras import Sequential,layers

class my_nn_layer(tf.keras.layers.Layer):
    def __init__(self,kernel_size,inputdim,outdim):
        super(my_nn_layer, self).__init__()
        self.w=tf.Variable(tf.random.normal([kernel_size,kernel_size,inputdim,outdim]))

    def call(self, input):
        out = tf.nn.conv2d(input, self.w, padding='SAME', strides=1)
        return out

class Mynetwork(tf.keras.Model):
    def __init__(self):
        super(Mynetwork, self).__init__()
        self.network=Sequential([
        my_nn_layer(3,1,6),
        #layers.Conv2D(6, kernel_size=3, strides=1),  # 第一个卷积层, 6 个 3x3 卷积核
        tf.keras.layers.MaxPooling2D(pool_size=2,strides=2), # 高宽各减半的池化层
        tf.keras.layers.ReLU(),
        my_nn_layer(3, 6,16),
        #layers.Conv2D(16, kernel_size=3, strides=1),  # 第二个卷积层, 16 个 3x3 卷积核
        tf.keras.layers.MaxPooling2D(pool_size=2, strides=2),  # 高宽各减半的池化层
        tf.keras.layers.ReLU(), # 激活函数
        tf.keras.layers.Flatten(),  # 打平层，方便全连接层处理

        tf.keras.layers.Dense(120, activation='relu'),
        # 全连接层，120 个节点
        tf.keras.layers.Dense(84, activation='relu'), # 全连接层，84 节点
        tf.keras.layers.Dense(10) # 全连接层，10 个节点
        ])
        #self.network.build(input_shape=[4, 28, 28, 1])

    def call(self, inputs,training=None):
        x=self.network(inputs)
        return x
Mynetwork=Mynetwork()
Mynetwork.build(input_shape=(4, 28, 28, 1))
print(Mynetwork.summary())

