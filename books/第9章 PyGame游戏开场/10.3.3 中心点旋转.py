import pygame,os,sys
from pygame.locals import *
import random
FILE_PATH = os.path.join(os.path.dirname(__file__), 'files')
os.chdir(FILE_PATH)
#屏幕上图片会意外地不断跳动
pygame.init()
screen = pygame.display.set_mode((900,600))
bg = pygame.image.load('bg.jpg')
waiting = pygame.image.load('loading.png')
clock = pygame.time.Clock()
angle = 0
while True:
    clock.tick(20)
    angle += 10
    for eventType in pygame.event.get():  # 进行事件等待
        # 如果用户点击了关闭窗口按钮，那么就执行退出
        if eventType .type == QUIT:
            sys.exit()
    screen.blit(bg,(0,0)) #先把背景贴覆盖上，删除原图上的原图
    newloading = pygame.transform.rotate(waiting,-angle)
    #中心的点偏移，是长度的一半
    center_off_x = (newloading.get_width()-128)/2
    center_off_y = (newloading.get_height()-128)/2
    screen.blit(newloading,(400-center_off_x,200-center_off_y))
    pygame.display.update()


