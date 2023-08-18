import pygame, os, sys,time
from pygame.locals import *
import random
import files.pygame_textinput as pygame_textinput

FILE_PATH = os.path.join(os.path.dirname(__file__), 'files')
os.chdir(FILE_PATH)
font = pygame.font.Font(None,30)

def main_loop(screen):
    #加入成功的声音
    sound_eat = pygame.mixer.Sound('sound_snake_get.wav')
    sound_hit = pygame.mixer.Sound('sound_snake_fail.wav')
    bg = pygame.image.load('bg.jpg')
    snake = Snake(screen)
    clock = pygame.time.Clock()
    level = 1
    last_collide = None
    KEY = None
    SNAKEEVENT = USEREVENT + 1
    pygame.time.set_timer(SNAKEEVENT, 300)
    eaten = []
    food_score,time_score = 0,0
    font = pygame.font.Font(None,30)
    while True:
        clock.tick(20)
        time_score = int(pygame.time.get_ticks()/1000)
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
                food_score += 10
                level += 1
                eaten.append(rasp)
                snake.lengthening += 1
                #加入成功的声音
                sound_eat.play()
                
            else:
                #碰撞对象相同，说明还是同一个食物，那么就缩小2个像素
                rasp.image = pygame.transform.smoothscale(rasp.image,(int(rasp.rect.width-2),int(rasp.rect.height-2)))
                rasp.rect.inflate_ip(-2,-2)
            last_collide = rasp

        #当从碰撞中走出来时 或者 进入了一个新的碰撞时 就从组里删除被吃的树莓
        if last_collide and  rasp != last_collide and last_collide in Raspberry.group.sprites():
            for one_eaten in eaten:
                one_eaten.kill()
            eaten = []

        #根据难度增长树莓数量
        while len(Raspberry.group.sprites())<int(level):
            Raspberry(snake.snakeLine)
        #绘制树莓
        Raspberry.group.draw(screen)
        pygame.display.update()

        if not snake.live:
            sound_hit.play()
            break
    return food_score,time_score

def show_top10(screen,score):
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


def high_score(screen, score):
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
    fileContent = '\n'.join([ x[0]+str(x[1]) for x in top10])
    file.write(fileContent)
    file.close()
    return top10

def input_name(screen):
    #创建文本输入对象
    textinput = pygame_textinput.TextInput()
    textinput.font_size = 30
    textinput.text_color = Color(255,0,0)
    textinput.cursor_color = Color(255,0,0)
    clock = pygame.time.Clock()
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


def show_end(screen,food_score=0,time_score = 0):
    
    old_screen = screen.copy()
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
            if eventType.type == KEYUP and newWidth>700:
                return
        #当图片宽度不足700时，就从200放大
        if newWidth<=700:
            newWidth += int(ticks/1000*20)
        #从原始图片实现放大，比较清晰
        end_image = pygame.transform.smoothscale(origin_end_image,
        (newWidth,int(newWidth/ratios)))
        #要贴图的位置在屏幕正中央
        x,y = int((900-end_image.get_rect().width)/2),int((400-end_image.get_rect().height)/2)
        screen.blit(old_screen,(0,0)) #填充原来的图案
        screen.blit(end_image,(x,y))
        #当画圈静止时，显示一片绿色计分区域
        if newWidth>700:
            pygame.draw.rect(screen,Color(153,204,51),Rect(150,350,600,200))
            screen.blit(pygame.image.load('snake_food.png'),(350,380))
            screen.blit(font.render(str(food_score) + '  Points',1,Color(255,0,0)),
                (500,370))
            screen.blit(pygame.image.load('time.png'),(350,430))
            screen.blit(font.render(str(time_score) + '  Points',1,Color(255,0,0)),
                (500,420))    
            screen.blit(font.render('Total:',1,Color(255,0,0)),
                (350,480))
            screen.blit(font.render(str(time_score + food_score) + '  Points',1,Color(255,0,0)),
                (500,480))

        pygame.display.update()

def show_start(screen):
    # 加载图像
    background = pygame.image.load('snake_start.png')
    pygame.mixer.music.load('sound_snake_start.mp3') #开场音乐
    pygame.mixer.music.play(loops=-1) #循环播放

    # 开始不停地进行图像循环
    screen.blit(background,[0,0])  # 把背景图画到0。0开始的坐标点上去
    while True:
        for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                if event.type == KEYDOWN:
                    pygame.mixer.music.stop() #音乐停止播放
                    return
        time.sleep(0.05)
        screen.fill(pygame.Color(0,0,0),Rect(0,560,900,40)) #画出黑框
        if int(time.time())%2 ==0: #如果是偶数秒就画上文字
            screen.blit(font.render('Press any key......',1,Color(255,255,255)),[200,565])
        pygame.display.update()  # 把图像显示出来


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
        self.live = True

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
        #如果蛇的位置列表当中有重复值，就说明自身在碰撞
        if len(set(self.snakeLine)) < len(self.snakeLine):
            self.live = False
            return
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

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((900,600))
    bg = pygame.image.load('bg.jpg')
    screen.blit(bg,(0,0)) #先把背景贴覆盖上，删除原图
    food_score,time_score = 10,20
    font = pygame.font.Font(None,30)

    show_end(screen,30,51)
    print(high_score(screen,91))
