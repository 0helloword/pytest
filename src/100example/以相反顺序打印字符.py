# -*-coding:UTF-8 -*-


a=raw_input('输入字符串：')
a=list(a)
for i in range (0,len(a)/2):
    t=a[i]
    a[i]=a[len(a)-1-i]
    a[len(a)-1-i]=t
print a
