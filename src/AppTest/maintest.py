# -*- coding: utf-8 -*-

from appium import webdriver
import time
from appium.webdriver.mobilecommand import MobileCommand
import login
import location
# import regist

desired_caps = {
        'platformName': 'Android',
        'deviceName': 'EATGNJCYBADAGEU8',
        'platformVersion': '5.1',
        'appPackage': 'com.jiufu.heyuanwanka',
        'appActivity': '.ui.activity.StartLoadingActivity',
    }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)#启动APP

# print driver.contexts#打印当前页面的所有context

driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": "NATIVE_APP"})#切换到h5页面
# print driver.current_context#打印当前context
# print driver.page_source#d打印当前页面源码
time.sleep(25)
driver.find_element_by_name('立即激活').click()

#注册
# regist.regist(driver)

#登录
login.login(driver)

#额度分期
time.sleep(5)
# print driver.page_source
location.taptest(driver)#使用相对坐标定位额度分期按键
time.sleep(2)
# driver.find_element_by_class_name('cash-input').clear()
time.sleep(2)
# driver.find_element_by_android_uiautomator('new UiSelector().descriptionStartsWith("500~")').send_keys('1000')
# time.sleep(2)
# driver.hide_keyboard()
# driver.swipe(866, 989, 977, 991, 1)#请选择下拉框
# time.sleep(2)
# driver.find_element_by_android_uiautomator('new UiSelector().description("个人消费")').click()
# time.sleep(2)
 
driver.swipe(42,1062,96,1272,1) #勾选协议
time.sleep(2)
driver.find_element_by_name('查看费用详情').click()
print '额度分期第一页面填写成功'
time.sleep(3)
 
location.swipe_up(driver)
driver.swipe(114,1419,168,1530,1)#勾选协议
# # driver.find_element_by_css_selector('i.hyiconfont.hyicon-circle.fee-checkout').click()
time.sleep(2)
driver.find_element_by_name('下一步').click()
print '额度分期第二页面填写成功'
time.sleep(2)
driver.find_element_by_name('我已阅读并确认').click()
print '额度分期第三页面填写成功'   
time.sleep(3)
 
print driver.page_source
time.sleep(3)
driver.find_element_by_name('1').click()
driver.find_element_by_name('2').click()
driver.find_element_by_name('3').click()
driver.find_element_by_name('1').click()
driver.find_element_by_name('2').click()
driver.find_element_by_name('3').click()
print '交易密码输入成功'
     
time.sleep(5)
driver.find_element_by_name('回到主页').click()
print '额度分期下单成功'
