# -*-coding:UTF-8 -*-
# 一个五位数，个位等于万位，十位等于千位，即为回文数，判断一个一个五位数是否为回文数


num=int(raw_input('输入一个5位数：'))
a=num/10000
b=num%10000/1000
c=num%1000/100
d=num%100/10
e=num%10
print a,b,c,d,e

if a==e and b==d:
    print '该数字为回文数'
else:
    print '该数字不为回文数'