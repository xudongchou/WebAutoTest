from selenium.webdriver import Firefox
from selenium.webdriver import Ie
from selenium.webdriver import Chrome
from selenium.webdriver.ie.options import Options
from uimethod.helpers import Logger
from setting.driverconfig import FIREFOX_DIR
from  setting.driverconfig import IE_DIR
from  setting.driverconfig import CHROME_DIR
"""
对三种常用的浏览器的驱动进行了封装，输入浏览器的名字即可自由切换webdriver的驱动
firefox 火狐浏览器
chrome  谷歌浏览器
ie      ie浏览器
本类 依赖于配置文件driverconfig.py 里面的路径可以根据自身需要进行配置
"""
class SelectDriver:
    def mybrowser(browser):
        driver=None
        if(browser.lower()=="firefox"):
            driver =Firefox(executable_path=FIREFOX_DIR)
            Logger.logger.info("启动火狐浏览器,请稍等")
            driver.maximize_window()
        if browser.lower()=="chrome":
            driver=Chrome(executable_path=CHROME_DIR)
            Logger.logger.info("启动谷歌浏览器,请稍等")
            driver.maximize_window()
        if browser.lower()=="ie":
           op=Options()
           op.set_capability(op.IGNORE_PROTECTED_MODE_SETTINGS,True)
           driver=Ie(executable_path=IE_DIR)
           Logger.logger.info("启动ie浏览器,请稍等")
           driver.maximize_window()
        return driver


