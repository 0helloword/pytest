# -*- coding: UTF-8 -*-
#!/usr/bin/python
#python的内置类属性

#__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
#__doc__ :类的文档字符�?
#__name__: 类名
#__module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于�?��导入模块mymod中，那么className.__module__ 等于 mymod�?
#__bases__ : 类的�?��父类构成元素（包含了�?��由所有父类组成的元组�?

class Employee:
 #  '�?��员工的基�?
    empCount = 0
 
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
   
    def displayCount(self):
        print "Total Employee %d" % Employee.empCount
 
    def displayEmployee(self):
        print "Name : ", self.name,  ", Salary: ", self.salary
 
print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__