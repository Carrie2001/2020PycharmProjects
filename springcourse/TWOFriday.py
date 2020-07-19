print("abc")    # abc
print('abc')    # abc
print('"abc"')  # "abc"
print(100, "100")   # 整数，字符

# 重新设置分隔符
print(100, 'hello', 200, sep='\n')  # 分行输出
# end
print(100, end='abc')
print(100, end='abc\n')
print(100, end='abc\n\n')   # 一个参数逗号之后加上空格与下一个参数分开
import turtle
# 使用import，调用函数时候要math.函数名
# 函数名与库里面的函数名重名了，或者是标识符重名了，没有特别的要紧
# 对于import是直接用math.pi来调用还是用from math import sin,pi
# 写一个py文件，例如test.py,import test之后可以直接调用里面的东西，test.x等等。所以说我们import的包可以是文件
#如果有两个包，里面有重名的东西，利用from test import x，from test1 import x，会被后面的import覆盖掉，
# 视情况而论选择使用from这种的还是使用math.pi，当然建议使用math.pi这种
# import和#include有什么区别吗
# #include 是直接把.h的文件直接copy过来，后面没有;，是个预编译，不是命令
# 但是，python中的import是实实在在的命令，不仅仅是copy文件，我们改原来文件的x，y的值是不会影响原来的文件的值得，但是我们的确能到改了之后的数值，
# 为什么再次import之后，那个数值还是我们改了之后的值呢？因为import同一个文件在一个程序中只回执行第一次，因为import的文件可能比较大，在设计之初就是这么设定的
# python只要在调用之前import就可以，不用在乎在哪个位置定义，但是我们尽量统一定义在开始两行
# import math as m，就是把math库的用m来指代，就是改了名字，只能用m.pi等等，就不能再用math.pi了（引入包，库，模块等都是一样的）


