try:
    import tensorflow.python.keras as keras
except:
    import tensorflow.keras as keras
import tensorflow as tf
from tensorflow.keras import layers
def creat_network():
    softmax=layers.Softmax()         #Softmax层
    print(softmax(tf.constant([1.0,2.0,3])))
    network = keras.Sequential([ # 封装为一个网络
                layers.Dense(3, activation=None), # 全连接层
                layers.ReLU(),#激活函数层
                layers.Dense(2, activation=None), # 全连接层
                layers.ReLU() #激活函数层
             ])
    x = tf.random.normal([4,3])
    print(network(x)) # 输入从第一层开始，逐层传播至最末层
    '''
    也可以添加的方法建立网络
    '''
    layers_num = 2  # 堆叠 2 次
    network = keras.Sequential([])  # 先创建空的网络
    for i in range(layers_num):
        network.add(layers.Dense(3))
        network.add(layers.ReLU())
    network.build(input_shape=(None, 4))  # 创建网络参数
    print(network.summary())
    # 打印网络的待优化参数名与 shape
    for p in network.trainable_variables:
        print(p.name, p.shape)
def do_minist():
    network=keras.Sequential([
        layers.Dense(256,activation='relu'),
        layers.Dense(128, activation='relu'),
        layers.Dense(64, activation='relu'),
        layers.Dense(32, activation='relu'),
        layers.Dense(8, activation='relu')
    ]
    )
    network.build(input_sharp=(None,28*28))
    # 采用 Adam 优化器，学习率为 0.01;采用交叉熵损失函数，包含 Softmax
    network.compile(optimizer=keras.optimizer.Adam(lr=0.01), loss=keras.losses.CategoricalCrossentropy(from_logits=True),
        metrics=['accuracy'] )# 设置测量指标为准确率
    train_db,val_db=[]
    # 指定训练集为 train_db，验证集为 val_db,训练 5 个 epochs，每 2 个 epoch 验证一次 # 返回训练信息保存在 history 中
    network.fit(train_db,validation_data=val_db, validation_freq=2)
    # 保存模型参数到文件上,这种方式得重新建立网络结构这种只是储存权值
    network.save_weights("weight.ckpt")
    # 保存模型结构与模型参数到文件 ,和本科毕设做的不一样这种方法不需要重新建立网络结构
    network.save('model.h5')
    # 从文件恢复网络结构与网络参数
    network = tf.keras.models.load_model('model.h5')
def about_metrics():
    loss=0
    loss_meter=keras.metrics.Mean()
    # 记录采样的数据
    loss_meter.update_state(float(loss))
    # 打印统计的平均 loss
    print(loss_meter.result())
    # 清零测量器
    loss_meter.reset_states()
class MyDense(layers.Layer):
    # 自定义网络层
    def __init__(self, inp_dim, outp_dim):
        super(MyDense, self).__init__()
        # 创建权值张量并添加到类管理列表中，设置为需要优化
        self.kernel = self.add_variable('w', [inp_dim, outp_dim], trainable=True)

    def call(self, inputs, training=None):
        # 实现自定义类的前向计算逻辑
        # X@W
        out = inputs @ self.kernel
        # 执行激活函数运算
        out = tf.nn.relu(out)
        return out
class MyModel(keras.Model):
    # 自定义网络类，继承自 Model 基类
    def __init__(self):
        super(MyModel, self).__init__()
    # 完成网络内需要的网络层的创建工作
        self.fc1 = MyDense(28*28, 256)
        self.fc2 = MyDense(256, 128)
        self.fc3 = MyDense(128, 64)
        self.fc4 = MyDense(64, 32)
        self.fc5 = MyDense(32, 10)

    def call(self, inputs, training=None):
        # 自定义前向运算逻辑
        x = self.fc1(inputs)
        x = self.fc2(x)
        x = self.fc3(x)
        x = self.fc4(x)
        x = self.fc5(x)
        return x

creat_network()