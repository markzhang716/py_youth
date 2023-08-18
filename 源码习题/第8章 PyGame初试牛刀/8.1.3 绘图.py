import sys,os
import pygame
#导入pygame库
from pygame.locals import *
#导入一些常用的函数和常量
from sys import exit
#向sys模块借一个exit函数用来退出程序

#指定图像文件名称
background_image_filename =  os.path.dirname(sys.argv[0]) + '/images/snake_start.png'

print(background_image_filename)

pygame.init()
#初始化pygame,为使用硬件做准备
 
screen = pygame.display.set_mode((800, 600), 0, 32)
#创建了一个窗口
pygame.display.set_caption("Hello, World!")
#设置窗口标题
 
background = pygame.image.load(background_image_filename).convert()
#加载并转换图像

event_text = []

while True:
    event = pygame.event.wait()
    event_text.append(str(event))
    #获得时间的名称
    event_text = event_text[-SCREEN_SIZE[1]/font_height:]
    #这个切片操作保证了event_text里面只保留一个屏幕的文字
 
    if event.type == QUIT:
        exit()

    screen.blit(background, (0,0))
    pygame.display.update()
