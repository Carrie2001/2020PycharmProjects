# region 已知三角形三点的坐标，求三个角
# round() 方法返回浮点数x的四舍五入值
# from math import sqrt, acos, degrees
# x1, y1, x2, y2, x3, y3 = eval(input("Enter six coordinates of three points \
# separated by commas like x1, y1, x2, y2, x3, y3: "))
# # x1, y1, x2, y2, x3, y3 = map(int, input().split())
# a = sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3))
# b = sqrt((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3))
# c = sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
# A = degrees(acos((a * a - b * b - c * c) / (-2 * b * c)))
# B = degrees(acos((b * b - a * a - c * c) / (-2 * a * c)))
# C = degrees(acos((c * c - b * b - a * a) / (-2 * a * b)))
# print("The three angles are ", round(A * 100) / 100.0, round(B * 100) / 100.0, round(C * 100) / 100.0)
# endregion

# region 现利用 Turtle 绘制三角形、正方形、五边形、六边形以及圆
"""
import turtle
turtle.pensize(3)                 # Set pen thickness to 3 pixels，设置画笔的宽度
turtle.pencolor("red")            # 设置画笔的颜色

turtle.penup()                    # Pull the pen up，另起地方绘制
turtle.goto(-200, -50)            # 讲画笔移动到（-200，-500）的位置
turtle.pendown()                  # Pull the pen down,移动时绘制图形，缺省时也为绘制

turtle.circle(40, steps=3)        # Draw a triangle
'''
turtle.circle(radius, extent=None, steps=None)<=>
radius(半径)：半径为正(负)，表示圆心在画笔的左边(右边)画圆
extent(弧度)：(optional)
steps (optional)：(做半径为radius的圆的内切正多边形，多边形边数为steps)
'''

turtle.penup()
turtle.goto(-100, -50)
turtle.pendown()

turtle.circle(40, steps=4)        # Draw a square

turtle.penup()
turtle.goto(0, -50)
turtle.pendown()

turtle.circle(40, steps=5)        # Draw a pentagon

turtle.penup()
turtle.goto(100, -50)
turtle.pendown()

turtle.circle(40, steps=6)        # Draw a hexagon

turtle.penup()
turtle.goto(200, -50)
turtle.pendown()

turtle.circle(40)                 # Draw a circle

turtle.done()
"""
# endregion

# region 提示用户输入五边形的边长，然后显示面积（保留 2 位小数）
# from math import sin, cos, tan, pi
# n = int(input("输入五边形的边长："))
"""
a = 2 * pi / 5
b = pi - a
s = n * n * sin(b) + 0.25 * n * n * tan(a)
"""
# s = 5 * n * n / 4 / tan(pi / 5)
# print("{:.2f}".format(s))
# endregion

# region 绘制五个同切圆
"""
import turtle                       # 导入turtle库
turtle.setup(700, 700, 100, 100)    # 设置窗口宽高和距离左上距离
turtle.pensize(5)                   # 设置画笔粗细
turtle.pencolor('red')              # 设置画笔颜色
turtle.right(90)                    # 设置笔尖右旋90度
turtle.penup()                      # 设置笔尖朝上
turtle.fd(100)                      # 设置前进100像素
turtle.pendown()                    # 设置笔尖朝下
turtle.seth(0)                      # 设置（前进）方向归零
turtle.circle(50)                   # 画半径50像素的圆
turtle.circle(100)                  # 画半径100像素的圆
turtle.circle(150)                  # 画半径150像素的圆
turtle.circle(200)                  # 画半径150像素的圆
turtle.hideturtle()                 # 设置隐藏笔尖
turtle.done()
"""
# endregion

# region 现绘制三角形、正方形、五边形、六边形以及圆，并填充不同的颜色，程序也为图形添加文本标题

# endregion

# region something about GBK UTF8 UNICODE
"""
Unicode 是内存,编码表示方案（是规范），而 UTF 是如何保存和传输 Unicode 的方案（是实现）
我们存储文件的时候，可以用 GBK，也可以用 utf8，但是内存里表示字符的时候，可以用 Unicode
"""
"""
s = 'aA1中国'
print(len(s))     # 字符串长度为5
print(s[3])       # Python内部，内存里面是用Unicode表示这些字符串的，存储字符串或者是从文件中读取字符串，我们必须知道存储编码
"""
"""
encode & decode
编码 & 解码
"""
"""
g = s.encode('gbk')
print(g)                    # b'aA1\xd6\xd0\xb9\xfa' 是一个b开头的，字节码
u = s.encode('utf8')
print(u)

print(g.decode('gbk'))
print(u.decode('utf8'))
# print(g.decode('utf8'))是错误的
"""
# endregion

# region something about Encoding and Save original string to file
"""
为了解决Windows系统的文件路径搜索问题，python提供三种做法
1.把Windows系统文件路径中的反斜杠“\”改为正斜杠“/”
2.要是想输入“\”,就要多加一个写成“\\”，取消转义作用
3.在字符串前面加上一个“r”，提示解释器，按照原来的字符串进行处理
"""
"""
open 函数
open(name[, mode[, buffering]])
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
name : 一个包含了你要访问的文件名称的字符串值
mode : 决定了打开文件的模式：只读，写入，等。参数是非强制的，默认文件访问模式为只读(r)
buffering : 若buffering 的值被设为 0，就不会有寄存。若buffering 的值取 1，访问文件时会寄存行。
若将 buffering 的值设为大于 1 的整数，表明了这就是的寄存区的缓冲大小。如果取负值，寄存区的缓冲大小则为系统默认。
file: 必需，文件路径（相对或者绝对路径）  mode: 可选，文件打开模式
buffering: 设置缓冲  encoding: 一般使用utf8  errors: 报错级别
newline: 区分换行符  closefd : 传入的file参数类型 opener:
"""
s = 'aA1中国'
fp = open(r'C:\Users\HP\Desktop\test.txt', 'w', encoding='utf8')
# 'w' 打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件
print(fp.write(s))                                                   # 将字符串写入文件，返回的是写入的字符长度(写入字符串以外的数据,先将他转换为字符串)
fp.close()                                                           # 关闭文件,关闭后文件不能再进行读写操作
# 此时查看文件，文件用utf8存储，但是不含 EF BB BF 是这样的utf8 的 BOM 标记
# 如果现在在python直接用fp.read()打开文件是无法解码的，因为Windows 系统默认编码是 GBK,Linux系统默认是utf8编码
# 我们选择利用encoding重新指定编码
fp = open(r'C:\Users\HP\Desktop\test.txt', 'r', encoding='utf8')
# 'r' 以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式
print(fp.read())
fp = open(r'C:\Users\HP\Desktop\test.txt', 'rb')
# 'rb' 以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等
print(fp.read())
# endregion