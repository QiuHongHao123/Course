'''
构建一个三层前向传播网络
'''
import tensorflow as tf
def creat_3layer(x,y_onehot,lr):
    '''
    三层前向传播网络，输入为MNIST图片集，第一层输入为784输出为256，第二层输出为128第三层输出为10

    :return:
    '''
    w1 = tf.Variable(tf.random.truncated_normal([784,256]))
    w2 = tf.Variable(tf.random.truncated_normal([256,128]))
    w3 = tf.Variable(tf.random.truncated_normal([128,10]))
    b1 = tf.Variable(tf.random.zeros([256]))
    b2 = tf.Variable(tf.random.zeros([128]))
    b3 = tf.Variable(tf.random.zeros([10]))
    x=tf.reshape(x,[-1,784])
    h1=x@w1+tf.broadcast_to(b1,[1,256])                    #显示的broadcast变形可以不写
    h1=tf.nn.rule(h1)
    h2 = h1 @ w2 + b2
    h2 = tf.nn.rule(h2)
    out = h2@w3+b3
    #将真实的标注张量 y 转变为 one-hot 编码，并计算与 out 的均方差：
    loss = tf.square(y_onehot - out)
    loss=tf.reduce_mean(loss)
    #通过 tape.gradient()函数求得网络参数到梯度
    grads = tf.tape.gradient(loss, [w1, b1, w2, b2, w3, b3])
    w1.assign_sub(lr * grads[0])
    b1.assign_sub(lr * grads[1])
    w2.assign_sub(lr * grads[2])
    b2.assign_sub(lr * grads[3])
    w3.assign_sub(lr * grads[4])
    b3.assign_sub(lr * grads[5])