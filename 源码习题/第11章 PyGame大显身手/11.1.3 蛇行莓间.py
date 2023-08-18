import pygame, os, sys
from pygame.locals import *
from snakeclass import *

pygame.init()
screen = pygame.display.set_mode((900,600))
bg = pygame.image.load('bg.jpg')
snake = Snake(screen)
clock = pygame.time.Clock()
level = 10
while True:
    clock.tick(4)
    KEY = None
    for eventType in pygame.event.get():  # 进行事件等待
        # 如果用户点击了关闭窗口按钮，那么就执行退出
        if eventType.type == QUIT:
            sys.exit()
        elif eventType.type == KEYUP:
            KEY = eventType.key
    screen.blit(bg,(0,0)) #先把背景贴覆盖上，删除原图上的小蛇
    snake.move(KEY)
    snake.show()
    if len(Raspberry.group.sprites())<level:
        Raspberry(snake.snakeLine)
    Raspberry.group.draw(screen)
    pygame.display.update()

