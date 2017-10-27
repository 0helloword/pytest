# -*-coding:UTF-8 -*-
from math import sqrt
from __builtin__ import quit

# 求输入数字的平方，如果平方运算后小于 50 则退出。
while(1):
    n=int(raw_input('输入一个数字：'))
    s=n*n
    if s<50:
        break
    else:
        print '请继续输入'



