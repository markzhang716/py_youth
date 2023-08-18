#牌的字符
cardText = [str(number) for number in range(2,11)] + ['J','Q','K','A']
#牌的花色
cardSuit = ['♠','♡','♣','♢']
#生成整个54张牌
cardDict = {s + t:cardText.index(t) for t in cardText for s in cardSuit}
#加入小鬼和大鬼
cardDict.update({'Joker-':12,'Joker+':13})
print(cardDict)
#形成有顺序的一套牌
oneSetCard = [s + t for t in cardText for s in cardSuit] + ['Joker-','Joker+']
#洗牌
import random
for c in range(len(oneSetCard)):
    oneSetCard.append(oneSetCard.pop(random.randint(0,len(oneSetCard)-1)))
#输入您的选择
myCard = oneSetCard[int(input('牌已洗好，输入您选第几张(0-53):'))]
#电脑进行选择
robotCard = oneSetCard[random.randint(0,len(oneSetCard)-1)]
#显示你们抽中的
print('您抽中%s，电脑抽中%s'%(myCard,robotCard))
#判断输赢
if cardDict[myCard] > cardDict[robotCard]:
    print('恭喜，您赢了！')
elif cardDict[myCard] == cardDict[robotCard]:
    print('平局！')
else:
    print('遗憾，您输了！')
   
   
    