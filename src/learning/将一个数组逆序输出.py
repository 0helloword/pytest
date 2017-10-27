# -*-coding:UTF-8 -*-

a=[1,2,3,4,5]
n=len(a)
for i in range (0,n/2):
    t=a[i]
    a[i]=a[n-1-i]
    a[n-1-i]=t
print a    

# 或者：
# a=[1,2,3,4,5]
# print a[::-1]
