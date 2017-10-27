# -*- coding: UTF-8 -*-
from string import upper
from sys import stdout

# 从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存。

if __name__=='__main__':
    fp = open('test.txt','w')
    ch=raw_input('input string:')
    CH=upper(ch)
    fp.write(CH)
    fp = open('test.txt','r')
    print fp.read()
    fp.close()
        