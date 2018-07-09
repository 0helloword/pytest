#-*-coding:utf-8-*-
from collections import namedtuple
from _collections import deque, defaultdict
from asn1crypto._ordereddict import OrderedDict

# namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
circle=namedtuple('circle',['x','y','r'])
c=circle(3,3,5)
print c.x,c.y,c.r
print isinstance(c, circle)
print isinstance(c, tuple)

# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
l=deque([1,2,3])
l.append('a')
print l
l.appendleft(5)
print l
l.pop()
print l
l.popleft()
print l

# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
d=defaultdict(lambda:'N/A')
d['one']='hello'
print d['one'],d['two']

# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
# 如果要保持Key的顺序，可以用OrderedDict：
dd=([('a',1),('b',2),('c',3)])
print dd
cc=OrderedDict([('a',1),('b',2),('c',3)])
print cc