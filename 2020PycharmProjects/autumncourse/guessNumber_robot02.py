def guessNumber():
    print("请您心里想一个整数，我们来一场猜数游戏！\n首先我们需要一个取值范围。")
    n = eval(input("请设置下限："))

    while True:
        print("您猜的数是不是", n, "?")
        print("若您猜的数等于", n, "请输入0,不等于就随便输个不等于0的数:")
        choose = eval(input())
        if choose == 0:
            return n
            break
        n = n + 1
    return n

def main():
    print("原来您心里面想的数字是",guessNumber() , "！")

main()