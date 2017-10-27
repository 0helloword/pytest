# -*-coding:UTF-8 -*-

x=int(raw_input('int1:\n'))
y=int(raw_input('int2:\n'))

Min=min(x,y)
Max=max(x,y)

z=int(raw_input('int3:\n'))

if z>Max:
    print Min,Max,z
elif z<Min:
    print z,Min,Max
else:
    print Min,z,Max
