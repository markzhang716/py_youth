import pygame, os, sys
from pygame.locals import *
from snakeclass import *



pygame.init()
screen = pygame.display.set_mode((900,600))
bg = pygame.image.load('bg.jpg')
snake = Snake(screen)
clock = pygame.time.Clock()
KEY = None
SNAKEEVENT = USEREVENT + 1
pygame.time.set_timer(SNAKEEVENT, 300)
while True:
    clock.tick(20)
    screen.blit(bg,(0,0)) #先把背景贴覆盖上，删除原图
    for eventType in pygame.event.get():  # 进行事件等待
        # 如果用户点击了关闭窗口按钮，那么就执行退出
        if eventType.type == QUIT:
            sys.exit()
        elif eventType.type == KEYUP:
            KEY = eventType.key
        elif eventType.type == SNAKEEVENT:
            snake.move(KEY)
    snake.show()
    
    pygame.display.update()

