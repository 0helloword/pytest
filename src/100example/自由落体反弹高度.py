# -*-coding:UTF-8 -*-

sum=100.0
h=100.0
n=int(raw_input('输入球落地和反弹次数:'))
for i in range (1,n):
    sum+=h
    h=h/2
    
print '球落地%d次共经过%f米，第%d次反弹高度为%f' %(n,sum,n,h/2)