'''
1、请写一段程序通过输入的数字判断一下是不是偶数？
提示：% 操作符可以取余数。
'''
num = int(input('输入一个整数：'))
print('偶数' if num%2==0 else '奇数' )

'''
2、有1-100个编号的球，请随机找出编号不同的2个球。
'''
import random
ball1 = random.randint(1,100)
ball2 = random.randint(1,100)
if ball1 == ball2:
    print('失败，挑出了一样的编号。')
else:
    print(ball1,ball2)
