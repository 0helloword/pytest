# -*-coding:UTF-8 -*-

def sumtest(n,m):
    s=[]
    sum=0
    num=0
    for i in range (1,m+1):
        num+=n
        n=n*10
        s.append(num)
    print s
    for i in s:
        sum+=i
    return sum

n=int(raw_input('n='))
m=int(raw_input('m='))
print sumtest(n,m)


