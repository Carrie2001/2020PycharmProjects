def guessNumber():
    ans = 0
    bigger = eval(
        input("If the number equal to 0 ? input 1 if equal, higher than 0 input 1 , lower than 0 input -1 \n"))
    plus = 1
    if bigger == 0:
        return ans
    elif bigger == -1:
        plus = -1
    while 1:
        ans += plus
        found = eval(input("If the number equal to "+str(ans) +
                           "? input 1 if equal, else input 0\n"))
        if found == 1:
            return ans
    return ans


def main():
    print("Think a number in your mind")
    ans = guessNumber()
    print("The number you think is", ans)


main()
