def card_1():
    if True:
        number = 'J'
    print(number)

#如果我赢了就把电脑的筹码给我
def win():
    global Me,Computer #声明这2个变量是全局变量
    Me += stake
    Computer -= stake
#如果我输了就把我的筹码给电脑
def lose(): 
    global Me,Computer #声明这2个变量是全局变量
    Me -= stake
    Computer += stake
#显示2家的筹码数量
def show():
    print("Me:%d,Computer:%d"%(Me,Computer))
#各买10个筹码
def buy():
    global Me,Computer
    Me = 10
    Computer = 10
Me = 0 #我的初始筹码
Computer = 0 #电脑的初始筹码
show() #显示初始状态
buy() #买10个筹码
show() #显示

stake = 2  #每次下注2个筹码
win() #我赢了一次
show() #显示2家数量
win() #我赢了一次
show() #显示2家数量
lose() #我输了一次
show() #显示2家数量