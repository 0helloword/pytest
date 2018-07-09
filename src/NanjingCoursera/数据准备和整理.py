#-*-coding:utf-8-*-
#那数据获得后我们常常要对它进行整理 比如说我们观察这组数据 我们发现 它的index和columns 也就是行索引和列索引 都用了默认的方式
#也就是从0开始编号的一组整数 这样的方式含义不够清晰 处理上也不太方便 特别是columns 
#所以再做其他的数据处理之前 我们最好对它们先进行整理 我们直接对数据进行操作 
#利用DataFrame的 columns和index属性修改它的列索引和行索引

import pandas
from datetime import date
from numpy.random.mtrand import np

a=pandas.read_csv(r'F:\test\workspace\PyhtonTest\src\NanjingCoursera\test.csv')
a.columns=['name','type','price','date']
a.index=range(1,len(a)+1)
print a
# print a['date'][1]
list=[]

for i in range(1,len(a)+1):
    x=date.fromtimestamp(a['date'][i])#转换成常规时间
    y=date.strftime(x,'%y-%m-%d')#转换成固定格式
    list.append(y)
# print list
b=pandas.DataFrame(a,index=list)
print b  #打印出来的值为NaN,暂未解决该问题

d=b.drop(['date'],axis=1)
print d
#转换时间戳
# firstday=date.fromtimestamp(1464010200)
# lastday=date.fromtimestamp(1495200600)
# print firstday,lastday



#创建一个dataframe，创建一个时间序列
dates=pandas.date_range('20170101',periods=7)
ss=pandas.DataFrame(np.random.randn(7,3),index=dates,columns=['a','b','c'])#生成一个7*3的矩阵
print 'dataframe ss显示为\n%s'%ss

#数据显示
print 'dataframe结构'
print ss.index#显示行索引
print ss.columns#列索引
print ss.shape#显示数据的维度
print ss.size#显示元素的个数
print ss.describe#显示数据的基本描述
print ss.values#显示所有的值

print 'dataframe数据列筛选'
print ss.a#显示数据的某一列的值，方法1
print ss['a']#显示数据的某一列的值，方法2


print 'dataframe数据行筛选-切片'
print ss.head(1)#显示第一行数据，方法1
print ss[:1]#显示第一行数据，方法2
print ss.tail(2)#显示最后两行数据，方法1
print ss[-2:]#显示最后两行数据，方法2

print 'dataframe数据选择-条件筛选'
print ss['2017-01-01':'2017-01-02']#根据日期筛选
print ss[(ss.a<1)&(ss.b>1)]#根据数值筛选