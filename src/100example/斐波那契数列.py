# -*-coding:UTF-8 -*-
#0 1 1 2 3 5 8
#1递归（为了求一个f(n),我们要多次计算前面的数值,这样既浪费了内存,又浪费了计算能力）
# def fin(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fin(n-1)+fin(n-2)
#  
# n=int(raw_input('输入显示的数列个数：'))   
# for i in range (0,n):
#     print fin(i)
    
#2循环(减少了生成数列的速度,但是如果想要生成某一个值的话,却需要从头开始计算就不太方便)
# def Fibonacci_Loop(n):
#     result_list = []
#     a, b = 0, 1
#     while n > 0:
#         result_list.append(b)
#         a, b = b, a + b
#         n -= 1
#     return result_list
# print Fibonacci_Loop(6)

#yield关键字(可以在不打断循环的情况下从循环中返回数值)
def fi(n):
    a,b=0,1
    while n>0:
        yield b#yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，Python 解释器会将其视为一个 generator
        a,b=b,a+b
        n-=1
print list(fi(5))
