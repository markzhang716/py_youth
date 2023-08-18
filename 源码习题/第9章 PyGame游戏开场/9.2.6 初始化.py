import sys,os,time
import pygame  # 导入pygame库
from pygame.locals import *  # 导入一些常用的函数和常量
#向sys模块借一个exit函数用来退出程序
from sys import exit
#初始化pygame,为使用硬件做准备
pygame.init()
#创建了一个窗口
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Joe的贪吃蛇游戏")  #设置窗口标题
pygame.display.update()

while True:
    eventType  = pygame.event.wait()  # 进行事件等待
    # 如果用户点击了关闭窗口按钮，那么就执行退出
    if eventType .type == QUIT:
        exit()