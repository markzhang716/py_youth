import pygame
from snakeclass import *

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((900,600))
show_start(screen)
pygame.mixer.music.load('sound_snake_play.mp3') 
pygame.mixer.music.play(loops=-1) #循环播放
food_score,time_score = main_loop(screen)
show_end(screen,food_score,time_score)
show_top10(screen,food_score+time_score)


