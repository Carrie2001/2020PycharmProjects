"""
 三门问题 两只羊和一辆劳斯莱斯
"""""
# choice(seq): 从seq序列中（可以是列表，元组，字符串）随机取一个元素返回
from random import choice

def stay():
    doors = ['car','goat','goat']
    choose = choice(doors)
    if choose == 'car':
        return 'win'
    else:
        return 'lose'

def switch():
    doors = ['car', 'goat', 'goat']
    choose = choice(doors)
    # list.remove(obj)移除列表中的一个对象
    doors.remove(choose) #移除了已经选择的
    doors.remove('goat') #移除剩下门里面的羊
    # 换门 从原来的choose 换成剩下的这个doors
    if doors == ['car']:
        return 'win'
    else:
        return 'lose'

total = 100000
count_switch = 0
win_switch = 0
count_stay = 0
win_stay = 0
for i in range(total):
    choose = choice([1,2]) # 随机返回列表[1,2]中的一个数字
    if choose == 1:
        # 随机数为1就换门
        count_switch += 1
        if switch() == 'win':
            win_switch += 1
    else:
        # 不换门
        count_stay += 1
        if stay() == 'win':
            win_stay += 1

print('the times of switch doors:',count_switch)
print('win after switching:',win_switch,'%.2f%%'%(100*win_switch/count_switch))
print('the times of not switch:',count_stay)
print('not switch but win:',win_stay,'%.2f%%'%(100*win_stay/count_stay))

