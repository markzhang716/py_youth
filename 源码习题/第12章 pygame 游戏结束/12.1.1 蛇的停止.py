import pygame, os, sys
from pygame.locals import *
from snakeclass import *

pygame.init()
screen = pygame.display.set_mode((900,600))
bg = pygame.image.load('bg.jpg')
snake = Snake(screen)
clock = pygame.time.Clock()
level = 1
last_collide = None
KEY = None
SNAKEEVENT = USEREVENT + 1
pygame.time.set_timer(SNAKEEVENT, 300)
eaten = []
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
            snake.move(KEY) #移动蛇的位置

    snake.show() #绘制蛇
    #当前碰撞的食物是什么
    rasp =  pygame.sprite.spritecollideany(snake, Raspberry.group)
    if rasp:
        if rasp != last_collide: #碰撞对象不同，就升级
            level += 1
            eaten.append(rasp)
            snake.lengthening += 1
        else:
            #碰撞对象相同，说明还是同一个食物，那么就缩小2个像素
            rasp.image = pygame.transform.smoothscale(rasp.image,(int(rasp.rect.width-2),int(rasp.rect.height-2)))
            rasp.rect.inflate_ip(-2,-2)
        last_collide = rasp

    #当从碰撞中走出来时 或者 进入了一个新的碰撞时 就从组里删除被吃的树莓
    if last_collide and  rasp != last_collide and last_collide in Raspberry.group.sprites():
        print(len(snake.snakeLine))
        for one_eaten in eaten:
            one_eaten.kill()
        eaten = []

    #根据难度增长树莓数量
    while len(Raspberry.group.sprites())<int(level):
        Raspberry(snake.snakeLine)
    #绘制树莓
    Raspberry.group.draw(screen)
    pygame.display.update()



