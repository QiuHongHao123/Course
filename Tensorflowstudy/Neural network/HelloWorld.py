import tensorflow as tf
from tensorflow import keras
def simple_connect_layer():
    '''
    创建全连接层
    '''
    '''
    张量方式
    '''
    x = tf.random.normal([2, 784])
    w1 = tf.Variable(tf.random.truncated_normal([784, 256], stddev=0.1))
    b1 = tf.Variable(tf.zeros([256]))
    o1 = tf.matmul(x, w1) + b1  # 线性变换
    o1 = tf.nn.relu(o1)  # 激活函数

    '''
    层方式
    '''
    # 创建全连接层，指定输出节点数和激活函数
    fc = keras.layers.Dense(512, activation=tf.nn.relu)
    h1 = fc(x)  # 通过 fc 类完成一次全连接层的计算
    '''
    输入的节点数 在fc(x)计算时自动获取，并创建内部权值矩阵 W 和偏置 b。我们可以通过类内部的成员名 kernel 和 bias 来获取权值矩阵 W 和偏置 b： 
    在优化参数时，需要获得网络的所有待优化的参数张量列表，可以通过类的 trainable_variables 来返回待优化参数列表： 
    '''
    print(fc.trainable_variables)
def creat_network():
    '''
    1.层方式
    :return:
    '''
    x = tf.random.normal([2, 784])
    w1=tf.Variable(tf.random.truncated_normal([784,256]))
    b1=tf.Variable(tf.zeros([256]))
    w2=tf.Variable(tf.random.truncated_normal([256,128]))
    b2 = tf.Variable(tf.zeros([128]))
    w3=tf.Variable(tf.random.truncated_normal([128,64]))
    b3 = tf.Variable(tf.zeros([64]))
    w4 = tf.Variable(tf.random.truncated_normal([64, 10]))
    b4 = tf.Variable(tf.zeros([10]))
    with tf.GradientTape() as tape: # 梯度记录器
        h1=x@w1+b1
        h1=tf.nn.relu(h1)
        h2 = h1 @ w2 + b2
        h2 = tf.nn.relu(h2)
        h3 = h2 @ w3 + b3
        h3 = tf.nn.relu(h3)
        h4 = h3 @ w4 + b4
    '''
    层实现
    '''
    fc1 = keras.layers.Dense(256,
                       activation=tf.nn.relu)  # 隐藏层 1
    fc2 = keras.layers.Dense(128, activation=tf.nn.relu) #  隐藏层 2
    fc3 = keras.layers.Dense(64, activation=tf.nn.relu) #  隐藏层 3
    fc4 = keras.layers.Dense(10, activation=None)  # 输出层
    model=keras.layers.Sequential(
        [
            fc1,
            fc2,
            fc3,
            fc4,
            
        ]

    )


simple_connect_layer()