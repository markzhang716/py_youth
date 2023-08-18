import pygame,os,sys
from pygame.locals import *
import random

FILE_PATH = os.path.join(os.path.dirname(__file__), 'files')
os.chdir(FILE_PATH)

class Raspberry(pygame.sprite.Sprite):
    '''
    蛇吃的树莓
    '''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        x = random.randint(0,900-30)
        y = random.randint(0,600-30)
        self.rect = Rect(x,y,30,30)
        self.image =pygame.image.load('snake_food.png')



pygame.init()
screen = pygame.display.set_mode((900,600))

screen.blit(pygame.image.load('bg.jpg'),(0,0))



group = pygame.sprite.Group()
for i in range(1,10):
    group.add(Raspberry())
group.draw(screen)
pygame.display.update()

while True:
    eventType = pygame.event.wait()  # 进行事件等待
    # 如果用户点击了关闭窗口按钮，那么就执行退出
    if eventType .type == QUIT:
        sys.exit()




class Snake(pygame.sprite.Sprite):
    snakeHead = pygame.image.load('snake_head.png')
    snakeBody = pygame.image.load('snake_body_h.png')
    snakeTurn = pygame.image.load('snake_turn.png')
    snakeTail = pygame.image.load('snake_tail.png')
    def __init__(self,screen):
        #表示组成蛇每一个图片的左上角坐标，初始就是3张图片，从蛇头开始
        self.snakeLine = [(400,300),(400-30,300),(400-60,300)]
        self.screen = screen #传入屏幕
    #根据新的蛇头的坐标来画出蛇的
    def show(self,newSnakeLine = None):
        #如果新的位置设定了，就把原来的形象擦除
        if newSnakeLine is not None:
            self.snakeLine = newSnakeLine #把新的位置设置成当前位置
        #画出头
        self.screen.blit(Snake.snakeHead,self.snakeLine[0])
        #画出直线的身体
        for cord in self.snakeLine[1:-1]:
            self.screen.blit(Snake.snakeBody,cord)
        #画出蛇尾
        self.screen.blit(Snake.snakeTail,self.snakeLine[-1])



pygame.init()
screen = pygame.display.set_mode((900,600))

screen.blit(pygame.image.load(os.path.join(
        os.path.abspath(os.path.dirname(sys.argv[0])), 'images', 'bg.jpg')),(0,0))

snake = Snake(screen)
snake.show([(500,200),(500-30,200),(500-60,200),(500-90,200),(500-120,200)])


group = pygame.sprite.Group()
for i in range(1,10):
    group.add(Raspberry())
group.draw(screen)

while True:
    eventType = pygame.event.wait()  # 进行事件等待
    # 如果用户点击了关闭窗口按钮，那么就执行退出
    if eventType .type == QUIT:
        sys.exit()
    elif eventType.type == KEYDOWN:
    # 如果用户点击了，那么就执行退出
        screen.blit(pygame.image.load(os.path.join(
            os.path.abspath(os.path.dirname(sys.argv[0])), 'images', 'bg.jpg')),(0,0))
        if eventType.key == K_UP:
            snake.show(list(map(lambda x:(x[0],x[1]-30),snake.snakeLine)))
        elif eventType.key == K_DOWN:
            snake.show(list(map(lambda x:(x[0],x[1]+30),snake.snakeLine)))
        elif eventType.key == K_LEFT:
            snake.show(list(map(lambda x:(x[0]-30,x[1]),snake.snakeLine)))
        elif eventType.key == K_RIGHT:
            snake.show(list(map(lambda x:(x[0]+30,x[1]),snake.snakeLine)))
        elif eventType.key == K_SPACE:
            snake.show(snake.snakeLine + [(snake.snakeLine[-1][0]-30,snake.snakeLine[-1][1])])
        elif eventType.key  == K_ESCAPE:
            break
    pygame.display.update()
