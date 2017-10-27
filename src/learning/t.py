# -*-coding:utf-8-*-
fp=open('text.txt','w')
fp.write('Life is short, you need Python.\nSimple is better than complex.')
fp.close()

with open('text.txt', 'r+') as fp:
    fp.seek(15)
    print(fp.readline())