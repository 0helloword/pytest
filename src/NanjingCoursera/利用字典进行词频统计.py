# -*-coding:utf-8 -*-
# 对于一个已分词的中文句子：
# "我 是 一个 测试 句子，大家 赶快 来 统计 我 吧，大家 赶快 来 统计 我 吧，家 赶快 来 统计 我 吧，重要 事情 说 三遍！"
# 可以用collections模块中的Counter()函数方便地统计词频
import collections

s='我是一个测试句子，大家 赶快 来 统计 我 吧，大家 赶快 来 统计 我 吧，家 赶快 来 统计 我 吧，重要 事情 说 三遍！'
print s
s_list=s.split()    #通过指定分隔符对字符串进行切片
print s_list
[s_list.remove(item) for item in s_list if item in ',!。“”']
print (collections.Counter(s_list))

# #英文字符串统计
# s2='hello world'
# s22=s2.split()
# [s22.remove(item) for item in s22 if item in ',!。“”']
# print (collections.Counter(s22))

#通过字典来解决，请编写用字典解决本问题的程序。
q='我是一个测试句子，大家 赶快 来 统计 我 吧，大家 赶快 来 统计 我 吧，家 赶快 来 统计 我 吧，重要 事情 说 三遍！'
q_list=q.split()
q_dict={}
for item in q_list:
    if item not in ',/。""':
        if item not in q_dict:
            q_dict[item]=1
        else:
            q_dict[item]+=1
print q_dict

