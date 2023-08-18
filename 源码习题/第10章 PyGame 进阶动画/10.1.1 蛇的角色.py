import pygame,os,sys
from pygame.locals import *

#得到images文件夹的绝对路径
FILE_PATH = os.path.join(os.path.dirname(__file__), 'files')
#把当前的工作路径改成images文件夹
os.chdir(FILE_PATH)


pygame.init()
screen = pygame.display.set_mode((900,600))
screen.fill(Color(0xc5,0xd5,0xc5))

head_x =400
head_y =300

snakeHead = pygame.image.load('snake_head.png')
snakeBody = pygame.image.load('snake_body_h.png')
snakeTail = pygame.image.load('snake_tail.png')

screen.blit(snakeHead,[head_x,head_y])
screen.blit(snakeBody,[head_x-30,head_y])
screen.blit(snakeTail,[head_x-60,head_y])



pygame.display.update()
while True:
    eventType  = pygame.event.wait()  # 进行事件等待
    # 如果用户点击了关闭窗口按钮，那么就执行退出
    if eventType .type == QUIT:
        sys.exit()
    # 如果用户点击了，那么就执行退出
    #elif eventType .type == KEYUP:  
        break
