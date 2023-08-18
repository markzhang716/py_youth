#Sam学院中把书籍位置使用（柜号，行号，列号）来表示
book_a_loc = (1,23,34)
book_b_loc = (5,10,90)
print('a书位置:',book_a_loc)
print('a书行列:',book_a_loc[1:])
print('b书行号:',book_b_loc[1])

#试删除第1个元素会出错
del book_a_loc[0]
