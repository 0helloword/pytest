# -*-coding:UTF-8 -*-

score=int(raw_input('score:'))
if score>=90:
    print 'A'
elif 60<score<89:
    print 'B'
else:
    print 'C'


# 或者
score=int(raw_input('score:'))
if score in range(0,60):
    print 'C'
elif score in range(61,90):
    print 'B'
else:
    print 'A'