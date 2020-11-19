def guessNumber():
    print("请您心里想一个整数，我们来一场猜数游戏！\n首先我们需要一个取值范围。")
    low = eval(input("请设置下限："))
    high = eval(input("请设置上限："))
    while True:
        mid = (low + high) // 2
        counts = 1
        print("您心里面的那个数字是", mid,"么？")
        judge = eval(input(
            "若我猜的数字和您心里面的相等请键0，若猜大了请键1，若猜小了请键-1\n"))
        if judge == 0:
            print("好巧，是猜对了呢！")
            return mid
            break
        elif judge == -1:
            low = mid
        else:
            high = mid
    return mid

def main():
    print("原来您心里面想的数字是", guessNumber() , "！")

main()










