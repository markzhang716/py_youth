def peach(day):
    # 如果是第十天就返回1(1个桃子)
    if day == 10:
        return 1
    else:
        print("求第%d天"%day)
        y =(peach(day+1) +1) * 2
        print("第%d天，结果：%d"%(day,y))
        return y

print(peach(1))