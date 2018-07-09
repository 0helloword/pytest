#-*-coding:utf-8 -*-

#<、>、<=、>=、==、!= 值比较
print 1>2
print 4<9
print 2<=2
print 5>=8
print 1==1
print 'a'!='b'

#is、is not 对象身份比较
print 'a' is 'a'
print 'abc' is not 'cba'

#and、or、not 逻辑运算
a=1
b=0
print a and b
print a or b
print not(a)

#seq[start: end]    切片操作
a='hello world'
print a[1::]
print a[::-1]  #翻转
print a[2:5]
print a[:5]
b=[1,2,3,4,5]
print b[1::]
print b[1:3]

#*重复组合序列数据
s=[0]
print s*5
ss='a'
print ss*5 

#+连接 2个序列
m=[1,2,3]
n=[4,5,6]
print m+n

#in、not in判断元素是否存在序列中
q=['he','it','she']
print 'he' in q
print 'her' not in q

#list(iter) 将可迭代对象iter转换成列表
w='hello world'
print list(w)

#tuple(iter) 将可迭代对象iter转换成元组
w='hello world'
print tuple(w)

#str(obj) 将对象obj转换成字符串表示
ww=123
print str(ww)

#len(sequence) 返回sequence的长度，为整型类型
print len(w)

#sorted(iter, key, reverse) 返回可迭代对象iter排序后的列表，key用来指定排序的规则，reverse用来指定顺序还是逆序排列
print sorted(w)

#reversed(sequence) 返回序列sequence逆序排列后的迭代器
e=[1,2,3]
e.reverse()
print e


#sum(iter, start) 将iter中的数值和start参数的值相加，返回float类型数值
a=[1,2,3,4,5]
b=15.0
c=sum(a,b)
print c

#max(iter) 返回可迭代对象iter中的最大值
s=[156,2,34,56]
print max(s)

#min(iter) 返回可迭代对象iter中的最小值
print min(s)

#enumerate(iter[, start]) 返回一个enumerate对象，可生成一个迭代器，该迭代器的元素是由参数iter元素的索引和值组成的元组
ss=['hello','nihao']
for i,item in enumerate(ss):
    print i+1,item
    
#zip(iter1 [,iter2 [...]]) 返回一个zip对象，可生成一个迭代器，该迭代器的第n个元素是每个可迭代对象的第n个元素组成的元组
x=[1,2,3]
y=['a','b','c']
print zip(x,y)

