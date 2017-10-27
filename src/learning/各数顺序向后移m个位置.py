# -*-coding:utf-8-*-

# 有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
n=5
s=[]
print '请输入%d个数字'%n
for i in range (n):
    num=int(raw_input('输入数字：'))
    s.append(num)
print s
ss=s[:]  #这样修改a对b没有影响。修改b对a没有影响。如果用ss=s，对a或b的元素进行修改，a,b的值同时发生变化。或使用ss=copy.deepcopy(s)
print ss    
m=3
print '将每个数字向后移动%d位'%m
  
for i in range (n):
    if i+m<n:
 
        ss[i+m]=s[i]
    else:
        ss[i-m+1]=s[i]
print ss