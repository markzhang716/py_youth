import random
def washCard(cards=None):
    if cards is None:
        cards = [str(x) for x in range(2,11)] + ['J','Q','K','A']
    for i in range(len(cards)):
        cards.append(cards.pop(random.randint(0, len(cards)-1)))
    return cards
print(washCard())



def sayHappy(name):
    print("Happy Birthday:"+ name)
sayHappy('Queen')
sayHappy('King')

sh = sayHappy

sh('zhang')