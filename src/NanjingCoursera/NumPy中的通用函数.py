# -*-coding:utf-8-*-
#NumPy中的通用函数与math库中函数的比较。将两者的运行时间比较打印出来

from numpy.random.mtrand import np
import math
import time



# a=np.arange(1,10)
# print a

start = time.clock()
b=np.abs(-5)
print b
end = time.clock()
print end-start

# c=np.add(1,2)
# print c

# d=np.alen('hello')
# print d
# 
# aa=math.floor(1)
# print aa
# 
# bb=math.log(3)
# print bb

# cc=math.ceil(5)
# print cc
start2 = time.clock()
dd=math.fabs(-5)
print dd
end2 = time.clock()
print end2-start2