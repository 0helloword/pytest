# -*-coding:UTF-8 -*-
from pyasn1.compat.octets import str2octs

str1=raw_input('input one string:')
str2=raw_input('input two string:')
str3=raw_input('input three string:')

# 方法一：
# if str1>str2:str1,str2=str2,str1
# if str1>str3:str1,str3=str3,str1
# if str2>str3:str2,str3=str3,str2
# print str1,str2,str3



# 方法二：
list1=[]
list1.extend([str1,str2,str3])
list2=sorted(list1)
print list2

