# solutions of questions that from OJ

# region 1246直接执行
# city=input('Please enter the name of a city:')
# print('Welcome to',city+'!')
# endregion

# region 1246写个函数
# def city_welcome(city_name):
#     print('Welcome to',city_name+'!')
# city_welcome(input('Please enter the name of a city:'))
# endregion

# region 1247计算矩形面积
# length = int(input( ))
# width = int(input ( ))
# print(length * width )
# endregion

# region 1248从键盘输入一个整数，输出它的符号（+或-，输入为0的话输出+，注意不要有多余的输入和输出）
# a = int(input())
# if a >= 0:
#     print("+\n")
# else:
#     print("-\n")
# endregion

# region 1249从键盘上输入3个数，输出它们的和与平均数。
# 注意：输入时不需要任何提示语句，每输入一个数值按回车键，
# 接着输入下一个数值，输出不要任何提示，
# 直接先输出和，再输出平均数，均保留2位小数，分行显示。
# num1 = float(input())
# num2 = float(input())
# num3 = float(input())
# s = sum([num1, num2, num3])
# print("{:.2f}".format(s))
# print("{:.2f}".format(s/3))
# endregion

# region 1249写个函数
print("-----求平均值，可输入任意多个数-------")
lst = []                                    # 定义一个空列表
str_of_num = input("请输入数值，用空格隔开:")
lst1 = str_of_num.split(" ")                # lst1用来存储输入的字符串，用空格分割
i = 0
while i <= len(lst1) + 1:
 lst.append(float(lst1.pop()))              # 将lst1的数据转换为整型并赋值给lst
 i += 1
print(lst)


def sum_list(list):
 "对列表的数值求和"
 s = 0
 for x in list:  s = s + x
 return s


print("s = %f"%sum_list(lst))


def average(list):
 "对列表数据求平均值"
 avg = 0
 avg = sum_list(list)/(len(list)*1.0)
 return avg


# 调用average函数求平均数
print("avg = %f"%average(lst))
# endregion

# region 1250输入三角形的三条边的值，输出它的面积，要求面积值保留小数点后2位。
# 注意：输入时不需要任何提示语句，每输入一个数值按回车键，接着输入下一个数值，
# 输出不要任何提示，本题暂时不考虑输入的三条边不能组成三角形的情况。
# num1 = float(input())
# num2 = float(input())
# num3 = float(input())
# num = (num1 + num2 + num3)/2
# s = (num * (num - num1) * (num - num2) * (num - num3)) ** 0.5
# print("{:.2f}".format(s))
# endregion



