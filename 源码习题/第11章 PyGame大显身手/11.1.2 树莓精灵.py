import pygame, os, sys
from pygame.locals import *
import random

FILE_PATH = os.path.join(os.path.dirname(__file__), 'files')
os.chdir(FILE_PATH)

class Raspberry(pygame.sprite.Sprite):
    '''
    蛇吃的树莓
    '''
    group = pygame.sprite.Group()
    #屏幕30X30网格的所有左上角坐标
    screenBlankGrid = [(x*30,y*30) for x in range(0,30) for y in range(0,20)]

    def __init__(self, snake_line=[]):
        pygame.sprite.Sprite.__init__(self)
        blank_grid = list(filter(lambda x :x not in snake_line, Raspberry.screenBlankGrid))
        xy = random.choice(blank_grid)
        Raspberry.screenBlankGrid.remove(xy) #占用
        self.rect = Rect(xy[0], xy[1], 30, 30)
        self.image =pygame.image.load('snake_food.png')
        Raspberry.group.add(self)

        
pygame.init()
screen = pygame.display.set_mode((900,600))
screen.blit(pygame.image.load('bg.jpg'),(0,0))
for i in range(1,10):
    Raspberry()
Raspberry.group.draw(screen)
pygame.display.update()
while True:
    EVENT = pygame.event.wait()  # 进行事件等待
    # 如果用户点击了关闭窗口按钮，那么就执行退出
    if EVENT.type == QUIT:
        sys.exit()

