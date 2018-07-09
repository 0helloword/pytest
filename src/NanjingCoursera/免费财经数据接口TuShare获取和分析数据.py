# -*-coding:utf-8 -*-

#pip install tushare
# "TuShare是一个免费、开源的python财经数据接口包。主要实现对股票等金融数据从数据采集、清洗加工 到 数据存储的过程，
# 能够为金融分析人员提供快速、整洁、和多样的便于分析的数据，为他们在数据获取方面极大地减轻工作量，使他们更加专注于策略和模型的研究与实现上。
# 考虑到Python pandas包在金融量化分析中体现出的优势，TuShare返回的绝大部分的数据格式都是pandas DataFrame类型，
# 非常便于用pandas/NumPy/Matplotlib进行数据分析和可视化。当然，如果您习惯了用Excel或者关系型数据库做分析，
# 您也可以通过TuShare的数据存储功能，将数据全部保存到本地后进行分析。"
# 这是TuShare官网（http://tushare.org/index.html）上对于TuShare的描述，它提供了便捷的各类财经数据和新闻等的接口。

# 例如要想获取股票代码是600848的股票在2017年3月1日至3月10日间的基本历史数据，只要使用如下代码即可：
# 1.在命令提示符窗口中输入如下命令安装：pip install tushare
# import tushare as ts
# print ts.get_hist_data('510880',start='2017-11-01',end='2017-11-07')
import tushare as ts
id=raw_input('输入要查询的股票代码:')
startdate=raw_input('输入查询开始日期:')
enddate=raw_input('输入查询结束日期:')
print ts.get_hist_data(id,start=startdate,end=enddate)