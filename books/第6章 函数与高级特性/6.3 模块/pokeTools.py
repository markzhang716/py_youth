#牌的字符
cardText = [str(number) for number in range(2,11)] + ['J','Q','K','A']
#牌的花色
cardSuit = list(reversed(['♠','♡','♣','♢']))
#牌的牌力
#生成整个54张牌
cardsPower = {s + t:cardText.index(t) for t in cardText for s in cardSuit}
#加入小鬼和大鬼
cardsPower.update({'Joker-':13,'Joker+':14})
#形成有顺序的一套牌,此时没有大小鬼
cards = [s + t for t in cardText for s in cardSuit]

#洗牌
import random
def washCards():
    random.shuffle(cards)
    return cards
#新牌    
def newCards():
    #形成有顺序的一套牌
    global cards
    cards = [s + t for t in cardText for s in cardSuit]
    return cards
#发牌
def licensing(x=1):
    global cards
    popup,cards = cards[0:x],cards[x:]
    return popup

#输入赌注，如果输入错误或是太大就反复输入 
def bid(myMoney):
    myBid = None
    while myBid is None or myBid>myMoney:
        if myBid is not None:
            print('输入不正确，请重新输入。')
        myBid = input('您堵几个筹码？')
        if not myBid.isnumeric():
            continue
        else:
            myBid = int(myBid)
    return myBid
    