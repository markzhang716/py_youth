import turtle

#画出半圆
'''
turtle.forward(100)
turtle.left(90)
turtle.circle(50,180)
'''

#写出生日祝福
#input()
turtle.reset()
turtle.pu()  #不用画线了
turtle.pencolor("black") #颜色设置成黑色
turtle.write("爸爸：",True,font=('黑体',14,'normal')) #显示爸爸黑体14号字
turtle.right(90)  #右转，使方向向下
turtle.forward(30) #向下移动30
turtle.pencolor("green") #绿色
turtle.write("生",True,font=('黑体',14,'normal'))
turtle.pencolor("red") #红色
turtle.write("日",True,font=('黑体',14,'normal'))
turtle.pencolor("orange") #橙色
turtle.write("快",True,font=('黑体',14,'normal'))
turtle.pencolor("brown") #棕色
turtle.write("乐",True,font=('黑体',14,'normal'))
turtle.forward(30)  #再向下移动30
turtle.pencolor("black")
turtle.write("大头儿子",True,font=('黑体',14,'normal'))
turtle.done()
