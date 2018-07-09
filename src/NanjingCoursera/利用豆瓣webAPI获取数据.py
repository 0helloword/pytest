#-*-coding:utf-8-*-
#利用豆瓣的webAPI更方便的获取数据， 因为这样获取的已经是数据部分 而不是HTML文件，
#HTML文件还需要进一步的解析才能获得里面真正的内容
#来看一个豆瓣图书API的例子 来理解下API的功能 例如我们要抓取《小王子》这本书的一些基本信息 我们以往是直接抓取它的HTML页面 
#然后进行解析获得其中的内容 通过API我们可以更简单
#https://developers.douban.com/豆瓣api地址
import requests
import json

a=requests.get('https://api.douban.com/v2/book/1084336')
print a.text
r=json.loads(a.text)#获取json数据
print r.keys()#获取json中的关键字
print r.values()#获取json中的值
print r["rating"]#获取关键字rating中的值
print r["rating"]["max"]#获取关键字rating中max的值
print r['tags'][0]['name']#获取关键字tags中第一行中name的值
