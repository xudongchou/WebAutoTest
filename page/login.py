"""
@project:code
@author:lenovo
@file:login.py
@ide:PyCharm
@time:2020/8/27 10:34
@month:八月

"""

from uimethod import driverselect
from uimethod.uiauto import WebUiMethod
from uimethod.helpers import Logger
from uimethod.driverselect import SelectDriver
from uimethod.logcat import Log
import unittest
log = Log()
driver = SelectDriver.mybrowser("firefox")
class Login():
   def __init__(self):
      self.username_element = "//*[@id='freename']"
      self.passwd_element = "//*[@id='freepassword']"
      self.btn_element = "//*[@class='loginRegisterSubmit']/a[1]"
   def navigate_email(self):
       Logger.logger.info("打开网易邮箱登录页：")
       WebUiMethod.navigate(driver,"https://mail.sina.com.cn/")
       WebUiMethod.wait(5)
   def input_username(self,str):
       Logger.logger.info("请输入用户名：")
       WebUiMethod.webEdit(driver,xpath=self.username_element,inputstring=str)
       # WebUiMethod.webEdit(driver, "//*[@id='freename']", inputstring=str)
   def input_passwd(self,str):
       Logger.logger.info("请输入密码：")
       WebUiMethod.webEdit(driver,xpath=self.passwd_element, inputstring=str)
       # WebUiMethod.webEdit(driver, "//*[@id='freepassword']", inputstring=str)
   def click_btn(self):
       Logger.logger.info("点击登录按钮")
       WebUiMethod.wait(2)
       WebUiMethod.webButton(driver,xpath=self.btn_element).click()
       # WebUiMethod.webButton(driver,"/html/body/div[1]/div/div[2]/div/div/div[4]/div[1]/div[1]/div[7]/div[1]/a[1]").click()
       # driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div[4]/div[1]/div[1]/div[7]/div[1]/a[1]").click()
       # driver.find_element_by_class_name("loginBtn11")
       WebUiMethod.wait(5)
       Logger.logger.info("开始截图")
       WebUiMethod.screen_shot(driver)
       WebUiMethod.wait(5)
       WebUiMethod.exit(driver)
       # driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div[4]/div[1]/div[1]/div[7]/div[1]/a[1]").click()

