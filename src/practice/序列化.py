#-*-coding:utf-8-*-
import json

class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    
    
    def std2dict(self,s):
        return {
             'name':self.name,
             'age':self.age,   
             'score':self.score
                }
        
    def dict2std(self,d):
        return Student(d['name'],d['age'],d['score'])
    
s=Student('cc',18,90)
print json.dumps(s,default=s.std2dict)
print(json.dumps(s, default=lambda obj: obj.__dict__))
json_str='{"age": 18, "score": 90, "name": "cc"}'
print json.loads(json_str,object_hook=s.dict2std)

