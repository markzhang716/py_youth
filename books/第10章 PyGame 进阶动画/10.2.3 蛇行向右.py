import pygame,os,sys
from pygame.locals import *
import random
FILE_PATH = os.path.join(os.path.dirname(__file__), 'files')
os.chdir(FILE_PATH)
class Snake(pygame.sprite.Sprite):
    snakeHead = pygame.image.load('snake_head.png') #头
    snakeBody = pygame.image.load('snake_body_h.png') #身
    snakeTail = pygame.image.load('snake_tail.png') #尾
    def __init__(self,screen):
        pygame.sprite.Sprite.__init__(self)
        #表示组成蛇每一个图片的左上角坐标，初始就是3张图片，从蛇头开始
        self.snakeLine = [(400,300),(400-30,300),(400-60,300)]
        self.screen = screen #传入屏幕
        self.rect = Rect(400,300,30,30) #蛇头的区域
    #根据新的蛇头的坐标来画出蛇的
    def show(self,newSnakeLine = None):
        if newSnakeLine is not None:
            self.snakeLine = newSnakeLine #把新的位置设置成当前位置
            self.rect = Rect(newSnakeLine[0],(30,30))
        #画出头
        self.screen.blit(Snake.snakeHead,self.snakeLine[0])
        self.rect = Rect(self.snakeLine[0],(30,30))
        #画出直线的身体
        for cord in self.snakeLine[1:-1]:
            self.screen.blit(Snake.snakeBody,cord)
        #画出蛇尾
        self.screen.blit(Snake.snakeTail,self.snakeLine[-1])
    def right(self):
        self.snakeLine = [((self.snakeLine[0][0]+30)%900,self.snakeLine[0][1])] + self.snakeLine[0:-1]
        self.show()

pygame.init()
screen = pygame.display.set_mode((900,600))
bg = pygame.image.load('bg.jpg')
snake = Snake(screen)
clock = pygame.time.Clock()
while True:
    clock.tick(8)
    for eventType in pygame.event.get():  # 进行事件等待
        # 如果用户点击了关闭窗口按钮，那么就执行退出
        if eventType .type == QUIT:
            sys.exit()
    screen.blit(bg,(0,0)) #先把背景贴覆盖上，删除原图上的小蛇
    snake.right()
    pygame.display.update()

