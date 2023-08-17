class Compass:
    invitedBy = '中国'
    usedFor ='导航'
    __p = '从外面看不见\n'
    #初始化方法
    def __init__(self):
        self.shape = 'round'
        self.__magnetism = 4
        Compass.__p += '初始化\n'
        self.__secret()
    def setMag(self,mag_level=4):
        self.__magnetism = mag_level
    def getStatus(self):
        return "正常" if self.__magnetism>=1 else "失效"
    def __secret(self):
        return 'called secret method'

com1,com2 = Compass(),Compass()
com1.setMag(1)
com2.setMag(0.5)
print(com1.getStatus(),com2.getStatus())
#私有变量是经过系统的改写
print(com1._Compass__magnetism)

#下面的语名会出错
#print(com1.__magnetism)
#print(Compass.__p,com1.__secret)
