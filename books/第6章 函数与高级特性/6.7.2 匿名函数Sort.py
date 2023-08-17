org =  [1,-2,3,4,5,]
print(list(sorted(org,key=lambda x:-x)))
print(list(sorted(org,reverse =True)))

org.sort(key=lambda x:-x)
print(org)


scores = [('黄忠',23),('张飞',45),('赵云',10)]
scores.sort()
print(scores)
scores.sort(key = lambda x:x[1])
print(scores)