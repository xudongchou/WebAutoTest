"""
@project:code
@author:lenovo
@file:test_netease_login.py
@ide:PyCharm
@time:2020/8/27 11:04
@month:八月

"""
import unittest
from page.login import Login
from uimethod.uiauto import WebUiMethod
from uimethod .driverselect import SelectDriver
class Test_login(unittest.TestCase):
    def test_login(self):
        """
        登录新浪邮箱

        """


        Login.navigate_email(self)
        Login.input_username(self,"zhouxudong886@sina.com")
        Login.input_passwd(self,"zhouxudong325460")
        Login.click_btn(self)

if __name__ =="__main__":
    unittest.main()