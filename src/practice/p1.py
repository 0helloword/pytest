# -*- coding: utf-8 -*-   

class employee:
    emcount=0
    
    def __init__(self,name,salary):#类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
        self.name=name              #self 代表类的实例，self 在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数
        self.salary=salary
        employee.emcount+=1
        
    def displaycount(self):
        print "total employee %d" %employee.emcount
    
    def displayemployee(self):
        print "name:" ,self.name,"salary:",self.salary
        
#实例
#"创建 Employee 类的第一个对象
emp1 = employee("Zara", 2000)
#"创建 Employee 类的第二个对象
emp2 = employee("Manni", 5000)

#访问类属性
emp1.displayemployee()
emp2.displayemployee()
print "Total employee %d" % employee.emcount
