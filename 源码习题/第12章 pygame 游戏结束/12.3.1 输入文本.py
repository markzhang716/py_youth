import pygame, os, sys,string
from pygame.locals import *
from snakeclass import *


def input_name_demo(screen):
    '''
    用来接受用户的输入，并且以字符串返回结果
    '''
    #创建文本输入对象
    textinput = pygame_textinput.TextInput()
    textinput.font_size = 30
    textinput.text_color = Color(255,0,0)
    textinput.cursor_color = Color(255,0,0)
    clock = pygame.time.Clock()
    font = pygame.font.Font(None,40)
    old_screen = screen.copy()
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
        # 第一帧都要更新这个组件，如果输入回车就为True
        if textinput.update(events):
            return textinput.get_text()
        screen.blit(old_screen,(0,0))
        # 把输入的文字显示在屏幕上
        screen.blit(font.render('Congratulations, you are one of Top 10!',1,Color(255,0,0)),(170,10))
        screen.blit(font.render('Input your name: ',1,Color(255,0,0)),(200,50))

        screen.blit(textinput.get_surface(), (450, 50))
        pygame.display.update()
        clock.tick(30)

#以下用来测试以上语句的代码
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((900,600))
    bg = pygame.image.load('bg.jpg')
    screen.blit(bg,(0,0)) #先把背景贴覆盖上，删除原图
    food_score,time_score = 10,20
    font = pygame.font.Font(None,30)

    show_end(screen,30,51)
    print(input_name_demo(screen))
