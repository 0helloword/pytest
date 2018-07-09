# -*- coding: UTF-8 -*-

# 有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。

if __name__=='__main__':
    fp=open('A.txt','w')
    a=raw_input('input string:')
    fp.write(a)
    fp.close()
    
    fp=open('B.txt','w')
    b=raw_input('input string:')
    fp.write(b)
    fp.close()
    
    fp=open('C.txt','w')
    c=list(a+b)
    c.sort()  #排序
    s=''
    s=s.join(c)
    fp.write(s)
    fp = open('C.txt','r')
    print fp.read()
    fp.close()