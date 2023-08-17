#class语句表示我们将建一个类
class Gun:
    #fire在类中的一个函数，即为类的一个方法
    def fire(self):
        if self.bullets>0:
            self.bullets -= 1
        print("*")


myGun = Gun()
myGun.color = 'Red'
myGun.size = '1.2'
myGun.bullets = 10
myGun.fire()
print(myGun.bullets,myGun.color,myGun.size)