""""
def hanoi(Rings,fromWhich,byWhich,toWhich):
    if Rings ==1:
        print("move from",fromWhich,"to",toWhich)
        return
    hanoi(Rings - 1, fromWhich,toWhich,byWhich)
    print("move from", fromWhich, "to", toWhich)
    hanoi(Rings - 1, byWhich,fromWhich,toWhich)

hanoi(2,1,2,3)
"""
"""
import math
import matplotlib.pyplot as plt
import numpy as np

def sigmoid(x):
    return 1 / (1 + math.e**(-x))  #np.exp(-x)

def diffsigmoid(x):
    return sigmoid(x)*(1-sigmoid(x))

def plot_sigmoid():
    x = np.arange(-10, 10, 0.1)
    y = sigmoid(x)
    fig = plt.figure()

    ax = fig.add_subplot(111)
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.axis['bottom'].set_axisline_style("-|&gt;",size=1.5)
    ax.spines['left'].set_position(('data', 0))
    ax.plot(x, y)
    plt.xlim([-10.05, 10.05])
    plt.ylim([-0.02, 1.02])
    plt.tight_layout()
    plt.savefig("sigmoid.png")
    plt.show()

if __name__ == "__main__":
    plot_sigmoid()
"""
"""
import math
import matplotlib.pyplot as plt
import numpy as np

def sigmoid(x):
    return 1.0/(1.0+math.e**(-x))
def diffsigmoid(x):
    return sigmoid(x)*(1-sigmoid(x))
x = np.linspace (-10,10,100)
y = sigmoid(x)
z=diffsigmoid(x)

plt.plot(x,y,label="Sigmoid",color = "blue")
plt.plot(x,z,label="Sigmoid diff",color = "red")
plt.legend()

plt.show()
"""
import matplotlib.pyplot as plt
import numpy as np

def sici(x):
    return x**4 - 3*x**3 + 1.5*x**2 -4.0

def diffsici(x):
    return 4*x**3 - 9*x**2 + 3*x
x = np.linspace (-10,10,100)
y = sici(x)
z=diffsici(x)

plt.plot(x,y,label="sici",color = "blue")
plt.plot(x,z,label="sici diff",color = "red")
plt.legend()
plt.show()

lr = 0.1 #学习率
x = 1.5 #初值
# 初值和学习率对于极值点的影响
for i in range(1000):
    x = x - lr*(4*x**3 - 9*x**2 + 3*x)
    print(x)



