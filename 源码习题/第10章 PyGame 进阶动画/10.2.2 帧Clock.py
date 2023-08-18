import pygame,os,time
from pygame.locals import *
import random

pygame.init()
clock = pygame.time.Clock()
startSecond = time.time()
otherCodesRunningSpan = 0
while time.time()<=startSecond +2:
    clock.tick(10)
    print('-'*10)
    print('get_time()',clock.get_time())
    print('模拟绘图耗时',otherCodesRunningSpan)
    print('get_rawtime()',clock.get_rawtime())

    otherCodesRunningSpan = random.randint(50,150)
    time.sleep(otherCodesRunningSpan/1000)
