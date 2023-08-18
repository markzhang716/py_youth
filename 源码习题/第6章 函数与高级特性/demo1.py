#如下定义了 kill_dead函数，用来上报战况
# name: 表示人名变量, number:表示战绩变量
def kill_dead(name,number=1):
    print(name,'杀死异鬼',number,'头') #显示

# *names: 基于位置参数元组，表示的人名变量, 
# **killed:基于关键字参数的字典，表示目标和数量
def group_kill(*names,**killed):
    print(names,'杀死',killed['target'],killed['number'],'头') #显示

#张王被压缩成元组存在names,后面被组装进字典killed里。
group_kill('张','王',number=2,target='异龙')


#默认值不填
kill_dead('小牛叔')

#这是主程序（没有缩进）
kill_dead('Snow',2)  #位置参数调用
kill_dead(number=1,name='Sam')    #关键字参数调用
kill_dead('Guido',number = 1)    #位置+关键字参数调用

def money(dead:int,drag:int)->int:
    return (dead*50 + drag*500)

print('2人3龙的赏金为:',money(2,3))