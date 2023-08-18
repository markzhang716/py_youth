def sayHello(name,week='',weather=''):
    print("Hello " + name + ". ",end = '')
    print(("Wish you have a nice " + week + ". ") if week !='' else '',end = '')
    print(("We have a " + weather + " day,isn't it?") if weather !='' else '')

sayHello('zhang')
sayHello('zhang','Friday','good')
sayHello('zhang',weather='fine')
sayHello(name = 'zhang',week='Monday')