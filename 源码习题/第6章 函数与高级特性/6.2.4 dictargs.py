
def sayHello(myname,*args,**kwargs):
    print('My name is ' + myname,end=', Hello:')
    print(','.join(list(args)))
    print('We have a ' + kwargs.get('weather','good') + ' day')
    print('What a nice ' + kwargs.get('week','day') + ' today')

sayHello("Joe","Pony","Tony",week="Monday",weather="sunny")
sayHello("Joe")


