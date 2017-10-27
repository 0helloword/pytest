# -*-coding:utf-8 -*-
import random


file_address=r'G:\pythonCase\idCards.txt'
file=open(file_address,'r')

s1=[]
for line in file.readlines():
    s1.append(line.strip('\n'))
file.close()

s11=s1[random.randint(0,len(s1)-1)]  #身份证前6位-地区代码
print s11   
s2=str(random.randint(1963,1997)) #生日-年
print s2
s3=['01','02','03','04','05','06','07','08','09','10','11','12']
s33=s3[random.randint(0,len(s3)-1)] #生日-月
print s33
s4=['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28']
s44=s4[random.randint(0,len(s4)-1)] #生日-日
print s44
s5=str(random.randint(1,999)) #序号
print s5
s6='1234567890X'
s66=s6[random.randint(0,len(s6)-1)] #校验位
print s66

print s11+s2+s33+s44+s5+s66