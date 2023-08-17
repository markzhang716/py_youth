class Gun:
    def __init__(self,name,typeOf,bullets = 0):
        self.name = name
        self.type = typeOf
        self.bullets = bullets
    def __str__(self):
        return self.name + ":" + str(self.bullets) + "发弹匣的 " + self.type

class HandGun(Gun):
    def __init__(self,name,action='单发',bullets=0):
        super(HandGun,self).__init__(name,'手枪',bullets)  #重写的方法，也使用了父类
        self.action = action                  #增加的属性 

hg = HandGun('FN Five-seveN','双发',20)  #使用了重写的__init__函数
print(hg)                               #使用了Gun父类的__str__函数
print('激发:' + hg.action)               #增加了一个属性