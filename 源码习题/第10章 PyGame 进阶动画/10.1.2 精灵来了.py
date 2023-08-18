import pygame,os,sys
from pygame.locals import *
import random

FILE_PATH = os.path.join(os.path.dirname(__file__), 'files')
os.chdir(FILE_PATH)

class Raspberry(pygame.sprite.Sprite):
    '''
    蛇吃的树莓
    '''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        x = random.randint(0,900-30)
        y = random.randint(0,600-30)
        self.rect = Rect(x,y,30,30)
        self.image =pygame.image.load('snake_food.png')



pygame.init()
screen = pygame.display.set_mode((900,600))

screen.blit(pygame.image.load('bg.jpg'),(0,0))



group = pygame.sprite.Group()
for i in range(1,10):
    group.add(Raspberry())
group.draw(screen)
pygame.display.update()

while True:
    eventType = pygame.event.wait()  # 进行事件等待
    # 如果用户点击了关闭窗口按钮，那么就执行退出
    if eventType.type == QUIT:
        sys.exit()


