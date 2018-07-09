# -*-coding:UTF-8 -*-

# 
# def fn(n):
#     sum=1
#     for i in range (1,n+1):
#         sum*=i
#     return sum
#     
# print fn(4)

# 或者
def fn(n):
    sum=0
    if n==0:
        sum=1
    else:
        sum=fn(n-1)*n
    return sum
print fn(4)

#或者
# def fn(n):
#     if n==1:
#         return 1
#     else:
#         return fn(n-1)*n
#     
print fn(3)