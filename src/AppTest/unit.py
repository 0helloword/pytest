# -*- coding: utf-8 -*-

import unittest
import time
from appium import webdriver
from appium.webdriver.mobilecommand import MobileCommand

class Test(unittest.TestCase):
#     @classmethod
    def set_up(self):
        cap = {}
        cap['platformName'] = 'Android'
        cap['platformVersion'] = '5.1'
        cap['deviceName'] = 'EATGNJCYBADAGEU8'
#         cap['noReset'] = 'noReset'  #选择fullreset会卸载APP重新安装
        cap['appPackage'] = 'com.jiufu.heyuanwanka'
        cap['appActivity'] = '.ui.activity.StartLoadingActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',cap)



#     def test_regist(self):
#         self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": "NATIVE_APP"})#切换到h5页面
#         time.sleep(5)
#         self.driver.find_element_by_name('未激活').click()
#         self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": ""})#切换到APP
#         time.sleep(2)
#         self.driver.find_element_by_name('注册').click()
#         self.driver.find_element_by_name('请输入手机号').send_keys('15626513325')
#         self.driver.find_element_by_name('获取验证码').click()
#         self.driver.find_element_by_name('请输入验证码').send_keys('')
#         self.driver.find_element_by_id('com.jiufu.heyuanwanka:id/et_psd_num').send_keys('cyj123')
#         self.driver.hide_keyboard()#隐藏键盘
#         self.driver.find_element_by_name('确定').click()
#         print("test_regist success!!!")
           
    def test_login(self):
        time.sleep(5)  
        print self.driver.contexts#打印当前页面的所有context [u'NATIVE_APP', u'WEBVIEW_com.jiufu.heyuanwanka']
        print self.driver.page_source
        self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": "WEBVIEW_com.jiufu.heyuanwanka"})#切换到h5页面    
        self.driver.find_element_by_name('未激活').click()  
        self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": "NATIVE_APP"})#切换到APP  
        self.driver.find_element_by_name('手机号码/世纪佳缘账号').send_keys('15626513325')
        self.driver.find_element_by_name('登录密码').send_keys('cyj123')
        self.driver.hide_keyboard()#隐藏键盘
        self.driver.find_element_by_name('登录').click()
        print("test_login success!!!")
    
#     @classmethod
    def tearDown(self):
        self.driver.quit()
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
#     unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite) 