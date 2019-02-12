# -*-coding:utf-8 -*-
from selenium import webdriver
import time
import pyautogui as pag
import datetime
from retry import retry
import logging

logging.basicConfig()
@retry(tries=10, delay=1,jitter=1)
def buy():
    driver.find_element_by_xpath('//*[@id="J_juValid"]/div[1]/a').click()#点击立即购买
    pag.scroll(-900)
    driver.find_element_by_class_name('go-btn').click()#提交订单   

def login(url):
    #打开网页
    driver.get(url)
    driver.maximize_window()
    driver.find_element_by_xpath('//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]').click()#点击请登录
    #手动扫码登录
    time.sleep(10)     
    pag.scroll(-600)
    time.sleep(2)   
    driver.find_element_by_xpath('//*[@id="J_isku"]/div/dl[1]/dd/ul/li[2]/a/span').click()#选择尺码
    time.sleep(2)  
    monitor()

def monitor():
    interval = 0.1
    last = 1800
    elapse = 0
    while elapse < last:
        t =  datetime.datetime.now()
        now = t.strftime('%Y-%m-%d %H:%M:%S')
        print '现在时间是 %s' % (now)
     
        if now == '2018-11-11 10:00:00':
            print '立即购买！'
            buy()
            break
        else:
            print '还没开始呢，再等等吧！'
        time.sleep(interval)
        elapse += interval

driver = webdriver.Chrome()
url='https://item.taobao.com/item.htm?id=581169694730'
login(url)
