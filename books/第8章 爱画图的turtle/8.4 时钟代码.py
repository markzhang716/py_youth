from turtle import *
from time import *
#这是绘制指针的函数
def drawPointers():
    tracer(False) #关闭慢动作
    hour_pointer.reset() #重置时针
    min_pointer.reset() #重置分针
    sec_pointer.reset() #重置秒针
    h=localtime().tm_hour  #几点了
    m=localtime().tm_min   #几分了
    hour_deg = -360/(12*60)*(60*h+m)+90  #时针转动的度数（以海龟坐标系统）
    hour_pointer.width(8) #把时针宽度设置为8
    hour_pointer.color("white") #把时针设置成白色
    hour_pointer.seth(hour_deg) #转动度数
    hour_pointer.fd(60) #画出时针
    hour_pointer.hideturtle() #隐藏海龟的标识（时针较粗有这个不好看）
    min_deg = -6*m+90  #分针转动的度数（以海龟坐标系统）
    min_pointer.width(4) #把分针宽度设置为4
    min_pointer.color("white") #把分针设置成白色
    min_pointer.seth(min_deg) #转动度数
    min_pointer.fd(110) #画出分针
    s = localtime().tm_sec #几秒
    sec_deg = -6*s+90  #秒针转动的度数（以海龟坐标系统）
    sec_pointer.width(2) #把秒针宽度设置为2
    sec_pointer.color("white") #把秒针设置成白色
    sec_pointer.seth(sec_deg) #转动度数
    sec_pointer.fd(140) #画出秒针
    tracer(True)
    ontimer(drawPointers,500)
#这是主程序
hour_pointer = Turtle() #使用一个新的时针 
min_pointer = Turtle() #使用一个新的分针
sec_pointer = Turtle() #使用一个新的秒针 
color('#ffa500','#ffbb00') #框是深黄面是浅黄色
goto(0,-150) #把画笔向下移动1个半径的圆
#绘制表盘
begin_fill() #需要填充
width(30) #边框30宽
circle(150) #圆的半径为150
end_fill() #填充
#文字12，3，6，9点
color('#FFF') #文字使用白色
pu() #提笔不画线只写字
#表盘文字
for hour in [12,3,6,9]:
    home() #回到原点
    goto(0,-9) #为了保持18大小的字在中间垂直，先把笔下沉一半高度（因为字是在笔正上方打印的）
    seth(-hour*30+90) #向不同小时方向前进，
    fd(148) #前进到表框边缘写时间的文字
    write(str(hour),False,'center',('Arial',18,'normal'))  #写小时文字
hideturtle() #隐藏海龟的标识
drawPointers()
done()
