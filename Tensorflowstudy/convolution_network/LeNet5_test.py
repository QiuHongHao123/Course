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
# 导入误差计算，优化器模块
from tensorflow.keras import losses, optimizers
# 创建损失函数的类，在实际计算时直接调用类实例即可
criteon = losses.CategoricalCrossentropy(from_logits=True)
Mynetwork=Mynetwork()
Mynetwork.build(input_shape=(4, 28, 28, 1))
print(Mynetwork.summary())
x=tf.random.normal([3,28,28,1])
y=[[0,1,0,0,0,0,0,0,0,0],
[0,0,0,1,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0,0,0]
   ]
# 构建梯度记录环境
with tf.GradientTape() as tape:
# 插入通道维度，=>[b,28,28,1]
    x = tf.expand_dims(x,axis=3)
# 前向计算，获得 10 类别的概率分布，[b, 784] => [b, 10]
    out = Mynetwork(x)
# 真实标签 one-hot 编码，[b] => [b, 10]
    y_onehot = tf.one_hot(y, depth=10)
# 计算交叉熵损失函数，标量
    loss = criteon(y_onehot, out)
# 自动计算梯度
grads = tape.gradient(loss, Mynetwork.trainable_variables)
optimizer = tf.keras.optimizers.RMSprop(0.001)  # 创建优化器，指定学习率
# 自动更新参数
optimizer.apply_gradients(zip(grads, Mynetwork.trainable_variables))

