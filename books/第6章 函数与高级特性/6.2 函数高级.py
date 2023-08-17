
def sayHappy(name):
    print("Happy Birthday:"+ name)

def sayHello(name):
    print("Good days:"+ name)

def meet(name,say):
    print('You meet ' + name)
    say(name)

meet('zhang',sayHappy)
meet('wang',sayHello)

