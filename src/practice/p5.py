#!/usr/bin/python
# -*- coding: UTF-8 -*-
#方法重写


class parent:
    def __init__(self):
        print '这是父类构造函数'
    def mymethod(self):
        print '调用父类方法'

        
class child(parent):
    def __init__(self):
        print '这是子类构造函数'
    def mymethod(self):
        print '调用子类方法'

        
c=child()
c.mymethod()

#运算符重载
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b
 
    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)
   
    def __add__(self,other):
        return Vector(self.a + other.a, self.b + other.b)
 
v1 = Vector(2,10)
v2 = Vector(5,-2)
print v1 + v2

