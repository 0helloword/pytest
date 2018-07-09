# -*-coding:utf-8-*-

# 输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。

s=[]

for i in range(5):
    i=int(raw_input('输入数字：'))
    s.append(i)
    
print s

max=s[0]
min=s[0]
for i in range(5):
    if max<s[i]:
        max=s[i]
        t1=s[0]
        s[0]=max
        s[i]=t1
for j in range(5):
    if min>s[j]:
        min=s[j]
        t2=s[4]
        s[4]=min
        s[j]=t2
print max,min  

 
print s