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
    out = tf.nn.conv2d(x, w, strides=1, padding=[[0, 0], [0, 0], [0, 0], [0, 0]])
    print(out)
creat_nn_layer()
