a=[1,2,3,4,5]   #定义5个元素的列表
b=[] #定义了空的列表
c=['夜王前传',1045,'龙晶使用方法',1056] #定义了书名序号
d=[['夜王前传','龙晶使用方法'],[1045,1056]]   #定了2个列表元素（书名列表、序号列表）的列表
print(a[-4:-2],a[100:])  #倒数第4至第2元素
del a[0]
print('删除a第0个:',a)
a.append(5)
print('添加5,a:',a)
a.remove(5)  #只能删除一次5
print('删除数值5,a:',a)
b = a.pop(3)
print('弹出第3个元素,a:',a,',弹出了:',b)
#第0个位置前插入字符“首”
a.insert(0,'首')
print('插入a:',a)
