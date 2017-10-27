# -*-coding:UTF-8 -*-
# 编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n

def fn1(n):
    sum=0.5
    for i in range(2,n-1):
        sum+=1.0/(2*i)
    return sum
    
def fn2(n):
    sum=1.0
    for i in range(2,n):
        sum+=1.0/(2*i-1)
    return sum
        
if __name__=='__main__':       
    n=int(raw_input('input n:'))

    if n%2==0:
        print fn1(n)
    else:
        print fn2(n)