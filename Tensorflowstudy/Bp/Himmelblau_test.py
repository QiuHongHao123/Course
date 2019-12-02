import tensorflow as tf
import numpy as np
from typing import List
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
'''
Himmelblau 函数是用来测试优化算法的常用样例函数之一，它包含了两个自变量 𝑥,𝑦，数学表达式是： 𝑓(𝑥,𝑦) = (𝑥^2 + 𝑦 − 11)^2 + (𝑥 + 𝑦^2 − 7)^2 
'''
def Himmelblau(input:List):
    return (pow(input[0],2)+input[1]-11)**2+(input[0]+pow(input[1],2)-7)**2
def draw():
    x = np.arange(-6, 6, 0.1)
    y = np.arange(-6, 6, 0.1)
    # 生成 x-y 平面采样网格点，方便可视化
    X, Y = np.meshgrid(x, y)
    print('X,Y maps:', X.shape, Y.shape)
    Z=Himmelblau([X,Y])# 绘制 himmelblau 函数曲面
    fig = plt.figure('himmelblau')
    ax = Axes3D(fig)
    ax.plot_surface(X, Y, Z)
    ax.view_init(60, -30)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    return fig
draw()
def do_youhua():
    x=tf.Variable(tf.constant([4.0,0]))
    epoch=200
    graphdata=[]
    for i in range(epoch):
        with tf.GradientTape() as tape:
            out=Himmelblau(x)
        # 反向传播
        grads = tape.gradient(out, [x])[0]
        # 更新参数,0.01 为学习率
        x.assign_sub(0.01 * grads)
        graphdata.append(x)
        if i %10==0:
            print("step=",i,"x=",x,"f(x)=",Himmelblau(x))
    fig=draw()
    Z=[]
    X=[]
    Y=[]
    for i in graphdata:
        X.append(i[0])
        Y.append(i[1])
        Z.append(Himmelblau(i))
    plt.plot(X,Y,Z)
    plt.show()

do_youhua()


