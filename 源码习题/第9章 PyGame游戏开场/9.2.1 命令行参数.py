import sys,random
guess = sys.argv[1]
print('你的输入',guess)
if str(random.randint(1,3)) == guess:
    print('猜对了！')
else:
    print('猜错了！')
