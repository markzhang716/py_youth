'''
1、定义一个Person类，包含出生日期(born date)和姓名(name)两个属性，
并且有一个age（）方法，可以根据当前日期计算出年龄。
2、根据Person类实例化如下2个实例对象，并计算年龄之差。
姓名	出生日期
Stannis	1983-10-1
Lannister	1998-5-1
3、通过继承Person类，定义Student类，并且增加学号（StudentID）属性(字符串)，增加成绩列表属性（整数列表），并增加getAvg()方法，用来获得所有分数的平均分。
4、根据上题实例化如下的数据，并且打印出每个人的平均分和年龄。
姓名	出生日期	学号	分数
Stannis	1983-10-1	17210691006	80，89，100，90
Lannister	1998-5-1	18220690260	60，80，74，69
'''
from datetime import *  #引入日期库，处理年龄

class Person:
    def __init__(self,bornDate,name):
        self.born_date = bornDate
        self.name = name
    def age(self):
        return date.today().year - self.born_date.year

stannis = Person(date(1983,10,1),'Stannis')
lannister = Person(date(1998,5,1),'Lannister')
print(stannis.age()-lannister.age())

class Student(Person):
    def __init__(self,bore_date,name,StuID):
        self.StuID = StuID
        self.scores = []
        super().__init__(bore_date,name)
    def add(self,*score):
        self.scores += score
    def getAve(self):
        return sum(self.scores)/len(self.scores)

stannis = Student(date(1983,10,1),'Stannis','17210691006')
lannister = Student(date(1998,5,1),'Lannister','18220690260')
stannis.add(80,89,100,90)
lannister.add(60,80,74,69)
print(lannister.getAve(),lannister.getAve())



