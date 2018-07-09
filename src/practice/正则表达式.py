#-*-coding:utf-8-*-
import re

# 版本一应该可以验证出类似的Email：
# someone@gmail.com
# bill.gates@microsoft.com
# 版本二可以验证并提取出带名字的Email地址：
# <Tom Paris> tom@voyager.org


r_telephone=re.compile(r'([a-zA-Z0-9._]+@+[gmail|qq|microsoft]+.+[com|cn])$')
print r_telephone.match('someone@gmail.cn').group()
print r_telephone.match('bill.gates@microsoft.com').group()

v = re.match(r'^(<[0-9a-zA-Z\s_]+>)\s+([0-9a-zA-Z._]+@[0-9a-z]+.\w+)$', '<Tom Paris> tom@voyager.org')
print v.group(1)