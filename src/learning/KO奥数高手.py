# -*- coding: utf-8 -*-
# 2000个5（55555...55555）除以84的余数是多少吗

sum=''

for i in range(2000):
    sum=sum+'5'
print sum
print int(sum)%84

#或

sum='5'*2000
print int(sum)%84