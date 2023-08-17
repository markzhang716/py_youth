#划出五角星
import turtle
turtle.color("#FF0000") #设置填充和线条的颜色都为红色
turtle.begin_fill() #下面的代码画出的形状要填充
for i in range(5):  #重复5次
    turtle.forward(100)   #向前画一条线长度100
    turtle.right(180-36)  #向右转体
turtle.end_fill() #填充颜色
turtle.done()
