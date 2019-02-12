# -*- coding: utf-8 -*-

a=['periods','repayType','bankCardName','bankCardNo','productId',]
b=[u'bankCardName', u'bankCardNo', u'periods', u'productId', u'repayType','123']

# c=list(set(a)  ^ set(b))
c=list(set(a).difference(set(b)))
print  c
