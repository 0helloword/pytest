# -*-coding:utf-8-*-

from enum import Enum, unique

#test1
# Month=Enum('Month',('jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'))
# 
# for name,member in Month.__members__.items():
#     print (name,member,member.value)

#test2
# @unique
# class weekday(Enum):
#     sun=0
#     mon=1
#     tue=2
#     
# day1=weekday.mon
# print day1
# print day1.value
# print weekday.tue
# print weekday.tue.value
# print weekday(1)
# 
# for name,member in weekday.__members__.items():
#     print (name,member.value)


#test3
class gender(Enum):
    male=0
    female=1
class student(object):
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender

bart=student('bart',gender.male)
if bart.gender==gender.male:
    print 'pass'
else:
    print 'fail'
    
print type(gender)
print type(student)
    