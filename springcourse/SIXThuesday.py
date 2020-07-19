"""
range(start, stop[, step])
参数说明：
start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
"""""
"""
关系运算的结果是bool类型，True,False
if 的后面什么都可以，只要不是空的，为零的都是为真的
python的短路and和or，第一个为F则and为F，第一个为T则or为T
2 and 3
Out[2]: 3
3 or 2
Out[3]: 3
"""
"""
条件表达式的写法
一个简单的双分支操作
x = 1 if 2 > 1 else 2 : 如果2>1成立则x=1，否则x=2
是把1 if 2 > 1 else 2的结果给了x
x = a if a < b else b
"""
"""
pyhton 只有while和for
for：遍历一个数
range： 本身据的集合就是一个对象，一个数据序列、集合
range（10）：0,1,2,3,4,5,6,7,8,9
"""
"""
pass：直接跳过
"""
"""
for else
while else
"""
"""
for i in range(2, 100):
    k = True
    for j in range(2, i):
        if i % j == 0:
            k = False
            break
        if k:
            print(i)
"""
"""
for i in range(2, 100):
    for j in range(2, i):
        if i % j == 0:
           break
    else:                         # for结束之后就会运行这个else
            print(i)              # 区分是否是break停止
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
