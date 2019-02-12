#-*-coding:utf-8-*-
#@符号属于函数式编程的装饰器。放在函数定义的上面。主要作用是在不改变原来函数代码的前提下，给函数增加新的功能。

# import time
# def deco(func):
#     def ctime():
#         starttime=time.time()
#         func()
#         endtime=time.time()
#         usetime=endtime-starttime
#         print usetime
#     return ctime
# 
# @deco
# def func():
#     print 'hello'
#     time.sleep(1)
#     print 'world'
#     
# func()

def deco(func):
    print 'before myfunc() called'
    func()
    print 'after myfunc() called'
    return func

@deco
def myfunc():
    print 'myfunc() called'












