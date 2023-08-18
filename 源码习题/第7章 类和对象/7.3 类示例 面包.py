class Bread:
    #初始化方法
    def __init__(self):
        self.cooked_level = 0
        self.cooked_string = '软嫩'
        self.condiments = []
        self.slices = 1
    #烤的方法
    def cook(self,time):
        self.cooked_level += time
        if self.cooked_level>=10:
            self.cooked_string = '焦糊'
        elif self.cooked_level>=8:
            self.cooked_string = '硬脆'
        elif self.cooked_level>=6:
            self.cooked_string = '适中'
        elif self.cooked_level>=3:
            self.cooked_string = '稍软'
        else:
            self.cooked_string = '软嫩'
    #添加配料的方法
    def addCondiment(self,condi):
        self.condiments.append(condi)
    #添加片的方法
    def addSlice(self,number=1):
        self.slices+=number    
    #返回比较详细的信息数据
    def __str__(self):
        return  str(self.slices) + ' 个面包片，烤了' + \
        str(self.cooked_level) + '分钟，现在口感：' + \
        self.cooked_string + ',有配料:' + ','.join(self.condiments)


joeBread = Bread()
print(joeBread)
joeBread.addSlice(1)
joeBread.cook(8)
print("Joe加了1片，烤了8分钟")
print(joeBread)
joeBread.addCondiment('黄油')
print("Joe加了点黄油")
print(joeBread)
joeBread.cook(3)
print("Joe又烤了3分钟")
print(joeBread)



