import random

def guess():
    count=1
    realNumber = random.randint(1, 200)
    while True:
        guessNumber = int(input("请输入："))
        if guessNumber<realNumber:
            count+=1
            print("太小了！")
        elif guessNumber>realNumber:
            print("太大了！")
            count += 1
        else:
            print("你猜对了噢！一共猜了",count,"次！")
            break

#二分查找
def binary_search(list,item):
    low = 0
    high = len(list)-1
    while low <= high:
      mid = int((low + high)/2)
      guess = list[mid]
      if guess > item:
          high = mid -1
      elif guess < item:
          low = mid + 1
      else:
          return mid
    return None


if __name__=="__main__":
     #guess()
     list=[1,2,3,4,5,6,7,8,9,10]
     print(binary_search(list,7))


# import random
# # （0，1000）随机产生一个数
# key = random.randint(1,1000)
# # 用来统计猜的次数
# count = 0
#
# # 定义一个折半查找的函数
# def BinSearch(array, key, low, high):
#     global count
#     mid = int((low+high)/2)
#     if key == array[mid]:  # 若找到
#         count += 1
#         print("您总共猜了次数是：%d"%count)
#         print("恭喜您猜对了，答案是：" )
#         return array[mid]
#     if low > high:
#         return False
#
#     if key < array[mid]:
#         print("小于猜的数")
#         count += 1
#         return BinSearch(array, key, low, mid-1)  #递归
#     if key > array[mid]:
#         count += 1
#         print("大于猜的数")
#         return BinSearch(array, key, mid+1, high)
#
#
#
# if __name__ == "__main__":
#     # 给定一个列表
#     num_value_list = list(range(1, 1001))
#     # 通过折半查找，找到随机的数
#     ret = BinSearch(num_value_list, key, 0, len(num_value_list)-1)
#     print(ret)