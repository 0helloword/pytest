# -*-coding:utf-8 -*-
#enumerate()字典上是枚举、列举的意思
# s=['today','is','a','funny','day']
# for i in range(len(s)):
#     print i,s[i], 
# print '\n'   
# 
# for index,item in  enumerate(s):
#     print index,item,
# print '\n'
# 
# #第二个参数指定索引起始值    
# for index,item in  enumerate(s,1):
#     print index,item,
# print'\n'    
# 
# 
# #reversed()倒序
# n=[1,2,3,4,5]
# n.reverse()
# print n
# nn=[1,2,3,4,5]
# reversed(nn)#不改变nn的顺序
# print nn
# 
# #sorted()按从小到大排序
# m=[4,55,33,37,2]
# m.sort()
# print m
# mm=[4,55,33,37,2]
# sorted(mm)#不改变mm的排序
# print mm

#zip()接受任意多个（包括0个和1个）序列作为参数，返回一个tuple列表
x=[1,2,3]
y=[4,5,6]
a=zip(x,y)
print a
list=[[1,2,3],[4,5,6],[7,8,9]]
t=zip(*list)
print t
print [sum(x) for x in list]

#map
# b=['1','2','3','4']
# print map(list,b)#将列表a中的每个元素转换为列表
# print map(int,b)#将列表a中的每个元素转换为整数



