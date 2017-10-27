# -*-coding:UTF-8 -*-
# 给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字

num=int(raw_input('输入一个不多于5位的正整数：'))
a=num/10000
b=num%10000/1000
c=num%1000/100
d=num%100/10
e=num%10


if a!=0:
    print '5位数',e,d,c,b,a
elif b!=0:
    print '4位数',e,d,c,b
elif c!=0:
    print '3位数',e,d,c    
elif d!=0:
    print '2位数',e,d
else:
    print '1位数',e