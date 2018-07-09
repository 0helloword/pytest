# -*-coding:utf-8-*-

class Dog(object):
    counter=0
    
    def __init__(self,name):
        self.name=name
        Dog.counter+=1
        
    def great(self):
        print "hello,my name is %s,i'm the number %s"%(self.name,Dog.counter)
        
        
dog=Dog('wangcai')
dog.great() 
dog=Dog('pite')
dog.great()     