import turtle
#任意多角形的
turtle.color("#c2002a","#f0ae00") #设置填充暗黄色和线条暗红色
turtle.width(3)
turtle.begin_fill() #下面的代码画出的形状要填充
N=int(turtle.numinput("输入","请输入多角星的 N="))  #输入函数默认是float类型，要转换成整数
for i in range(N):  #重复5次
    turtle.forward(100)   #向前画一条线长度100
    turtle.right(180-180/N)  #向右转体
turtle.end_fill() #填充颜色
turtle.done()
