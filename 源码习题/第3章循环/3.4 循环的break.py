for i in range(1,13):
    print('这是第',i,'天')
    if(input('看到红色信号弹了(y/n)?')=='y'):
        break
    if(i%2==0):
        continue
    print('维护望远镜')
else:
    print('13天-等待结束！')
print('准备营救!')