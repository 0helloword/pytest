# -*-coding:UTF-8 -*-
import time,datetime

time.sleep(1)
TIME=datetime.datetime.now()
TIME1=datetime.datetime.today()
print TIME
print TIME1
print (TIME.strftime("%Y.%m.%d %H-%M-%S"))