import sys,os,time
import pygame  # 导入pygame库
from pygame.locals import *  # 导入一些常用的函数和常量
# 向sys模块借一个exit函数用来退出程序
from sys import exit
# 切换当前文件夹到files文件夹
FILE_PATH = os.path.join(os.path.dirname(__file__), 'files')
os.chdir(FILE_PATH)    
# 初始化pygame,为使用硬件做准备
pygame.init()
# 创建了一个窗口
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Joe的贪吃蛇游戏")  # 设置窗口标题
# 加载图像
background = pygame.image.load('snake_start.png')
# 开始不停地进行图像循环
screen.blit(background,[0,0])  # 把背景图画到0。0开始的坐标点上去
screen.fill(pygame.Color(0,0,0),Rect(0,560,900,40))

font = pygame.font.SysFont('songtittc',16)

pygame.display.update()  # 把图像显示出来
while True:
    for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
    time.sleep(0.05)
    screen.fill(pygame.Color(0,0,0),Rect(0,560,900,40)) #画出黑框
    if int(time.time())%2 ==0: #如果是偶数秒就画上文字
        screen.blit(font.render('按任意键继续......',1,Color(255,255,255)),[200,565])
    pygame.display.update()  # 把图像显示出来
