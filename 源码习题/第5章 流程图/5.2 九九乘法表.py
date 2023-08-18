for i in range(1,10):
    print(('┣' if i>1 else '┏') + ('━'*8 + '╋') * (i-1) + '━'*8 + '┓'+ ' ' * 5+ ('-- > 第%d行 表线行\n' % i))  
    for j in range(1,i+1):
        print("┃%2d×%-2d=%2d"%(j,i,i*j),end='')
    print('┃' + ' ' * 5 + '-- > 第%d行 算式行\n'%i)
print('┗' + ('━'*8 + '┻')*8 + '━'*8 + '┛')

for i in range(1,10):
    print(('┣' if i>1 else '┏') + ('━'*8 + '╋') * (i-1) + '━'*8 + '┓')  
    for j in range(1,i+1):
        print("┃%2d×%-2d=%2d"%(j,i,i*j),end='')
    print('┃' + ' ' * 5 )
print('┗' + ('━'*8 + '┻')*8 + '━'*8 + '┛')