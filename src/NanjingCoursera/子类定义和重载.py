# -*-coding:utf-8-*-

class Dog(object):
    counter=0
    
    def __init__(self,name):
        self.name=name
        Dog.counter+=1
        
    def great(self):
        print "hello,my name is %s,i'm the number %s"%(self.name,Dog.counter)
        
class NewDog(Dog):
    def great(self):
        print "wow,,my name is %s,i'm the number %s"%(self.name,Dog.counter)        
        

dog=NewDog('wangcai')
dog.great() 
     