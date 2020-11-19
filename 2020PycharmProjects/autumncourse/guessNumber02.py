def robot1():
    print("请从 m 到 n 选择一个数，我会猜出这个数。")
    m = eval(input("请确定m的值："))
    n = eval(input("请确定n的值："))
    r = (n + m) // 2

    while 1:
        print("你猜的数是不是", r, "?")
        print("如果你猜的数大于", r, "请输入1，小于请输入-1，等于请输入0:")
        choose = eval(input())
        if choose == 0:
            return r
            break
        elif choose == -1:
            n = r
            r = (m + r) // 2

        elif choose == 1:
            m = r
            r = (n + r) // 2

        else:
            print("请认真输入！")

result = robot1()
print("你猜的数是",result)
