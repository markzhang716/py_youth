import getpass
print('1-剪刀 2-石头 3-布')
joe_input = getpass.getpass('Joe:')
me_input = getpass.getpass('我:')
print('Joe出%s,我出%s'%(joe_input,me_input))
if joe_input not in '123' or me_input not in '123' or len(me_input)!=1:
    print('请只输入1-3。')
    exit()
#以下计算我们输入数字之差
distance =  int(joe_input) - int(me_input)
if distance == 0:     #如果差是0，即2个输入一样是平局
    print('平局！')
elif distance == 1 or distance==-2:    #如果差是1，或-2，即Joe赢了
    print("Joe 赢了！")
else:
    print("我 赢了！")
