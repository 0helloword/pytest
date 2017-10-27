# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select

class test():

    def __init__(self):
        print '开始测试'
    
    def openbrower(self,url):
        driver.get(url)  
        driver.maximize_window()
        pass
         
    def login(self,username,password):
        driver.find_element_by_id("username").send_keys(username)
        driver.find_element_by_id("password").send_keys(password)
        driver.find_element_by_id("loginButton").click()
        time.sleep(3)  
        pass
     
    def appquery(self):
        driver.find_element_by_xpath('//li[3]/a/span').click()
        time.sleep(2)
        driver.find_element_by_id('idParam').send_keys('35442701')
        time.sleep(2)
        driver.find_element_by_css_selector('button.btn.btn-primary').click() 
        time.sleep(2)    
        pass  
    
    def ManualAudit(self):
        driver.find_element_by_xpath('//li[4]/a/span').click()
        time.sleep(2)
        driver.find_element_by_link_text('审核分单（POS）').click()
        time.sleep(2)
        driver.find_element_by_name('id').send_keys('35441918')
        driver.find_element_by_css_selector('button.btn.blue-madison').click()
        time.sleep(2)
        driver.find_element_by_name('ids').click()
        select=Select(driver.find_element_by_tag_name("select"))
        select.select_by_visible_text('xiaola')
        time.sleep(2)
        driver.find_element_by_xpath("//button[@onclick='validateAssign()']").click()
        pass
    
driver = webdriver.Chrome() 
user1=test()
user1.openbrower('http://123.57.39.68:7778/OC/initLogin')
user1.login('999111','cyj123')
user1.appquery()
user1.ManualAudit()    
driver.close()  
driver.quit() 

if __name__ == '__main__':
    pass
    