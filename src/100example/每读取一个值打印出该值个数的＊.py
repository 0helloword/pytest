# -*-coding:UTF-8 -*-

import random

# 读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊

if __name__=='__main__':
    for i in range (1,8):
        m=int(raw_input('\n输入一个1-50之间的整数：'))
        for j in range(0,m):
            print '*',
            