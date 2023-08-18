import getpass
joe = me  = 0 #joe得分、我的得分和总局数都为0
rounds = 1
while rounds<=5:
    print('第%d局开始了！\n1-剪刀 2-石头 3-布'%rounds)
    joe_input = getpass.getpass('Joe:')
    me_input = getpass.getpass('我:')
    if joe_input not in '123' or me_input not in '123' or len(me_input)!=1 or len(joe_input)!=1:
        print('请只输入1-3，重来')
        continue   
    print('Joe出%s,我出%s'%(joe_input,me_input))
    #以下计算我们输入数字之差
    distance =  int(joe_input) - int(me_input)
    if distance == 0:     #如果差是0，即2个输入一样是平局
        print('平局不算！')
        continue
    elif distance == 1 or distance==-2:    #如果差是1，或-2，即Joe赢了
        joe+=1
        print("Joe 赢了！")
    else:
        me+=1
        print("我 赢了！")
    if joe==3 or me==3:
        break
    rounds += 1
if joe==3:   
    print('最终的赢家是：Joe!')
else:
    print('最终的赢家是：我!')
