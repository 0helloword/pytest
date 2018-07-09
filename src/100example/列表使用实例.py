# -*-coding:UTF-8 -*-

# #list
# #新建列表
# testlist=[10086,'中国移动',[1,2,3,4]]
# 
# #访问列表长度
# print len(testlist)
# 
# #到列表结尾
# print testlist[1:]
# 
# #向列表最后添加元素
# testlist.append('i\'m new here')
# 
#向列表中添加元素
#testlist.insert(2,'test')


# print len(testlist)
# print testlist[-1]
# 
# #删除列表的第二个元素
# print testlist.pop(1)
# print len(testlist)
# print testlist

matrix = [[1, 2, 3],  
[4, 5, 6],  
[7, 8, 9]]  
print matrix  
print matrix[1]  
col2 = [row[0] for row in matrix]#get a  column from a matrix  
print col2  
col2even = [row[0] for row in matrix if  row[0] % 2 == 0]#filter odd item  
print col2even  

