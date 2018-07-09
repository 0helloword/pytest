# -*- coding: utf-8 -*-

#先获取屏幕的大小，每款手机尺寸不一，所以通过get_window_size函数获取尺寸。

    
def swipe_up(driver):#上滑操作就是从屏幕的下端点击一个坐标然后往上滑动，x坐标可以不变。Y的开始和结束坐标改进即可。
    width=driver.get_window_size()['width']
    height=driver.get_window_size()['height']
    driver.swipe(width/2,height*7/8,width/2,height*1/2,1000)
    
def taptest(driver):
    # 设定系数,控件在当前手机的坐标位置除以当前手机的最大坐标就是相对的系数了
    a1 = 188.8/1069#额度分期的相对系数
    b1 = 941.5/1916
    # 获取当前手机屏幕大小X,Y
    X = driver.get_window_size()['width']
    Y = driver.get_window_size()['height']
    # 屏幕坐标乘以系数即为用户要点击位置的具体坐标
    driver.tap([(a1*X, b1*Y)])