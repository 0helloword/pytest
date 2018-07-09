#-*-coding:utf-8-*-
import requests
import re
import pandas

r=requests.get("http://www.weather.com.cn/weather/101280601.shtml")
search=re.compile('class="sky skyid lv.*?">\n<h1>(.*?)</h1>\n<big.*?></big>\n<big.*?></big>\n<p.*?>(.*?)</p>')
li=re.findall(search, r.text)
print li
print type(li)

