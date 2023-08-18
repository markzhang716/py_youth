#包含有几项的数列
def fab(max): 
    n, a, b = 0, 0, 1
    fab_result = []
    while n < max: 
       fab_result.append(b) 
       a, b = b, a + b 
       n = n + 1
    return fab_result


#包含有几项的数列
def fab2(max): 
    n, a, b = 0, 0, 1
    while n < max: 
        yield b
        a, b = b, a + b 
        n = n + 1


#包含有几项的数列
def fab3(): 
    a, b =0, 1
    while True: 
        yield b       
        a, b = b, a + b 

#递归的娄列
def fab4(n):
    if n==0 or n==1:
        return 1
    return fab4(n-1) + fab4(n-2)

print(fab4(20))


f= fab3()

while True:
    print(next(f))
    if input()=="n":
        break

for f in fab2(100):
    print(f,end=',')