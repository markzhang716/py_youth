class Bread:
    weight = 34
    hard = 0
    def cook():
        Bread.hard += 5  #每烤一次，硬度增加5,重量少1
        Bread.weight -= 1
        print('bread are being cooked.....')
    def isOk():
        return Bread.hard<=15 #硬度过了15就不能吃了


print('weight:',Bread.weight)

Bread.cook()
Bread.cook()
print('isOK:',Bread.isOk())

Bread.cook()
Bread.cook()
print('isOK',Bread.isOk())
print('weight',Bread.weight)
