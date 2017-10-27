# -*-coding:UTF-8 -*-

sum=0

for i in range (1,21):
    k=1
    for j in range (1,i+1):
        k*=j
    sum+=k
print sum
