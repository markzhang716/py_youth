def move(n, a, b, c):
    if(n == 1):
        print(a,"->",c)
        return
    move(n-1, a, c, b) #把n-1个柱子从从a移到b
    move(1, a, b, c)   #把最后一个柱子从a移动到c
    move(n-1, b, a, c) #n-1的柱子从b移动到c

move(3,'a','b','c')