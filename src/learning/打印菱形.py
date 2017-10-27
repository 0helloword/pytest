# -*-coding:UTF-8 -*-

for i in range (1,5):
    print 
    for j in range (1,5-i):
        print ' ',
    for k in range (1,i*2):
        print '*',
        
for i in range (1,4):
    print
    for j in range (1,i+1):
        print ' ',
    for k in range (1,8-2*i):
        print '*',