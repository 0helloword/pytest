# -*-coding:utf-8-*-

from selenium import webdriver

class test1():
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.baseurl="http://192.168.78.243:8080/initLogin"
        self.driver.maximize_window()   
        
    def dengLu(self):
        browser=self.driver
        browser.get(self.baseurl)
        browser.find_element_by_id("username").send_keys("998866")
        browser.find_element_by_id("password").send_keys("cyj123")
        browser.find_element_by_id("loginButton").click()        
        
#   该方法用来确认元素是否存在，如果存在返回flag=true，否则返回false        
    def isElementExist(self,element):
        flag=True
        browser=self.driver
        try:
            browser.find_element_by_class_name(element)
            return flag
        except:
            flag=False
            return flag
      
            
if __name__ == "__main__":
    user1=test1()
    user1.setUp()
    user1.dengLu()
    #调用isElementExist方法，判断元素是否存在
    flag=user1.isElementExist('ui-dialog-title')         
        
    if flag:
        print("有弹窗")
    else:
        print("没有弹框")
    pass

