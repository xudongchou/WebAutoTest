"""
@project:code
@author:lenovo
@file:logcat.py
@ide:PyCharm
@time:2020/8/27 15:35
@month:八月
封装web自动化的常用的元素使用方法，本类依赖于 driverselect的SelectDriver类
使用时请引入此类

"""
import os
from datetime import datetime
from time import sleep
from  selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchElementException
from  selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import select
from selenium.common.exceptions import JavascriptException
from uimethod.helpers import Logger
from uimethod.driverselect import SelectDriver
import platform
import socket
from urllib3.exceptions import MaxRetryError,NewConnectionError
from selenium.webdriver.remote.command import Command
class WebUiMethod:
    def webEdit(driver,xpath,inputstring):
        try:
           webEdit=driver.find_element_by_xpath(xpath)
           webEdit.clear()
           webEdit.send_keys(inputstring)
        except NoSuchElementException:
              Logger.logger.info("页面上没有输入框")
        except ElementNotVisibleException :
              Logger.logger.info("该页面上有多个输入框")

    def webButton(driver,xpath):
        try:
            webButton=driver.find_element_by_xpath(xpath)
            return webButton
        except NoSuchElementException :
            Logger.logger.info("页面上使用xpath没有定位到按钮")
            # try:
            #     webButton=driver.find_element_by_class_name(xpath)
            #     return webButton
            # except NoSuchElementException:
            #     Logger.logger.info("页面上使用classname没有定位到按钮")
            #     try:



        except ElementNotVisibleException :
            Logger.logger.info("该页面上有多个按钮")






    def webLink(driver,xpath):
        try:
            webLink=driver.find_element_by_xpath(xpath)
            return webLink
        except NoSuchElementException :
            Logger.logger.info("页面上没有此链接")
        except ElementNotVisibleException :
            Logger.logger.info("该页面上有多个链接")


    def hover(driver,xpath):
        try:
            element=driver.find_element_by_xpath(xpath)
            action=ActionChains(driver)
            action.move_to_element(element).perform()
        except NoSuchElementException :
            Logger.logger.info("页面上没有悬停对象")
        except ElementNotVisibleException :
            Logger.logger.info("页面上有多个悬停对象")
    def switchTowindow(driver,title):
        try:
            current_handle=driver.current_window_handle()
            handles=driver.window_handles()
            for handle in handles:
                if handle==current_handle:
                    continue
                else:
                    driver.switch_to.window(handle)
                    if title in driver.title:
                        break
                    else:
                        continue
        except NoSuchElementException :
            Logger.logger.info("没有找到窗口")
    def webList(driver,xpath):
        try:
            se=select.Select(xpath)
            return se
        except NoSuchElementException :
            Logger.logger.info("下拉框不存在")
        except ElementNotVisibleException :
            Logger.logger.info("存在多个下拉框")
    def webRadio(driver,xpath):
        try:
            radios=driver.find_elements_by_xpath(xpath)
            return radios
        except NoSuchElementException:
            Logger.logger.info("您输入的xpath有误，请检查修正")
        except IndexError:
            Logger.logger.info("单选按钮不存在")
        except ElementNotVisibleException:
            Logger.logger.info("存在多个下拉框")
    def webCheckbox(driver,xpath):
        try:
            checkboxs=driver.find_elements_by_xpath(xpath)
            return checkboxs
        except NoSuchElementException:
            Logger.logger.info("您输入的xpath有误，请检查修正")
        except IndexError:
            Logger.logger.info("多选按钮不存在")
        except ElementNotVisibleException:
            Logger.logger.info("存在多个多选按钮")
    def upLoad(driver,xpath):
        try:
            file=driver.find_element_by_xpath(xpath)
            return file
        except NoSuchElementException:
            Logger.logger.info("上传文件的控件不存在")
        except ElementNotVisibleException:
            Logger.logger.info("存在多个上传文件的控件")
    def executeJS(driver,jsString):
        try:
            driver.execute_script(jsString)
        except JavascriptException:
            Logger.logger.info("输入的js脚本有误")

    def switchToIframe(driver,xpath):
        Logger.logger.info("---------开始切换框架---------")
        try:
            iframe=driver.find_element_by_xpath(xpath)
            driver.switch_to.frame(iframe)
        except NoSuchElementException:
            Logger.logger.info("您输入的xpath有误，请检查修正")
    def outOfIframe(driver):
        Logger.logger.info("---------跳出框架-------")
        return driver.switch_to.default_content()
    def switchToAlert(driver):
        alert=driver.switch_to.alert()
        return alert
    def title(driver):
        title=driver.title()
        return title

    def wait(seconds):
        sleep(seconds)
    def exit(driver):
        driver.quit()
        str1 = platform.platform()
        op=str1.split("-")[0]
        Logger.logger.info("关闭浏览器驱动并关闭标签页")
        """
        sleep(5)
        if op=="Windows":
            if driver.name=="firefox":
                os.system("taskkill /F /IM  firefox.exe")
            elif driver.name=="chrome":
                os.system("taskkill /F /IM  chrome.exe")
            elif driver.name=="ie":
                os.system("taskkill /F /IM  iexplore.exe")
            sleep(3)
        elif op=="Linux":
            if driver.name=="firefox":
                os.system("killall -s KILL -I -v firefox")
            elif driver.name=="chrome":
                os.system("killall -s KILL -I -v chrome")
            else:
                Logger.logger.info("您的浏览器不适合在linux系统")
            sleep(3)
        elif op=="Darwin":
            if driver.name=="firefox":
                os.system("killall -s KILL -I -v firefox")
            elif driver.name=="chrome":
                os.system("killall -s KILL -I -v chrome")
            else:
                Logger.logger.info("您的浏览器不适合在mac系统")
            sleep(3)
        """
        Logger.logger.info("关闭浏览器")
    def navigate(driver,url):
       driver.get(url)
       Logger.logger.info("打开用户指定的url:"+ url)
    def cookie(driver,cook):
        driver.add_cookie(cook)
    def refresh(driver):
        Logger.logger.info("-------开始刷新页面------")
        driver.refresh()
#web浏览器的截图方法
    def screen_shot(driver):
         '''
         web浏览器的截图方法,以事件发生的时间点为图片的名字方便查找原因 
         '''
         nowtime=datetime.now()
         stringtime=datetime.strftime(nowtime,"%Y%m%d%H%M%S")
         basedir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
         dir_name="/ScreenShot/"
         # filename=stringtime+".png"
         path_dir = basedir + dir_name
         #path_file = os.path.join(path_dir, filename)
         Logger.logger.info("----------开始截图--------")
         driver.get_screenshot_as_file(path_dir+stringtime+'.png')
         WebUiMethod.wait(5)
         dirs=os.listdir(path_dir)
         if stringtime+".png" in dirs:
             Logger.logger.info("------截图成功,位置在ScreenShot目录------")
         else:
             Logger.logger.info("------截图失败,请检查程序------")
    def get_driver_status(driver):
        try:
           driver.execute(Command.STATUS)
           return "Alive"
        except(socket.error,MaxRetryError,NewConnectionError):
            return "Dead"
