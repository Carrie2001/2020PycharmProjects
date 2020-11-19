"""
列表可以存各种类型数据元素，但是用到这些比较函数还是只针对同一类之间的，将列表当做数组
l1.sort()   //l1change
l2=sorted(l1)   //l1no change
l1.append(10)   //l1change
l1.extend(20)   //l1change
l3=['zhang','li','wang']
l3.sort()   //['li', 'wang', 'zhang']

列表的切片访问，非常灵活
l1=[3,4,1,2,5,10,20]
len(l1)=7
l1[0]=3
l1[6]=20
l1[-1]=20
l1[7]   //类似于数组越界
切片访问
提取子列表
l1[2:5]=[1,2,5]
l1[2:]=[1,2,5,10,20]   //：后面省略的就是7
l1[2:7]=[1,2,5,10,20]
l1[2:8]=[1,2,5,10,20]//就算超过7也不会出现越界问题
对切片直接进行重新赋值
l1[6:]=[]
l1=[3,4,1,2,5,10]
l1[5]=[]
l1=[3,4,1,2,5,[]]   //元素覆盖,单个访问元素和切片访问差别很大
"""""
"""
可迭代对象：range，列表，字符串
包含迭代方法_iter_的对象就是可迭代对象
for i in range(10):
print(i)
for i in l1:
print(i)
for i in 'abcd':
print(i)

__iter__方法返回的是迭代器
迭代器会包含一个next方法
(have l1=[3,4,1,2,5,[]])
i1=l1.__iter__()
type(l1)
Out[13]: list
type(i1)
Out[14]: list_iterator
i1.__next__()
Out[15]: 3
i1.__next__()
Out[16]: 4
i1.__next__()
Out[17]: 1
i1.__next__()
Out[18]: 2
i1.__next__()
Out[19]: 5
i1.__next__()
Out[20]: []

可迭代对象先执行__iter__方法，把自己变成一个迭代器，而for就是不停的调用迭代器的__next__方法
python的for循环是很严厉的遍历对象，不可更改
r=range(5)
type(r)
Out[24]: range
i=r.__iter__()
i
Out[26]: <range_iterator at 0x1bcc67d6590>
i.__next__()
Out[27]: 0
i.__next__()
Out[28]: 1
i.__next__()
Out[29]: 2
i.__next__()
Out[30]: 3
i.__next__()
Out[31]: 4
i.__next__()
函数的生成器
"""
"""
列表推导式（可以避免写for）
L = list(range(5))
for i in range(len(L)):
    L[i] += 10   //[10,11,12,13,14]
L = [x + 10 for x in L]   // L=[20,21,22,23,24]列表推导式比上面的for快了1倍
"""
"""
L = list(range(5))
for i in range(len(L)):
    L[i] += 10
L = [x + 10 for x in L]   # L=[20,21,22,23,24]
L=[x + 10 for x in L if x % 2 == 0]   # [20,22,24]
[x+y for x in 'ab' for y in 'cde']   # ac ad ae bc bd be
for x in 'ab':
    for y in 'cde':
        L.append(x+y)
"""
"""
列表写矩阵
L=[[1,2,3],[4,5,6],[7,8,9]]   #此时len(L)=3
L[0]   # 1,2,3
L[1]   # 4,5,6
L[2]   # 7,8,9
[x[1] for x in L]   # 取出第二列
[L[i][i] for i in range(len(L))]   # 取出主对角线
"""


