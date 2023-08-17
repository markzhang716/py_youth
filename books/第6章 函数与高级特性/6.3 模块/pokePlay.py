import pokeTools
myMoney= 10 #我的筹码
cmpMoney = 10 #电脑的筹码

def play2cards():
    global myMoney,cmpMoney
    print('2幅牌的梭哈游戏开始。')
    while myMoney>0 and cmpMoney >0:
        print('您现在还有%d筹码，我还有%d筹码'%(myMoney,cmpMoney))
        #开幅新牌然后洗牌
        pokeTools.newCards()
        pokeTools.washCards()
        #给我发2张牌
        myCard = pokeTools.licensing(2)
        #给电脑发2张牌
        cmpCard = pokeTools.licensing(2)
        #显示你们抽中的
        print('发牌结束，您的牌是：',myCard)
        #获得我的下注
        myBid = pokeTools.bid(myMoney)
        #是不是我赢了
        iWon =False
        #把牌翻译成牌力
        myCardPower = [pokeTools.cardsPower[x] for x in myCard]
        cmpCardPower = [pokeTools.cardsPower[x] for x in cmpCard]

        #最大的那张牌的花色代表的牌力
        myCardSuit = [pokeTools.cardSuit.index(x[0]) for x in myCard if pokeTools.cardsPower[x]==max(myCardPower)]
        cmpCardSuit = [pokeTools.cardSuit.index(x[0]) for x in cmpCard if pokeTools.cardsPower[x]==max(cmpCardPower)]


        #我是对子，电脑不是，我赢
        if cmpCardPower[0]!=cmpCardPower[1] and myCardPower[0] == myCardPower[1]:
            iWon = True
        #我们都是对子，但是我点数大
        elif cmpCardPower[0]==cmpCardPower[1] and myCardPower[0] == myCardPower[1]\
        and myCardPower[0]>cmpCardPower[0]:
            iWon = True
        #我们都是对子，点数一样，花色大
        elif cmpCardPower[0]==cmpCardPower[1] and myCardPower[0] == myCardPower[1]\
        and myCardPower[0]==cmpCardPower[0] and max(myCardSuit) > max(cmpCardSuit):
            iWon = True
        #都是单只，比较最大的数字
        elif cmpCardPower[0]!=cmpCardPower[1] and myCardPower[0] != myCardPower[1]\
        and max(myCardPower)>max(cmpCardPower):
            iWon = True
        #都是单只，数字相同比较花色
        elif cmpCardPower[0]!=cmpCardPower[1] and myCardPower[0] != myCardPower[1]\
        and max(myCardPower)==max(cmpCardPower) and max(myCardSuit)>max(myCardSuit):
            iWon = True

        print('我的牌是：',cmpCard)

        #判断输赢
        if iWon:
            print('恭喜，您赢了！')
            myMoney += myBid
            cmpMoney -= myBid
        else:
            print('抱歉，您输了！')
            myMoney -= myBid
            cmpMoney += myBid
    else:
        print('你' if myMoney>cmpMoney else '我' + '的筹码已经用完，游戏结束!')
#play2cards()

import pokeTools

print('牌字',pokeTools.cardText)
print('花色',pokeTools.cardSuit)
print('牌力表',pokeTools.cardsPower)
print('牌',pokeTools.cards)
print('洗牌',pokeTools.washCards())