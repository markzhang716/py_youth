a = [1,2,3,4,5,6,7,9,10,10]
print('原始列表a=',a)
del(a[0])  #直接删除
print('删除a[0]:',a)
a.remove(10) #通过值来删除，只能删除1个
print('删除值10:',a)
deleted = a.pop(5)  #通过位置来“弹出”
print('弹出第5个元素pop(5):',a,deleted)
a.append('被添加文字') #列表可以容纳任何类型的元素
print('添加字符串:',a)
print('a的-3:-2切片:',a[-3:-2]) #列表的切片
print('a[-1]=',a[-1]) #列表的切片

