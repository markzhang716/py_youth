for i in range(1,13):
    print('行军',i,'小时')
    if(input('所有马匹状态良好(y/n)?')=='y'):
        continue
    print('休整10分钟')
print('到达雪山附近!')