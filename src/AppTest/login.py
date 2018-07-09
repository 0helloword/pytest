# -*- coding: utf-8 -*-
import time

#登录
def login(driver):
    driver.find_element_by_name('手机号码/世纪佳缘账号').send_keys('15626513325')
    driver.find_element_by_id('com.jiufu.heyuanwanka:id/et_psd_numb').send_keys('123456')
    # #unicode编码方式发送字符串
    # desired_caps["unicodeKeyboard"] = "True"
    # #resetKeyboard是将键盘隐藏起来
    # desired_caps["resetKeyboard"] = "True"
    driver.hide_keyboard()#隐藏键盘
    time.sleep(2)
    driver.find_element_by_name('登录').click()
    print 'login success'
