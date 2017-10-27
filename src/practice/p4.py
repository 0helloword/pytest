#!/usr/bin/python
# -*- coding: UTF-8 -*-
#类的继承

class Parent1:        # 定义父类
    parentAttr = 100
   
    def __init__(self):
        print "调用父类构造函数"
 
    def parentMethod(self):
        print '调用父类方法'
 
    def setAttr(self, attr):
        Parent1.parentAttr = attr
 
    def getAttr(self):
        print "父类属性 :", Parent1.parentAttr
        
class Parent2:
    parentnum=22
    
    def __init__(self):
        print "这是父类构造函数"
        
    def method1(self):
        print Parent2.parentnum
        
    def method2(self):
        print "这是parent2的第二个方法"
 
class Child(Parent1): # 定义子类
    def __init__(self):
        print "调用子类构造方法"
 
    def childMethod(self):
        print '调用子类方法 child method'
        
class Child2(Parent1,Parent2):
    def __init__(self):
        print "这是child2的构造方法"
        
    def childMethod(self):
        print "这是child2的方法"
 
c = Child()          # 实例化子类
c.childMethod()      # 调用子类的方法
c.parentMethod()     # 调用父类方法
c.setAttr(200)       # 再次调用父类的方法
c.getAttr()          # 再次调用父类

d=Child2()
d.childMethod()
d.parentMethod()
d.method1()
d.method2()

e1=isinstance(d, Parent1)  #isinstance判断d是Class类的实例对象或�?是一个Class子类的实例对象则返回true
print e1
e2=isinstance(d, Child2)
print e2