'''
19.11.20
Tensorflow2.0学习：第一天，学习基本语法数据类型等
必须通过 TensorFlow 规定的方式去创建张量，而不能使用 Python 语言的标准变量创建方式。
张量分已优化和未优化张量：Constant 和 Variable
在 TensorFlow 中，可以通过多种方式创建张量，如从 Python List 对象创建，从 Numpy 数组创建，或者创建采样自某种已知分布的张量等。
'''
import tensorflow as tf
import numpy as np

def creat_constant():
    a=tf.constant(2.2)
    b=tf.constant([1.0,2.1])
    c=tf.constant([[1,2],[3,4]])
    print(a,b,c)
    pi1=tf.constant(np.pi,dtype=tf.float32)
    pi2 = tf.constant(np.pi, dtype=tf.float64)
    print(pi1,pi2)
    #类型转换
    pi3=tf.cast(pi1,tf.double)
    print(pi3)
    '''
    从nump 和矩阵中直接创建张量
    '''
    nump=np.array([[1,2],[3,4]])
    nump1=tf.constant(nump)
    print(nump,nump1)
    '''
    创建全0全1或者全指定初始化值的张量
    '''
    constant0=tf.zeros([3,4])
    constant1=tf.ones([3,4])
    constant3=tf.fill([3,4],3)
    print(constant0,constant1,constant3)
    '''
    通过 tf.zeros_like, tf.ones_like 可以方便地新建与某个张量 shape 一致，内容全 0 或全 1 的张量。例如，创建与张量 a 形状一样的全 0 张量：
    '''
    constant1_1=tf.ones_like(constant0)
    print(constant1_1)
    '''
    通过 tf.random.normal(shape, mean=0.0, stddev=1.0)可以创建形状为 shape，均值为 mean，标准差为 stddev 的正态分布𝒩(𝑚𝑒𝑎𝑛,𝑠𝑡𝑑𝑑𝑒𝑣2)。
    '''
    normal1=tf.random.normal([3,4],2,1)
    '''
    通过 tf.random.uniform(shape, minval=0, maxval=None, dtype=tf.float32)可以创建采样自 [𝑚𝑖𝑛𝑣𝑎𝑙,𝑚𝑎𝑥𝑣𝑎𝑙]区间的均匀分布的张量。
    '''
    uniform=tf.random.uniform([3,4],0,3)
    '''
    通过 tf.range(start, limit, delta=1)可以创建[𝑠𝑡𝑎𝑟𝑡,𝑙𝑖𝑚𝑖𝑡)，步长为 delta 的序列，不包含 limit 本身
    '''
    range1=tf.range(1,10,delta=2)
def creat_variable():
    '''
    Variable指待优化张量：tf.Variable。
    tf.Variable 类型在普通的张量类 型基础上添加了 name，trainable 等属性来支持计算图的构建。
    由于梯度运算会消耗大量的 计算资源，而且会自动更新相关参数，
    对于不需要的优化的张量，如神经网络的输入 X， 不需要通过 tf.Variable 封装；
    相反，对于需要计算梯度并优化的张量，如神经网络层的W 和𝒃，需要通过 tf.Variable 包裹以便 TensorFlow 跟踪相关梯度信息。
    '''
    a=tf.Variable([[1,2],[1,2]])
    a=tf.one_hot(a,depth=10)
    print(a)
creat_constant()
#creat_variable()
