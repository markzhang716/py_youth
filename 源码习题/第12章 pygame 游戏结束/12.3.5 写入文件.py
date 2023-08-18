import pygame, os, sys,string
from pygame.locals import *
from snakeclass import *


def high_score_demo(screen, score):
    open('snake_top10.txt','a').close()
    file = open('snake_top10.txt','r+')
    top10 =[]
    for line in file.readlines():
        top10.append((line[0:20],int(line[20:])))
    #如果分数比最后一名高
    if score>= top10[-1][1] or len(top10)<10:
        top10.insert(0,(('%-20s'%input_name(screen))[0:20], score))
        top10.sort(key = lambda x:x[1],reverse=True)
    if len(top10)>10:
        top10 = top10[0:10]
    file.seek(0)
    stringContent = '\n'.join([ '%2d.'% (i+1) +  x[0]+str(x[1]) for (i,x) in enumerate(top10)])
    fileContent = '\n'.join([ x[0]+str(x[1]) for x in top10])
    file.write(fileContent)
    file.close()
    return stringContent


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((900,600))
    bg = pygame.image.load('bg.jpg')
    screen.blit(bg,(0,0)) #先把背景贴覆盖上，删除原图
    food_score,time_score = 10,20
    font = pygame.font.Font(None,30)

    show_end(screen,30,61)
    print(high_score_demo(screen,91))