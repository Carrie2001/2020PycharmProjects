def guessNumber():
    found = 2
    high = 247483647
    low = -247483647
    ans = 0
    while 1:
        mid = (high+low) // 2
        print("您的数是这个么", mid,"?")
        found = eval(input(
            "如果和此数相等请输入0,大于此数请输入1，小于此数请输入-1\n"))
        if found == 0 or high == low:
            ans = mid
            if high == low:
                print("这个数是", ans, "!")
            break
        elif found == 1:
            low = mid
        else:
            high = mid
    print("这个数是",  ans)


def main():
    print("请确定一个数在 -2147483640 到 2147483642 之间！")
    guessNumber()


main()
