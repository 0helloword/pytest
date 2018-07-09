# -*- coding: utf-8 -*-

#注册
def regist(driver):
    driver.find_element_by_name('注册').click()
    driver.find_element_by_name('请输入手机号').send_keys('15626513325')
    driver.find_element_by_name('获取验证码').click()
    driver.find_element_by_name('请输入验证码').send_keys('')#输入验证码
    driver.find_element_by_id('com.jiufu.heyuanwanka:id/et_psd_numb').send_keys('cyj123')
    driver.hide_keyboard()#隐藏键盘
    driver.find_element_by_name('确定').click()
    print 'regit success'
pass