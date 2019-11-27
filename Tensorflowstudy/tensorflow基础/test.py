'''
构建一个三层前向传播网络
'''
import tensorflow as tf
import tensorflow as tf
from tensorflow import keras


def creat_3layer(train_db):
    lr = 0.00001
    '''
    三层前向传播网络，输入为MNIST图片集，第一层输入为784输出为256，第二层输出为128第三层输出为10

    :return:
    '''
    w1 = tf.Variable(tf.random.truncated_normal([784,256]))
    w2 = tf.Variable(tf.random.truncated_normal([256,128]))
    w3 = tf.Variable(tf.random.truncated_normal([128,10]))
    b1 = tf.Variable(tf.zeros([256]))
    b2 = tf.Variable(tf.zeros([128]))
    b3 = tf.Variable(tf.zeros([10]))
    for step, (x, y) in enumerate(train_db):
        x = tf.reshape(x, (-1, 784))
        with tf.GradientTape() as tape:
            h1=x@w1+tf.broadcast_to(b1,[1,256])                    #显示的broadcast变形可以不写
            h1=tf.nn.relu(h1)
            h2 = h1 @ w2 + b2
            h2 = tf.nn.relu(h2)
            out = h2@w3+b3
            loss = tf.square(y - out)
            loss=tf.reduce_mean(loss)
            if step%80==0:
                print(loss)


        #通过 tape.gradient()函数求得网络参数到梯度
        grads =tape.gradient(loss, [w1, b1, w2, b2, w3, b3])
        w1.assign_sub(lr * grads[0])
        b1.assign_sub(lr * grads[1])
        w2.assign_sub(lr * grads[2])
        b2.assign_sub(lr * grads[3])
        w3.assign_sub(lr * grads[4])
        b3.assign_sub(lr * grads[5])
'''
a=[[1,2],[3,4]]
b=[[5,6],[7,8]]
c=tf.data.Dataset.from_tensor_slices((a,b))
for i in c:
    print(i)
'''
# 加载 MNIST 数据集
(x, y), (x_test, y_test) = keras.datasets.mnist.load_data()
'''
数据加载进入内存后，需要转换成 Dataset 对象，以利用 TensorFlow 提供的各种便捷 功能。
通过 Dataset.from_tensor_slices 可以将训练部分的数据图片 x 和标签 y 都转换成 Dataset 对象： 
from_tensors()在形式上与from_tensor_slices()很相似，但其实from_tensors()方法出场频率上比from_tensor_slices()差太多，因为from_tensor_slices()的功能更加符合实际需求，且返回的TensorSliceDataset对象也提供更多的数据处理功能。
from_tensors()方法在接受list类型参数时，将整个list转换为Tensor对象放入Dataset中，当接受参数为tuple时，将tuple内元素转换为Tensor对象，然后将这个tuple放入Dataset中。
from_generator(）方法接受一个可调用的生成器函数作为参数，在遍历Dataset对象时，通过通用生成器函数继续生成新的数据供训练和测试模型使用，这在大数据集合中很实用。
from_tensor_slices()方法接受参数为list时，将list各元素依次转换为Tensor对象，然后依次放入Dataset中；更为常见的情况是接受的参数为tuple，
在这种情况下，要求tuple中各元素第一维度长度必须相等，from_tensor_slices()方法会将tuple各元素第一维度进行拆解，
然后将对应位置的元素进行重组成一个个tuple依次放入Dataset中，这一功能在重新组合数据集属性和标签时很有用。
另外，from_tensor_slices()方法返回的TensorSliceDataset对象支持batch、shuffle等等功能对数据进一步处理。
'''
train_db = tf.data.Dataset.from_tensor_slices((x, y))
'''
随机打散
'''
train_db = train_db.shuffle(10000)
'''
设置批训练
其中 128 为 batch size 参数，即一次并行计算 128 个样本的数据。Batch size 一般根据用户 的 GPU 显存资源来设置，
'''
train_db=train_db.batch(128)
train_db=train_db.repeat(8)

def preprocess(x, y): # 自定义的预处理函数
# 调用此函数时会自动传入 x,y 对象，shape 为[b, 28, 28], [b]
    # 标准化到 0~1
    x = tf.cast(x, dtype=tf.float32) / 255.
    x = tf.reshape(x, [-1, 28*28])     # 打平
    y = tf.cast(y, dtype=tf.int32)    # 转成整形张量
    y = tf.one_hot(y, depth=10)    # one-hot 编码
    # 返回的 x,y 将替换传入的 x,y 参数，从而实现数据的预处理功能
    return x,y
# 预处理函数实现在 preprocess 函数中，传入函数引用即可
train_db = train_db.map(preprocess)
creat_3layer(train_db)
