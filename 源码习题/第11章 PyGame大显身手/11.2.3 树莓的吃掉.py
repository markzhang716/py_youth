import pygame, os, sys
from pygame.locals import *
from snakeclass import *

pygame.init()
screen = pygame.display.set_mode((900,600))
bg = pygame.image.load('bg.jpg')
snake = Snake(screen)
clock = pygame.time.Clock()
level = 1
KEY = None
SNAKEEVENT = USEREVENT + 1
pygame.time.set_timer(SNAKEEVENT, 300)
last_collide = None
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
    #当前碰撞的食物是什么
    rasp =  pygame.sprite.spritecollideany(snake, Raspberry.group)
    if rasp:
        if rasp != last_collide:
            level+=1
        else:
            rasp.image = pygame.transform.smoothscale(rasp.image,(int(rasp.rect.width-2),int(rasp.rect.height-2)))
            rasp.rect = rasp.rect.inflate(-2,-2)
        last_collide = rasp
    #当从碰撞中走出来时 或者 进入了一个新的碰撞时 就从组里删除被吃的树莓
    if (last_collide and rasp is None) or (last_collide and rasp and rasp != last_collide):
        last_collide.kill()

    while len(Raspberry.group.sprites())<level:
        Raspberry(snake.snakeLine)

    snake.show()
    Raspberry.group.draw(screen)
    pygame.display.update()

