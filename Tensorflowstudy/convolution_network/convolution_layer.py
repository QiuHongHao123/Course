import tensorflow as tf
'''
建立卷积层
'''
def creat_nn_layer():
    x=tf.random.normal([2,5,5,3])            #模拟输入，3 通道，高宽为 5
    # 需要根据[k,k,cin,cout]格式创建 W 张量，4 个 3x3 大小卷积核
    w = tf.random.normal([3,3,3,4])
    # 步长为 1, padding 为 0,
    '''
    特别地，通过设置参数 padding='SAME'，strides=1 可以直接得到输入、输出同大小的 卷积层，其中 padding 的具体数量由 TensorFlow 自动计算并完成填充操作： 
    '''
    # 需要注意的是, padding=same 只有在 strides=1 时才是同大小 当𝑠 > 时，设置 padding='SAME'将使得输出高、宽将成1 𝑠 倍地减少
    out = tf.nn.conv2d(x, w, strides=1, padding=[[0, 0], [1, 1], [1, 1], [0, 0]])
    print(out.shape)
    '''
    卷积层类创建卷积层
    '''
    layer=tf.keras.layers.Conv2D(4,kernel_size=3,strides=1,padding='SAME')
    #创建 4 个 3x4 大小的卷积核，竖直方向移动步长 𝑠ℎ = 2，水平方向移动步长𝑠𝑤 = 1
    layer1=tf.keras.layers.Conv2D(4,kernel_size=(3,4),strides=(2,1),padding='SAME')
    print(layer(x).shape)
creat_nn_layer()
