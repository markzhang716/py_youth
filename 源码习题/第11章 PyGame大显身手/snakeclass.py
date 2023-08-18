import pygame, os, sys
from pygame.locals import *
import random
FILE_PATH = os.path.join(os.path.dirname(__file__), 'files')
os.chdir(FILE_PATH)

def show_end(screen):
    end_clock = pygame.time.Clock() #滴答时钟
    #结束画面
    origin_end_image = pygame.image.load('end.png')
    #宽高比
    ratios = origin_end_image.get_rect().width/origin_end_image.get_rect().height
    #开始从200宽的图显示
    newWidth = 200
    old_ticks = pygame.time.get_ticks() #获得从开始以来的毫秒数
    while 1:
        end_clock.tick(20)
        ticks = pygame.time.get_ticks()-old_ticks #获得从开始以来的毫秒数
        for eventType in pygame.event.get():  # 进行事件等待
            # 如果用户点击了关闭窗口按钮，那么就执行退出
            if eventType.type == QUIT:
                sys.exit()
            #当图片宽度足够时，按任意键退出
            if eventType.type ==KEYUP and newWidth>700:
                return
        #当图片宽度不足700时，就从200放大
        if newWidth<=700:
            newWidth += int(ticks/1000*20)
        #从原始图片实现放大，比较清晰
        end_image = pygame.transform.smoothscale(origin_end_image,
        (newWidth,int(newWidth/ratios)))
        #要贴图的位置在屏幕正中央
        x,y = int((900-end_image.get_rect().width)/2),int((600-end_image.get_rect().height)/2)
        screen.fill(Color(0,0,0)) #黑色背景
        screen.blit(end_image,(x,y))
        pygame.display.update()

class Snake(pygame.sprite.Sprite):
    snakeHead = pygame.image.load('snake_head.png') #头
    snakeBody = pygame.image.load('snake_body_h.png') #身
    snakeTail = pygame.image.load('snake_tail.png') #尾
    snakeTurn = pygame.image.load('snake_turn.png') #身

    def __init__(self,screen):
        pygame.sprite.Sprite.__init__(self)
        #表示组成蛇每一个图片的左上角坐标，初始就是3张图片，从蛇头开始
        self.snakeLine = [(450,300),(450-30,300),(450-60,300)]
        self.screen = screen #传入屏幕
        self.rect = Rect(450,300,30,30) #蛇头的区域
        self.lengthening = 0

    #根据新的蛇的坐标来画出蛇的
    def show(self,newSnakeLine = None):
        if newSnakeLine is not None:
            self.snakeLine = newSnakeLine #把新的位置设置成当前位置
            self.rect = Rect(newSnakeLine[0],(30,30))
        
        self.rect = Rect(self.snakeLine[0],(30,30))
        #画出身体
        for inx,cord in enumerate(self.snakeLine):
            self.screen.blit(self.getBodyImage(inx),cord)
        
    def getBodyImage(self,index):
        if index == 0 or index == len(self.snakeLine)-1: #如果是第0或最后一块
            #前面的块
            before = self.snakeLine[0] if index==0 else self.snakeLine[-2]
            #后面的块
            after = self.snakeLine[1] if index==0 else self.snakeLine[-1]
            offX = before[0] - after[0]
            offY = before[1] - after[1]
            if (offX==30 or offX==-870) and offY==0:
                return Snake.snakeHead if index ==0 else Snake.snakeTail
            elif (offX==-30 or offX==870) and offY==0:
                return pygame.transform.rotate(Snake.snakeHead if index ==0 else Snake.snakeTail,180)
            elif offX==0 and (offY==30 or offY==-570):
                return pygame.transform.rotate(Snake.snakeHead if index ==0 else Snake.snakeTail,-90)
            elif offX==0 and (offY==-30 or offY==570):
                return pygame.transform.rotate(Snake.snakeHead if index ==0 else Snake.snakeTail,90)
        elif self.snakeLine[index-1][0] == self.snakeLine[index+1][0]:
            #x坐标相同就是垂直身体
            return pygame.transform.rotate(Snake.snakeBody,90)
        elif self.snakeLine[index-1][1] == self.snakeLine[index+1][1]:
            #y坐标相同就是水平的身体
            return Snake.snakeBody
        else:
            #是否x,y坐标同时大于另一块
            slope = (self.snakeLine[index-1][0]  - self.snakeLine[index+1][0])/(self.snakeLine[index-1][1] - self.snakeLine[index+1][1])
            #是否存在一块x坐标大于中间块
            right =  max(self.snakeLine[index-1][0],self.snakeLine[index+1][0]) > self.snakeLine[index][0]
            if slope>0 and right:
                return pygame.transform.rotate(Snake.snakeTurn,180)
            elif slope>0 and not right:
                return Snake.snakeTurn
            elif slope<0 and right:
                return pygame.transform.rotate(Snake.snakeTurn,90)
            elif slope<0 and not right:
                return pygame.transform.rotate(Snake.snakeTurn,-90)
        
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

        if self.lengthening>0:
            self.enlarge()
            self.lengthening -= 1
        else:
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
        #self.show()
    
    def enlarge(self):
        #增加的蛇头与原来的蛇头的坐标偏移
        adding_block_offset = {K_LEFT:(-30,0),K_RIGHT:(30,0),K_UP:(0,-30),K_DOWN:(0,30)} 
        offset = adding_block_offset[self.getDirection()]
        self.snakeLine.insert(0,
        (offset[0]+self.snakeLine[0][0],offset[1]+self.snakeLine[0][1]))


class Raspberry(pygame.sprite.Sprite):
    '''
    蛇吃的树莓
    '''
    group = pygame.sprite.Group()
    #屏幕30X30网格的所有左上角坐标
    screenBlankGrid = [(x*30,y*30) for x in range(0,30) for y in range(0,20)]

    def __init__(self, snake_line=[]):
        pygame.sprite.Sprite.__init__(self)
        blank_grid = list(filter(lambda x :x not in snake_line, Raspberry.screenBlankGrid))
        xy = random.choice(blank_grid)
        Raspberry.screenBlankGrid.remove(xy) #占用
        self.rect = Rect(xy[0], xy[1], 30, 30)
        self.image =pygame.image.load('snake_food.png')
        Raspberry.group.add(self)