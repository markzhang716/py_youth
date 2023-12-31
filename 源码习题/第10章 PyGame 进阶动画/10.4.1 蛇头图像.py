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
    #根据新的蛇的坐标来画出蛇的
    def show(self,newSnakeLine = None):
        if newSnakeLine is not None:
            self.snakeLine = newSnakeLine #把新的位置设置成当前位置
            self.rect = Rect(newSnakeLine[0],(30,30))
        #画出头
        degrees = {K_UP:90,K_DOWN:-90,K_LEFT:180,K_RIGHT:0} #不同方向对应旋转不同角度
        degree  =  degrees[self.getDirection()]
        self.screen.blit(pygame.transform.rotate(Snake.snakeHead,degree),self.snakeLine[0])
        self.rect = Rect(self.snakeLine[0],(30,30))
        #画出直线的身体
        for inx in range(1,len(self.snakeLine)-1):
            self.screen.blit(Snake.snakeBody,self.snakeLine[inx])
        #画出蛇尾
        self.screen.blit(Snake.snakeTail,self.snakeLine[-1])
    
    def getBodyImage(self,index):
        snakeBody = pygame.image.load('snake_body_h.png') #身
        snakeTurn = pygame.image.load('snake_turn.png') #身

        if self.snakeLine[index-1][0] == self.snakeLine[index+1][0]:
            #x坐标相同就是垂直身体
            return pygame.transform.rotate(snakeBody,90)
        elif self.snakeLine[index-1][1] == self.snakeLine[index+1][1]:
            #y坐标相同就是水平的身体
            return snakeBody
        else:
            #是否x,y坐标同时大于另一块
            slope = (self.snakeLine[index-1][0]  - self.snakeLine[index+1][0])/(self.snakeLine[index-1][1] - self.snakeLine[index+1][1])
            #是否存在一块x坐标大于中间块
            right =  max(self.snakeLine[index-1][0],self.snakeLine[index+1][0]) > self.snakeLine[index][0]
            if slope>0 and right:
                return pygame.transform.rotate(snakeTurn,180)
            elif slope>0 and not right:
                return snakeTurn
            elif slope<0 and right:
                return pygame.transform.rotate(snakeTurn,90)
            elif slope<0 and not right:
                return pygame.transform.rotate(snakeTurn,-90)
        
        return None


    def getDirection(self):
        offX = self.snakeLine[0][0] - self.snakeLine[1][0]
        offY = self.snakeLine[0][1] - self.snakeLine[1][1]
        if (offX==30 or offX==-870) and offY==0:
            return K_RIGHT
        elif (offX==-30 or offX==870) and offY==0:
            return K_LEFT
        elif offX==0 and (offY==30 or offY==-570):
            return K_DOWN
        elif offX==0 and (offY==-30 or offY==570):
            return K_UP

    def move(self,KEY=None):
        #我们创建一个冲突列表
        wrong_list = [{K_RIGHT, K_RIGHT}, {K_RIGHT, K_LEFT}, {K_LEFT, K_LEFT},
         {K_UP, K_UP}, {K_UP, K_DOWN}, (K_DOWN, K_DOWN)]
        if KEY is None or {self.getDirection(), KEY} in wrong_list:
            KEY = self.getDirection() #按错方向键后，不改变原方向
        if KEY == K_RIGHT: #右移就在右侧添加蛇头，蛇尾减少1块
            self.snakeLine = [((self.snakeLine[0][0]+30)%900,self.snakeLine[0][1])] + self.snakeLine[0:-1]
        elif KEY == K_UP:  #上移就在上侧添加蛇头，蛇尾减少1块
            self.snakeLine = [(self.snakeLine[0][0], (600 + self.snakeLine[0][1] - 30)%600)] + self.snakeLine[0:-1]
        elif KEY == K_DOWN: #下移就在下侧添加蛇头，蛇尾减少1块
            self.snakeLine = [(self.snakeLine[0][0], (self.snakeLine[0][1] + 30)%600)] + self.snakeLine[0:-1]
        elif KEY == K_LEFT: #左移就在左侧添加蛇头，蛇尾减少1块
            self.snakeLine = [((self.snakeLine[0][0] - 30 + 900)%900, self.snakeLine[0][1])] + self.snakeLine[0:-1]

        self.show()

pygame.init()
screen = pygame.display.set_mode((900,600))
bg = pygame.image.load('bg.jpg')
snake = Snake(screen)
clock = pygame.time.Clock()
while True:
    clock.tick(2)
    KEY = None
    for eventType in pygame.event.get():  # 进行事件等待
        # 如果用户点击了关闭窗口按钮，那么就执行退出
        if eventType.type == QUIT:
            sys.exit()
        elif eventType.type == KEYUP:
            KEY = eventType.key
    screen.blit(bg,(0,0)) #先把背景贴覆盖上，删除原图上的小蛇
    snake.move(KEY)
    pygame.display.update()

