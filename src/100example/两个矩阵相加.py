# -*-coding:UTF-8 -*-
# 两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵：

x=[1,2,3],[4,5,6],[7,8,9]
y=[1,2,3],[4,5,6],[7,8,9]

print x
print y
s=[0,0,0],[0,0,0],[0,0,0]
for i in range (len(x)):
    for j in range (len(y)):
        s[i][j]=x[i][j]+y[i][j]
print s    