# -*-coding:utf-8 -*-
from retry import retry

#@retry重试机制，如果方法执行失败，会重新执行n次
@retry(tries=3, delay=1,jitter=1)

# tries:重试的次数
# delay：延时时间
# jitter：累加，以及异常触发的日志

def make_trouble():
    print ('retrying...')
    raise#通过raise引发异常,执行重试机制

if __name__ == '__main__':
    import logging
    logging.basicConfig()
    make_trouble()
