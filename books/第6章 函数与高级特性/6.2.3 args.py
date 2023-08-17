def sayHello(*args):
    for name in args:
        print("Hello "+ name)

'''        
sayHello()
sayHello('Herny','Partinton')
sayHello('Herny','Partinton','Tony Spark')
sayHello('A','B',"C","D")
exit()
'''

def sayHello2(weather,*args):
    for name in args:
        print("Hello "+ name)
    print("It is a " + weather + " day.Isn't it?")
sayHello2('windy','Herny','Partinton')
sayHello2('cloudy','Herny','Partinton','Tony Spark')

def sayHello3(*args,weather):
    print(','.join([x for x in args]))
    print('we have a ' + weather + ' day')
sayHello3('Herny','Partinton',weather="fine")
sayHello3('Herny','Partinton','Tony Spark',weather = 'cloudy')

