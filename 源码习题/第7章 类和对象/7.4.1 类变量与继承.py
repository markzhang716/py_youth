
class Compass:
    invitedBy = '中国'
    usedFor ='导航'
    #初始化方法
    def __init__(self):
        self.shape = 'round'
com1,com2 = Compass(),Compass()

print(Compass.invitedBy,com1.invitedBy,com2.invitedBy)

Compass.invitedBy = 'CN'
print(com1.invitedBy,com2.invitedBy)
#下面的语句，并不是给类变量赋值，将会创建一个对象的实例变量
com1.invitedBy = 'Korean'
print(com1.invitedBy,com1.__class__.invitedBy,com2.invitedBy)

