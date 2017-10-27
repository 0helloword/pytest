#!/usr/bin/python
# -*- coding: UTF-8 -*-
#类的私有方法

class test:
    __privatecount=0   #私有变量，以两条下横线开头仅能在类的内部调用
    _protectcount=0    #protected 变量,以单下划线开头，即保护类型只能允许其本身与子类进行访问
    publiccount=0     #公开变量

    def count(self):
        self.__privatecount+=1
        self.publiccount+=1
        self._protectcount+=1
        print self.__privatecount
        print self._protectcount
        print self.publiccount
        pass
    
class test1(test):
    def num(self):
        pass

class test2():
    def num2(self):
        pass
    
    
counter=test()
counter.count()
print counter.publiccount
print counter._protectcount
print counter._test__privatecount
#print counter.__secretcount    # 报错，实例不能访问私有变量

counter2=test1()
counter2.count()
print counter2.publiccount
print counter2._protectcount
print counter2._test__privatecount

