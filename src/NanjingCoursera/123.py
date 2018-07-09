#-*-coding:utf-8-*-
import pandas
from numpy.random.mtrand import np

#创建一个dataframe
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