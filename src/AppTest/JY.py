# -*- coding: utf-8 -*-
from appium import webdriver
import unittest
import time
from appium.webdriver.mobilecommand import MobileCommand


class JY(unittest.TestCase):
    def set_up(self):
        desired_caps = {
        'platformName': 'Android',
        'deviceName': 'EATGNJCYBADAGEU8',
        'platformVersion': '5.1',
        'appPackage': 'com.jiufu.heyuanwanka',
        'appActivity': '.ui.activity.StartLoadingActivity',
    }
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)#启动APP
        self.driver=driver
#         print self.driver.page_source

#         driver.implicitly_wait(30) #隐性等待
     

      
    def test_regist(self):
        print self.driver.contexts#打印当前页面的所有context
        self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": "NATIVE_APP"})#切换到h5页面
#          
        print self.driver.current_context#打印当前context
#         print driver.page_source#d打印当前页面源码
#         time.sleep(5)
#         self.find_element_by_name('未激活').click()
#         time.sleep(5)
#         self.driver.find_element_by_name('注册').click()
#         self.driver.find_element_by_name('请输入手机号').send_keys('15626513325')
#         self.driver.find_element_by_name('获取验证码').click()
#         self.driver.find_element_by_name('请输入验证码').send_keys('')#输入验证码
#         self.driver.find_element_by_id('com.jiufu.heyuanwanka:id/et_psd_numb').send_keys('cyj123')
#         pass
    
    def tearDown(self):  
        self.driver.quit() 
   


    