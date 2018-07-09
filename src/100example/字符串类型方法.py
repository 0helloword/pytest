# -*-coding:utf-8 -*-
from string import maketrans

#join()
a=','
b='00hello world00'
print a.join(b)

#strip()移除字符串头尾指定的字符
print b.strip('0')


#Replace
print b.replace('h', 'o')


#split()将一个字符串分割为子字符串,然后将结果作为字符串数组返回
print b.split('o')

#translate()根据参数table给出的表(包含 256 个字符)转换字符串的字符, 要过滤掉的字符放到 del 参数中
a='abcde'
b='12345'
trant=maketrans(a,b)
str='abcdefg'
print str.translate(trant)
print str.translate(trant,'ab')#将ab字符过滤掉


#startswith()
c='hello'
print c.startswith('e')
print c.startswith('e',1)
print c.startswith('el',1,3)#字符串的起始位置
