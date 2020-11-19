"""
#利用蒙特卡洛方法计算PI值
from random import random
from math import sqrt
from time import clock
DARTS = 2**26  #这个时候已经比较精确了，耗时也将近1分钟了。修改DARTS可以进一步提高计算精度。
hits=0
clock()        #引入time.clock()用于统计耗时
for i in range(1,int(DARTS)):
    x,y =random(),random()
    dist = sqrt(x**2+y**2)
    if dist <=1.0:
        hits =hits+1
pi = 4*(hits/DARTS)
print("PI的值是%s"%pi)
print("程序运行的时间是%-5.5ss"% clock())
"""
from random import random
from time import clock
from matplotlib import pyplot as plt
import numpy as np

plt.figure(figsize = (12,12))
X = np.linspace(0, 1, 256,endpoint = True)
C = np.sqrt(1 - X ** 2)
plt.plot(X, C, color = "b", linewidth = 6, linestyle = ":", label = "e ^ ( - (2x) ^ 2)")
#ax = plt.gca()
plt.fill_between(X,C,where = (X > 0),color = '#EFB582' , alpha = 0.4) # 填充颜色
n = 2 ** 10 # 设置投点次数
clock()
for i in range(1,n):
    x,y = random(),random()
    dist = np.sqrt(x ** 2+y ** 2)
    plt.scatter(x,y, s = 20, alpha = 0.7, marker = 'o')
    if dist <= 1.0:
        hist = hist+1
pi = 4 * (hist / n)
print('pi is %s'%pi)
print('elaspe is %ss'%clock())


plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20) # 刻度字体大小

plt.xlim(-0.05,1.05)
plt.ylim(-0.05,1.05)

plt.show()