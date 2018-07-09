# -*-coding:UTF-8 -*-
# 求一个3*3矩阵对角线元素之和。


# if __name__=="__main__":
#     a=[]
#     sum=0.0
#     for i in range (3):
#         a.append([])
#         for j in range (3):
#             a[i].append(int(raw_input('输入一个数字:\n')))
#         print
#         
#     
#     print a  
#     
#     for i in range (3):
#         sum+=a[i][i]
#     print sum  
    
if __name__=="__main__":
    a=[1,2,3],[4,5,6],[7,8,9]   
    sum=0.0 
    for i in range (3):
        sum+=a[i][i]
    print sum