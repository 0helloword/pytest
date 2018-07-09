# -*- coding: UTF-8 -*-
# 从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止
# 创建了 runoobfile.txt 文件并向其写入 runoob 和 google 两个字符串，查看 runoobfile.txt 文件内容

from sys import stdout

if __name__=='__main__':
    filename=raw_input('input file name:')
    fp=open(filename,'w')
    ch=raw_input('input string:')
    while ch!='#':
        fp.write(ch)
        stdout.write(ch)
        ch=raw_input('1')
#     fp.close()
    print fp.open(filename,'r')
    fp.close()
