from tensorflow import keras
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
def load_data():
    dataset_path = keras.utils.get_file("auto-mpg.data", "http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data")
    # 利用 pandas 读取数据集，字段有效能（公里数每加仑），气缸数，排量，马力，重量 # 加速度，型号年份，产地
    column_names = ['MPG','Cylinders','Displacement','Horsepower','Weight','Acceleration', 'Model Year', 'Origin']
    raw_dataset = pd.read_csv(dataset_path, names=column_names,na_values = "?", comment='\t',sep=" ",skipinitialspace=True)
    dataset = raw_dataset.copy()
    print(dataset.head())
    print(dataset.isna().sum()) # 统计空白数据
    dataset = dataset.dropna() # 删除空白数据项
    print(dataset.isna().sum()) # 再次统计空白数据
    # 处理类别型数据，其中 origin 列代表了类别 1,2,3,分布代表产地：美国、欧洲、日本
    # 先弹出(删除并返回)origin 这一列
    origin = dataset.pop('Origin')
    # 根据 origin 列来写入新的 3 个列
    dataset['USA'] = (origin == 1)*1.0
    dataset['Europe'] = (origin == 2)*1.0
    dataset['Japan'] = (origin == 3)*1.0
    dataset.tail()
    # 切分为训练集和测试集
    train_dataset = dataset.sample(frac=0.8,random_state=0)
    test_dataset = dataset.drop(train_dataset.index)
    # 移动 MPG 油耗效能这一列为真实标签 Y
    train_labels = train_dataset.pop('MPG')
    test_labels = test_dataset.pop('MPG')
    # 查看训练集的输入 X 的统计数据
    train_stats = train_dataset.describe()
    train_stats = train_stats.transpose()    #转置
    # 标准化数据
    def norm(x):
        return (x - train_stats['mean']) / train_stats['std']
    normed_train_data = norm(train_dataset)
    normed_test_data = norm(test_dataset)
    print(normed_train_data.shape)
    print(normed_train_data.shape)
    train_db = tf.data.Dataset.from_tensor_slices((normed_train_data.values,train_labels.values))  # 构建 Dataset 对象
    train_db = train_db.shuffle(100).batch(32)  # 随机打散，批量化
    return train_db


class Network(keras.Model):
    # 回归网络
    def __init__(self):
        super(Network, self).__init__()
        # 创建 3 个全连接层
        self.fc1 = keras.layers.Dense(64, activation='relu')
        self.fc2 = keras.layers.Dense(64, activation='relu')
        self.fc3 = keras.layers.Dense(1)

    def call(self, inputs, training=None, mask=None):
        # 依次通过 3 个全连接层
        x = self.fc1(inputs)
        x = self.fc2(x)
        x = self.fc3(x)
        return x
def do_train(train_db):
    graph=[]
    model = Network() # 创建网络类实例
    # 通过 build 函数完成内部张量的创建，其中 4 为任意的 batch 数量，9 为输入特征长度
    model.build(input_shape=(4, 9))
    print(model.summary()) # 打印网络信息
    optimizer = tf.keras.optimizers.RMSprop(0.001) # 创建优化器，指定学习率

    for epoch in range(200):  # 200 个 Epoch
        for step, (x,y) in enumerate(train_db): # 遍历一次训练集
            # 梯度记录器
            with tf.GradientTape() as tape:
                out = model(x)  # 通过网络获得输出
                loss = tf.reduce_mean(keras.losses.MSE(y, out)) # 计算 MSE
                mae_loss = tf.reduce_mean(keras.losses.MAE(y, out)) # 计算 MAE
            # 计算梯度，并更新
            grads = tape.gradient(loss, model.trainable_variables)
            optimizer.apply_gradients(zip(grads, model.trainable_variables))
        graph.append(mae_loss)
    plt.figure("loss")
    plt.xlabel("steps", fontsize=14)
    plt.ylabel("loss", fontsize=14)
    plt.plot(graph)
    plt.show()
train_db=load_data()
do_train(train_db)