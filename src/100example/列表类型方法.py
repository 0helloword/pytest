# -*-coding:utf-8 -*-

#append()向列表尾部追加一个新元素，列表只占一个索引位，在原有列表上增加
a=[1,2,3]
b=[4,5,6]
# a.append(b)
print a


#extend()向列表尾部追加一个列表，将列表中的每个元素都追加进来，在原有列表上增加
# a.extend(b)
print a

#+ 直接用+号看上去与用extend()一样的效果，但是实际上是生成了一个新的列表存这两个列表的和，只能用在两个列表相加上
# print a+b

#+= 效果与extend()一样，向原列表追加一个新元素，在原有列表上增加
a+=b
print a

#count()返回子字符串在字符串中出现的次数。
str='he is a good man,he feel happy'
s='he'
print str.count(s)
print str.count(s,5,10)#在指定的起始位置返回字符串出现的次数

#insert()用于将指定列表对象插入列表的指定位置
c=[1,2,3,4,5]
c.insert(1,'w')
print c

#pop()将列表中指定元素删除
d=[1,2,3,4,5]
d.pop()#不加参数默认去掉最后一个元素
print d
d.pop(1)
print d

#sort()排序
e=[34,3,45,2]
e.sort()
print e
