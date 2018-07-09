# -*-coding:utf-8-*-
# 已知有一个列表中存放了一组音乐数据：
# music_data = [("the rolling stones","Satisfaction"),("Beatles","Let It Be"),("Guns N' Roses","Don't Cry"),("Metallica","Nothing Else Matters")]
# 请根据这组数据创建一个如下的DataFrame
#                singer             song_name
# 1  the rolling stones          Satisfaction
# 2             Beatles             Let It Be
# 3       Guns N' Roses             Don't Cry
# 4           Metallica  Nothing Else Matters
#利用python扩展库，NumPy,Pandas

from numpy.random.mtrand import np
import pandas

music_data = [("the rolling stones","Satisfaction"),("Beatles","Let It Be"),("Guns N' Roses","Don't Cry"),("Metallica","Nothing Else Matters")]
print music_data
# info=np.array(music_data)              #pip install NumPy
# print info
frame=pandas.DataFrame(music_data,index=range(1,5),columns=['singer','song_name'])           #pip install Pandas
#frame.index=range(1,5)
#frame.columns=['singer','song_name']
print frame