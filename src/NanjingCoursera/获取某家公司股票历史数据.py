#-*-coding:utf-8-*-
import requests
import re
import json
import pandas

def test(stock_code):
    quotes=[]
    url='https://finance.yahoo.com/quote/%s/history?p=%s' %(stock_code,stock_code)
    r=requests.get(url)
    m=re.findall('"HistoricalPriceStore":{"prices":(.*?),"isPending"',r.text)
    if m:
        quotes=json.loads(m[0])
        quotes=quotes[::-1]
    return [item for item in quotes if not 'type' in item]

quotes=test('AXP')
quotesdf=pandas.DataFrame(quotes)
print(quotesdf)