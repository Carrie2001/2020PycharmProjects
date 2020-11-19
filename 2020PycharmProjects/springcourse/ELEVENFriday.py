"""
函数式编程
"""""
"""
匿名函数lambda+内建函数=更加强大
"""
"""
内建函数
filter函数filter(func,seq)（一种遍历）
第一个参数传入一个返回布尔值的函数
第二个参数传入一个需要过滤的序列
返回一个filter对象，需要通过list内置函数转换成为列表
list(filter(func,seq))
list(filter(str.isalnum,seq))
e.g.
seq = ['123','hello','.?','567abc']
list(filter(str.isdigit,seq))
Out[5]: ['123']
data = list(range(20))
data
Out[7]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
filterobj = filter(lambda x:x%2 == 1,data)
filterobj
Out[9]: <filter at 0x2895dfbb128>
5 in filterobj
Out[10]: True
list(filterobj)
Out[11]: [7, 9, 11, 13, 15, 17, 19]
"""
"""
比较常用的一种内置函数
map函数map(f,x)(一种遍历)
第一个参数是需要转换成的函数
第二个参数是传入一个需要的序列
返回结果需要用list转换为列表
def add5(v):
    return v + 5
list(map(add5,range(10)))
Out[14]: [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
def add(x,y):
    return x + y
list(map(add,range(5),range(6,11)))
Out[16]: [6, 8, 10, 12, 14]
x=['aab','bc','d']
x
Out[18]: ['aab', 'bc', 'd']
list(map(str.upper,x))
Out[19]: ['AAB', 'BC', 'D']
sum(map(int,'1234'))
Out[20]: 10
map(int,'1234')
Out[21]: <map at 0x2895dfadef0>
x
Out[22]: ['aab', 'bc', 'd']
''.join(map(lambda i:i[0],x))
Out[23]: 'abd'
"""
"""
zip函数
将多个可迭代对象中的元素压缩在一起，返回一个可迭代的zip对象(被压缩对象中长度不同那么返回的zip对象的长度由最短的那个决定)
list(zip('abcd',[1,2,3]))
Out[24]: [('a', 1), ('b', 2), ('c', 3)]
list(zip('abcd','1234',',?/'))
Out[25]: [('a', '1', ','), ('b', '2', '?'), ('c', '3', '/')]
"""
"""
reduce函数reduce(func(1,2,,,),seq)不是内置函数
讲一个接受2个以上的函数一迭代的方式从左到右依次作用到一个序列上或者是迭代器对象的所有元素上
from functools import reduce
seq=[1,2,3,4,5,6,7,8,9]
reduce(lambda x,y:x+y,seq)   #1+2=3+3=6+4=10+5=15+6=21+7=28+8=36+9=45
Out[28]: 45
def add(x,y):
    return x+y
reduce(add,range(5))
Out[30]: 10
reduce(add,map(str,range(10)))
Out[31]: '0123456789'
"""
"""
==>KISS=keep it simple and stupid
简单胜于复杂
"""
