#本程序从500人的队伍里，随机挑出，如果满意就入选，不满意就归队
import random
volunteer = 500
while volunteer > 500-10:
    test = random.randint(1,volunteer)
    #下面的\符号表示一行写不完，人为换行，
    #可以把多行写成一行方便阅读
    if(input('还剩下'+ str(volunteer)+'人,\
        这是随机挑选的第'+str(test)+'号，您满意么(y/n)?') == 'y'):
        volunteer -= 1 #入选后队伍就会少1人
print('您已经选足了10个人!')
