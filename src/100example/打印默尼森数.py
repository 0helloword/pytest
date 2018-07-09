# -*-coding:utf-8 -*-
# 经典程序设计问题：找第n个默尼森数。P是素数且M也是素数，并且满足等式M=2**P-1，则称M为默尼森数。
# 例如，P=5，M=2**P-1=31，5和31都是素数，因此31是默尼森数。
def sushu(n):
#     for i in range(1,100):
        for i in range(2,n):
            if n%i==0:
                return 0
                break
        else:
           return 1
            


    
for P in range (1,100):
    M=2**P-1
    if sushu(P)==1 and sushu(M)==1:
        print P,M