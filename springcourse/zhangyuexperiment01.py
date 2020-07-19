#region /与//
# print('Hello World')
# print(3/2)
# print(3//2)
# i=3
# print(i)
# t="python"
# print(t)
#endregion

#region 引号，字符串
# print('hello')
# # print("hello")
# # print(' ''hello'' ')
# # print(" ""hello"" ")
# # print('"hello"')
# # print("'hello'")
# # print('''hello
# # world''')
# # print("""hello
# # world""")
#endregion

#region turtle图形编程案例 太阳花
# import turtle
# turtle.color("red", "yellow")
# turtle.begin_fill()
# for i in range(50):
#     turtle.forward(200)
#     turtle.left(170)
# turtle.end_fill()
# turtle.done()
#endregion

#region 五角星
# import turtle
# turtle.pensize(5)
# turtle.pencolor("red")
# turtle.fillcolor("yellow")
# turtle.begin_fill()
# for i in range(5):
#     turtle.forward(180)
#     turtle.right(144)
# turtle.end_fill()
# turtle.done()
#endregion

#homework
print("""
学号：20181544
姓名：朱静如
班级：信计1801
""")

import turtle
turtle.screensize(900,900)
turtle.penup()
turtle.goto(-150,150)
turtle.pendown()
turtle.pensize(9)
turtle.pencolor("green")
turtle.fillcolor("yellow")
turtle.begin_fill()
for i in range(4):
    turtle.forward(300)
    turtle.right(90)
turtle.end_fill()
turtle.done()