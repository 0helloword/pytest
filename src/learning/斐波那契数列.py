# -*-coding:UTF-8 -*-

def fin(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fin(n-1)+fin(n-2)
 
n=int(raw_input('输入显示的数列个数：'))   
for i in range (0,n):
    print fin(i)