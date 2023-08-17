import random
poke = [2,3,4,5,6,7,8,9,10,11,12,13,14]
for i in range(len(poke)*2):
    poke.append(poke.pop(random.randint(0,len(poke)-1)))
print('洗牌后:',poke)
poke.sort()
print('顺牌后:',poke)