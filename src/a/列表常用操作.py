# -*-coding:utf-8 -*-

#l.append(obj) 在列表l末尾添加新的对象
l=[1,2,3]
l.append('abc')
print l

#l.count(obj) 统计某个元素在列表l中出现的次数
print l.count('abc')

#l.extend(seq) 在列表l末尾一次性追加另一个序列seq中的多个值(用新列表扩展原来的列表)
l.extend(['a','b','c'])
print l

#l.index(obj) 从列表l中找出某个值第一个匹配项的索引位置，索引从0开始
print l.index('a')

#l.insert(index, obj) 将对象obj插入列表l中索引为index的元素前
l.insert(2, 'q')
print l

#l.pop(index) 移除列表l中索引为index的一个元素(默认为最后一个元素)，并且返回该元素的值
l.pop(2)
print l

#l.remove(obj) 移除列表l中某个值的第一个匹配项
l.remove('a')
print l

#l.reverse() 将列表l中的元素反转
l.reverse()
print l

#l.sort(key=None, reverse=False) 对原列表l进行排序，可通过参数key指定排序依据，通过参数reverse指定顺序（默认方式）或逆序排列
l.sort()
print l
