# -*-coding:UTF-8 -*-
# 一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.


for i in range (1,1000):
    sum=0
    s=[]
    for j in range (1,i):
        if i%j==0:
            sum+=j
            s.append(j)
    if sum==i:
        print i
        print s