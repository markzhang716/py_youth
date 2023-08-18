import pygame, os, sys,string
from pygame.locals import *
from snakeclass import *


def show_top10_demo(screen,score):
    old_screen = screen.copy()
    top10_bg = pygame.Surface((900,600),SRCALPHA)
    top10_bg.fill(Color(0,0,0,50),None)
    font = pygame.font.Font(None,48)

    top10_bg.blit(font.render('TOP 10 HEROS',1,Color(255,255,255)),(300,20))
    for (i,textLine) in enumerate(high_score(screen,score)):
        top10_bg.blit(font.render('%-2d.'%(i+1) +  textLine[0],1,Color(255,255,255)),(180,120 + i*40))
        top10_bg.blit(font.render(str(textLine[1]),1,Color(255,255,255)),(710,120 + i*40))
        
    y=600
    clock = pygame.time.Clock()
    while True:
        clock.tick(30)
        for eventType in pygame.event.get():
            if eventType.type == QUIT:
                sys.exit()
            if eventType.type == KEYUP and y<=0:
                return
        screen.blit(top10_bg,(0,y))
        pygame.display.update()
        y-=20
        if y<=0:
            y=0



if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((900,600))
    bg = pygame.image.load('bg.jpg')
    screen.blit(bg,(0,0)) #先把背景贴覆盖上，删除原图
    show_top10(screen,100)