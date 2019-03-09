import numpy as np
import matplotlib.pyplot as plt

#生成一个等差数列
line = np.linspace(-5, 5, 200)

#画出非线性矫正的图形表示
plt.plot(line, np.tanh(line), label = 'tanh')
plt.plot(line, np.maximum(line,0), label = 'relu')

#设置图注位置
plt.legend(loc = 'best')
plt.xlabel('x')
plt.ylabel('relu(x) and tanh(x)')
plt.show()


from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
wine = load_wine()
X = wine.data[:,:2]
y = wine.target
X_train， X_test, y_train, y_test = train_test_split(X, y, random_state = 0)
#定义分类器
mlp = MLPClassifier(solver = 'lbfgs')
mlp.fit(X_train, y_train)

from matplot.colors import ListedColormap

#使用不同色块表示不同分类
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])
x_min, x_max = X_train[:, 0].min() -1, X_train[:, 0].max() + 1
x_min, x_max = X_train[:, 1].min() -1, X_train[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, .02),
                     np.arange(y_min, y_max, .02))

Z = mlp.predict(np.c_[xx.ravel(), yy.ravel()])

Z = Z.reshape(xx.shape)
plt.figure()
plt.pcolormesh(xx, yy, Z, cmap = cmap_light)

#将数据点用散点图表示出来
plt.scatter(X[:, 0], X[:, 1], c = y, edgecolor = 'k', s = 60)
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.title('MLPClassifier:solver=lbfgs')
plt.show()

#设定隐藏层的结点数为10
mlp_20 = MLPClassifier(solver = 'lbfgs', hidden_layer_sizes = [10])
mlp_20.fit(X_train, y_train)
Z1 = mlp_20.predict(np.c_[xx.ravel(), yy.ravel()])

Z1 = Z1.reshape(xx.shape)
plt.figure()
plt.pcolormesh(xx, yy, Z1, cmap = cmap_light)

#使用散点图画出X
plt.scatter(X[:, 0], X[:, 1], c = y, edgecolor = 'k', s = 60)
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.title('MLPClassifier:nodes=10')
plt.show()


#设置神经网络有两个节点数为10的隐藏层
mlp_2L = MLPClassifier(solver = 'lbfgs', hidden_layer_sizes = [10,10])
mlp_2L.fit(X_train, y_train)
Z1 = mlp_2L.predict(np.c_[xx.ravel(), yy.ravel()])
#用不同色彩区分分类
Z1 = Z1.reshape(xx.shape)
plt.figure()
plt.pcolormesh(xx, yy, Z1, cmap = cmap_light)
#用散点图画出X
plt.scatter(X[:, 0], X[:, 1], c = y, edgecolor = 'k', s = 60)
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.title('MLPClassifier:2layers')
plt.show()

#设置激活函数为tanh
mlp_tanh = MLPClassifier(solver = 'lbfgs', hidden_layer_sizes = [10, 10],
                         activation = 'tanh')
mlp_tanh.fit(X_train, y_train)
#重新画图
Z2 = mlp_tanh.predict(np.c_[xx.ravel(), yy.ravel()])

Z2 = Z2.reshape(xx.shape)
plt.figure()
plt.pcolormesh(xx, yy, Z2, cmap = cmap_light)
#用散点图画出X
plt.scatter(X[:, 0], X[:, 1], c = y, edgecolor = 'k', s = 60)
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.title('MLPClassifier:2layers with tanh')
plt.show()

#修改参数的alpha模型
mlp_alpha = MLPClassifier(solver = 'lbfgs', hidden_layer_sizes = [10, 10],
                         activation = 'tanh', alpha = 1)
mlp_alpha.fit(X_train, y_train)
#重新绘制图形
Z3 = mlp_alpha.predict(np.c_[xx.ravel(), yy.ravel()])

Z3 = Z3.reshape(xx.shape)
plt.figure()
plt.pcolormesh(xx, yy, Z3, cmap = cmap_light)
plt.scatter(X[:, 0], X[:, 1], c = y, edgecolor = 'k', s = 60)
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.title('MLPClassifier:alpha = 1')
plt.show()


from
