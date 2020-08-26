"""
@project:code
@author:lenovo
@file:test_baidu.py
@ide:PyCharm
@time:2020/8/26 16:12
@month:八月

"""
from uimethod.driverselect import SelectDriver
from uimethod.uiauto import WebUiMethod
from uimethod.helpers import Logger
import unittest
class Test_baidu(unittest.TestCase):

    def test_1(self):
        """
        打开百度，搜索豆瓣

        """
        driver = SelectDriver.mybrowser("firefox")
        print(driver.name)
        We = WebUiMethod
        We.navigate(driver, "http://wwww.baidu.com")
        We.wait(8)
        We.webEdit(driver, "//*[@id='kw']", "豆瓣")
        We.wait(3)
        We.webButton(driver, "//*[@id='su']").click()
        We.wait(10)
        We.screen_shot(driver)
        We.wait(8)
        We.exit(driver)
        print("关闭浏览器")
