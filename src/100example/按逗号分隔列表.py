# -*-coding:UTF-8 -*-

L=[1,2,3,4,5]
for i in L:
    print str(i)+',',


M=[11,22,33,44,55]
S=','.join(str(i) for i in M)
print S