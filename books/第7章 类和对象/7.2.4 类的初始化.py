#class语句表示我们将建一个类
class Gun:
    #fire在类中的一个函数，即为类的一个方法
    def fire(this):
        if this.bullets>0:
            this.bullets -= 1
        print("*")
    #类的初始化方法
    def __init__(self):
        self.color = 'Red'
        self.size = '1.2'
        self.bullets = 10
    def __str__(self):
        return '%s gun has %d bullets'%(self.color,self.bullets)


myGun = Gun()  #我的枪
myGun.fire() #激发一次，应该剩9
JoeGun = Gun()  #Joe的枪
JoeGun.fire()   #激发了2次，应该剩8
JoeGun.fire()
print('My Gun',myGun)
print('Joe Gun',JoeGun)
myGun.fire() == Gun.fire(myGun)