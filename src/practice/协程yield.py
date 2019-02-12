#-*-coding:utf-8-*-
def consumer():#如果一个函数中加了yield，则该函数变为一个generator
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'#consumer通过yield拿到消息，处理，又通过yield把结果传回

def produce(c):
    c.send(None)#启动生成器，初始化
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)#一旦生产了东西，通过c.send(n)切换到consumer执行
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()#produce决定不生产了，通过c.close()关闭consumer，整个过程结束

c = consumer()#consumer函数是一个generator
produce(c)