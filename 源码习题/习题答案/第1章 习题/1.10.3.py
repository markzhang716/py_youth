'''
有3个变量a、b、c，如何让b的值变成原来a的值，
a的值变成原来c的值，c的值变成原来a的值（即值往右移）？ 
'''

a,b,c = 1,2,3
print(a,b,c)
a,b,c = c,a,b
print(a,b,c)