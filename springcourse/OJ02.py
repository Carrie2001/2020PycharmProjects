# solutions of questions that from OJ

# region 1251从键盘输入一个四位数整数，判断第2位和第3位之和是否为偶数，若是，输出yes，否则输出no。
# from math import floor
# number = int(input())
# digit1 = int(floor(number / 1000))
# digit2 = int(floor((number-digit1 * 1000) / 100))
# digit3 = int(floor((number - digit1 * 1000 - digit2 * 100) / 10))
# if((digit2 + digit3) % 2) == 0:
#     print('yes')
# else:
#     print('no')
# endregion

# region 1252从键盘输入一个4位数字，将前2位和后2位分别组成2个新数字，并判断这两个新数字是否相等，
# 相等则输出“equal”，否则输出“not equal”。例如：键盘输入1234，新数字为：12和34，输出结果为：not equal。
# number = int(input())
# front = int(number / 100)
# back = int(number % 100)
# if front == back:
#     print("equal")
# else:
#     print("not equal")
# endregion

# region 1253实现功能为调查某学生的体重情况，
# 体重60斤及以上为超重，体重40斤及以下为营养不良，体重在40-60斤之间的为正常，
# 学生的体重数据（要求为实数）由键盘输入，在屏幕上显示“overweight”、“normal”和“malnutrition”的信息.
# weight = float(input())
# if weight >= 60:
#     print("overweight")
# elif weight <= 40:
#     print("malnutrition")
# else:
#     print("normal")
# endregion

# region 1254从键盘输入一个正整数n，计算出大于n并且加上168后是一个完全平方数的最小数并输出。
# num = int(input())
# x = 14
# while num + 168 != x * x:
#     num += 1
# print(num)
# n = int(input())
# n = n + 1
# x = 14
# while x * x < n + 168:
#     x += 1
# while x * x > n + 168:
#     n += 1
# print(n)
# endregion

# region 1255读取一个大于1的正整数，然后显示它所有的最小因子，也称之为素因子（即将一个正整数分解质因数）。
# 例如：输入整数为90，输出90=2*3*3*5
from math import sqrt
"""
while 1:
    n = int(input('请输入整数：'))
    print("%d = " % n, end='')
    while 1:
        for i in range(2, int(sqrt(n)+1)):
            if n % i == 0:
                print('%d*' % i, end='')
                n = int(n/i)
                break
        else:
            print(n)
            break
"""

"""
while 1:
    n = int(input('请输入一个整数：'))
    print('%d=' % n, end='')
    while n > 1:
         for i in range(2, n + 1):
             if n % i == 0:
                 n = int(n / i)
                 if n == 1:
                     print('%d' % i, end='')
                 else:
                    print('%d*' % i, end='')
                 break
print()
"""

"""
n = int(input())    # 创建一个列表用来存放遍历出来的因数
lt = []             # 给n换个名字记录,便于打印时打印出用户输入的n
m = n
while n > 1:
    for i in range(2, n+1):
        if n % i == 0:
            # 记录下用最小因数分解后的n
            n = n//i  # 取整除 - 返回商的整数部分（向下取整）
            # 把i转换成str,存到列表,便于后面用join拼接字符串列表
            lt.append(str(i))
            # 找到一个最小的因数时,就跳出for in循环,开始下一次循环
            break
if len(lt) == 1:
    print(m, '=', '1*', m)
else:
    s = '*'.join(lt)
    print(m, '=', s)
"""
# for oj, choose next one
"""
from math import sqrt
list1 = []
n = input()
num = int(n)
for i in range(2, int(sqrt(num) + 1)):
    while 1:
        if num % i == 0:
            list1.append(i)
            num = num / i
        else:
            break
m = '*'.join([str(x) for x in list1])
print(n+'='+m,end="")
"""
# or
"""
def ll(n):
    for i in range(2, n, 1):
        if (n % i == 0):
            return False
    return True


a = eval(input())
print(a, "=", sep="", end="")
for i in range(2, a+1, 1):
    while(a % i == 0)and(ll(i)):
        if (a == i):
            print(i, sep="", end="")
            break
        else:
            print(i, "*", sep="", end="")
            a = a/i
"""
# endregion

# region 1256 从键盘输入整数n，输出数字方阵
"""
从键盘输入整数n，输出数字方阵。例如：输入n=5，输出如下：
1 2 3 4 5
2 3 4 5 1
3 4 5 1 2
4 5 1 2 3
5 1 2 3 4
"""
"""
n = int(input())
for j in range(1, n+1):
    for i in range(j, n+j):
        if i == n:
            print(n, sep='', end=" ")
        else:
            print((i % n), sep='', end=" ")
    print()    
"""
"""
def cover(a):
    i = 0
    temp = a[0]
    while i < len(a)-1:
         a[i] = a[i+1]
         i += 1
    a[i] = temp


def show(a):
    for m in range(len(a)-1):
        print(a[m], end=' ')
    print(a[m+1])
    
n = int(input())
a = list()
j = 1
while j <= n:
    a.append(j)
    j += 1
show(a)
j = 1
while j < n:
    cover(a)
    show(a)
    j += 1
"""
# endregion
