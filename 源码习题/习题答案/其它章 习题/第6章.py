'''
1、请自行编写程序打印出前20项斐波那契数列。
'''
a,b,n=1,1,2 #a前项,b后项,n第几项
while n<20:
    a,b = b,a+b
    n += 1
print(n,b)

'''
2、有这么一个数列0，1，2，2，3，5，7，10，15，22
 f(n) = f(n-1)+f(n-3) ，请编写程序列出前20项。
'''

def fn2(n):
    if n==1:
        return 0
    if n==2:
        return 1
    if n==3:
        return 2
    return fn2(n-1) + fn2(n-3)

print(fn2(20))

'''
3、把如下的菜单形成由元组组成的列表，并且使用匿名函数给如下的菜单按单价排序。
菜单	单价
Salad	5
Hamburger	10
Juice	12
Apple Pie	9
'''

menu = [('Salad',5),('Hamburger',10),('Juice',12),('Apple Pie',9)]
menu.sort(key = lambda x:x[1])
print(menu)

'''
4、利用递归函数打印第20项的斐波那契数列数值。
斐波那契数列公式：f(n) = f(n-1)+f(n-2)
'''
def fibo(n):
    if n==1 or n==2:
        return 1
    return fibo(n-1) + fibo(n-2)

print(fibo(20))