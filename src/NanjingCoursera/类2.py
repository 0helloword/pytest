# -*-coding:utf-8-*-

class roster(object):
    "students and teacher class"
    teacher=""
    students=[]
    def __init__(self,tn='mayun'):
        self.teacher=tn
        
    def add(self,sn):
        self.students.append(sn)
        
    def remove(self,sn):
        self.students.remove(sn)
        
    def print_all(self):
        print("teacher:",self.teacher)
        print("students",self.students)
        
Roster=roster()
Roster.add('caoyyj')
Roster.add('xiaola')
Roster.remove('xiaola')
Roster.print_all()