#-*-coding:utf-8-*-
#yield将函数变为generator，并提供了跳出功能，send()是next的高级形式，可以赋值给yield。
def h():  
    print( 'Wen Chuan') 
    m = yield 1 
    print( m )
    d = yield 2  
    print ('We are together!'  )
c = h()  
m = next(c) #m 获取了yield 1 的参数值 1
print m
# n=next(c)#会从m=yield 1开始，只是由于next(c)没有提供入参，所以m为None，因而print（m）打印出来为None
# print n
n=c.send('hello')#使用send提供入参
print n