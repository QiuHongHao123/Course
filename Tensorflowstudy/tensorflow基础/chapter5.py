import tensorflow as tf
from tensorflow import keras
import numpy as np
'''
第五章有关内容
向量合并和分割
'''
def conbine():
    '''
    张量的合并可以使用拼接(Concatenate)和堆叠 (Stack)操作实现，拼接并不会产生新的维度，而堆叠会产生新的维度
    :return:
    '''
    '''
    合并操作可以在任意的维度上进行，唯一的约束是非合并维度的长度必须一致。
    比如 shape 为[4,32,8]和 shape 为[6,35,8]的张量则不能直接在班级维度上进行合并，
    因为学生数维度的 长度并不一致，一个为 32，另一个为 35
    '''
    a = tf.random.normal([4, 35, 8])  # 模拟成绩册 A
    b = tf.random.normal([6,35,8])   # 模拟成绩册 B
    c=tf.concat([a, b], axis=0)
    print(c.shape)
    '''
    使用 tf.stack(tensors, axis)可以合并多个张量 tensors，
    其中 axis 指定插入新维度的位置，axis 的用法与 tf.expand_dims 的一致，
    当axis ≥ 0时，在 axis 之前插入;当axis < 0时， 在 axis 之后插入新维度
    '''
    c=tf.random.normal([4, 35, 8])
    d=tf.random.normal([4, 35, 8])
    e=tf.stack([c,d],0)
    print(e.shape)
def split():
    '''
    张量分割
    :return:
    '''
    '''
    通过 tf.split(x,num_or_size_splits ,axis )可以完成张量的分割操作
    num_or_size_splits：切割方案。当 num_or_size_splits 为单个数值时，如 10，表示切割 为 10 份；
    当 num_or_size_splits 为 List 时，每个元素表示每份的长度，如[2,4,2,2]表示 切割为 4 份，每份的长度分别为 2,4,2,2 
    '''
    a=tf.random.normal([4,35,8])
    b=tf.split(a,[1,2,1],0)
    for i in b:
        print(i.shape)
def data_statistics():
    '''
    数据统计
    :return:
    '''
    '''
    L1 范数，定义为向量𝒙的所有元素绝对值之和 
    ‖𝒙‖1 = ∑|𝑥𝑖| 𝑖
    L2 范数，定义为向量𝒙的所有元素的平方和，再开根号 
    ‖𝒙‖2 = √∑|𝑥𝑖|2 𝑖
    ∞ −范数，定义为向量𝒙的所有元素绝对值的最大值： 
    '''
    '''
    在 TensorFlow 中，可以通过 tf.norm(x, ord)求解张量的 L1, L2, ∞等范数，其中参数 ord 指定为 1,2 时计算 L1, L2 范数，指定为 np.inf 时计算∞ −范数： 
    '''
    x=tf.random.normal([4,4])
    print(x)
    '''
    注意范数的结果为张量形式
    '''
    print(tf.norm(x,1),tf.norm(x,2),tf.norm(x,np.inf))
    '''
    最大最小和均值
    当不指定 axis 参数时，tf.reduce_*函数会求解出全局元素的最大、最小、均值、和
    '''
    print(tf.reduce_max(x, axis=1))
    print(tf.reduce_min(x, axis=1))
    print(tf.reduce_mean(x, axis=1))
def compare():
    '''
    张量比较
    :return:
    '''
    out = tf.random.normal([100, 10])
    out = tf.nn.softmax(out, axis=1)  # 输出转换为概率
    pred = tf.argmax(out, axis=1)     #选取预测值

    y = tf.random.uniform([100], dtype=tf.int64, maxval=10)# 真实标签
    result=tf.equal(pred,y)
    print(result)
    result=tf.cast(result,tf.int8)
    result=tf.reduce_sum(result)
    print("accuracy=",int(result)/100)
def pad_and_copy():
    '''
    填充和复制
    :return:
    '''
    '''
    填充操作可以通过 tf.pad(x, paddings)函数实现，
    paddings 是包含了多个 [𝐿𝑒𝑓𝑡 𝑃𝑎𝑑𝑑𝑖𝑛𝑔,𝑅𝑖𝑔ℎ𝑡 𝑃𝑎𝑑𝑑𝑖𝑛𝑔]的嵌套方案 List，如[[0,0],[2,1],[1,2]]表示第一个维度不填充，
    第二个维度左边(起始处)填充两个单元，右边(结束处)填充一个单元，
    第三个维度左边 填充一个单元，右边填充两个单元。
    这什么sb函数
    '''
    a= tf.constant([7, 8, 1, 6])
    b = tf.pad(a, [[0, 2]])  # 填充
    print(b)
    '''
    keras.preprocessing.sequence.pad_sequences 可以快速完成句子的填充和截断工作
    '''
    a=tf.expand_dims(a,axis=0)
    c=keras.preprocessing.sequence.pad_sequences(a,maxlen=5,truncating='post',padding='post')
    print(c)
def other_operation():
    '''
    数字限幅， 根据索引号收集数据
    :return:
    '''
    '''
    在 TensorFlow 中，可以通过 tf.maximum(x, a)实现数据的下限幅：𝑥 ∈ [𝑎,+∞)；可以 通过 tf.minimum(x, a)实现数据的上限幅：𝑥 ∈ (−∞,𝑎
   
    '''
    '''
    tf.gather 
   对于不规则的索引方 式，比如，需要抽查所有班级的第 1,4,9,12,13,27 号同学的成绩，则切片方式实现起来非常麻烦，而 tf.gather 则是针对于此需求设计的，使用起来非常方便： 
    收集第 1,4,9,12,13,27 号同学成绩 
    tf.gather(x,[0,3,8,11,12,26],axis=1) 
    '''
    '''
    通过 tf.gather_nd，可以通过指定每次采样的坐标来实现采样多个点的目的。
    '''
    '''
    除了可以通过给定索引号的方式采样，还可以通过给定掩码(mask)的方式采样。
    tf.boolean_mask(x,mask=[True, False,False,True],axis=0) 
    太多了用到再看那个文档吧
    '''
#conbine()
#split()
#data_statistics()
#compare()
pad_and_copy()