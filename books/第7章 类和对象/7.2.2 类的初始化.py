#class语句表示我们将建一个类
class Gun:
    #fire在类中的一个函数，即为类的一个方法
    def fire(self):
        if self.bullets>0:
            self.bullets -= 1
        print("*")
    #类的初始化方法
    def __init__(self):
        self.color = 'Red'
        self.size = '1.2'
        self.bullets = 10


myGun = Gun()
print(str(myGun))
#myGun.color = 'Red'
#myGun.size = '1.2'
#myGun.bullets = 10
myGun.fire()
print(myGun)