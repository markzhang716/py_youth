print({'男','女'})
mySet = set()
mySet.update('男','女')
print(mySet)
price_list = {'鱼香肉丝':58,'鸡汤':88,'番茄炒蛋':90}
print(price_list['鸡汤'])
for eachKey in price_list:
    print(eachKey,price_list[eachKey])