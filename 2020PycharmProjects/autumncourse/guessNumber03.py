def robot2():
    print("请从 m 到 n 选择一个数，我会猜出这个数。")
    m = eval(input("请确定m的值："))
    n = eval(input("请确定n的值："))
    while 1:
        print("你猜的数是不是",m,"?")
        print("如果你猜的数等于", m, "请输入0,不等于就随便输个不等于0的数:")
        choose = eval(input())
        if choose == 0:
            return m
            break
        m=m+1

result = robot2()
print("你猜的数是", result)
