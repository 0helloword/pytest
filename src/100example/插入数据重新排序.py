# -*-coding:UTF-8 -*-

# 有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
s=[1,5,9,10]
a=int(raw_input("输入一个数字："))

# for i in range (len(s)-1):
#     if s[i]<a<s[i+1]:
#         s.insert(i+1, a)
# print s

#或
s.append(a)
s.sort()
print s