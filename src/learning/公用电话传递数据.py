# -*-coding:UTF-8 -*-
# 某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：
# 每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。
from test.test_long import SHIFT

if __name__=='__main__':
    n=int(raw_input('输入一个4位的整数：'))
    qian=n/1000
    bai=n/100%10
    shi=n/10%10
    ge=n%10
    print qian,bai,shi,ge
    qian+=5
    qian=qian%10
    bai+=5
    bai=bai%10
    shi+=5
    shi=shi%10
    ge+=5
    ge=ge%10
    print qian,bai,shi,ge
#     t1=qian
#     qian=ge
#     ge=t1
#     t2=bai
#     bai=shi
#     shi=t2
    qian,ge=ge,qian
    bai,shi=shi,bai
    print qian*1000+bai*100+shi*10+ge