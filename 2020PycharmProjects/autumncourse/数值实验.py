import numpy as np
def sigmoid(x):
#激活函数
   return 1/(1+np.exp(-x))
#输入数据
input = np.array([[0.35], [0.9]])
#第一层权重参数
w1 = np.array([[0.1, 0.8], [0.4, 0.6]])
#第二层权重参数
w2 = np.array([0.3, 0.9])
  #真实值
real = np.array([[0.5]])
for s in range(0,100,1):
    pq = sigmoid(np.dot(w1,input))  #第一层输出
    output = sigmoid(np.dot(w2,pq)) #第二层输出,也即是最终输出
    e = output-real                 #误差
    if np.square(e)/2<0.01:
       break
    else:
        #按照梯度下降计算权重参数，应用链式法则计算权重参数的更新量
       w2 = w2 - e*output*(1-output)*pq.T
       w1 = w1 - e*output*(1-output)*w2*pq.T*(1-pq.T)*input
print(w1,'\n',w2)
#输出最终结果
print(output)
