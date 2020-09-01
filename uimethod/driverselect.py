"""
对三种常用的浏览器的驱动进行了封装，输入浏览器的名字即可自由切换webdriver的驱动
firefox 火狐浏览器
chrome  谷歌浏览器
ie      ie浏览器
本类 依赖于配置文件driverconfig.py 里面的路径可以根据自身需要进行配置
@Firefox_option :设置火狐浏览器模式
@Chrome_option:设置谷歌浏览器模式
@op:设置ie浏览器模式
使用add——argument('headless') 使用浏览器无头模式，以便浏览器在命令行下运行
"""
from selenium.webdriver import Firefox
from selenium.webdriver import Ie
from selenium.webdriver import Chrome
from selenium.webdriver.ie.options import Options
from uimethod.helpers import Logger
from setting.driverconfig import FIREFOX_DIR
from  setting.driverconfig import IE_DIR
from  setting.driverconfig import CHROME_DIR
from selenium.webdriver.chrome.options import Options as chop
from selenium.webdriver.firefox.options import Options as fireop
from selenium.webdriver.ie.options import Options as  ieop
import platform
class SelectDriver:
    def mybrowser(browser):
        driver=None
        str1 = platform.platform()
        op = str1.split("-")[0]
        if op == "Linux":
            if(browser.lower()=="firefox"):
                Firefox_option = fireop()
                fireop.add_argument('--headless')
                driver =Firefox(executable_path=FIREFOX_DIR,firefox_options=Firefox_option)
                Logger.logger.info("启动火狐浏览器,请稍等")
                driver.maximize_window()
            if browser.lower()=="chrome":
                Chrome_option=chop()
                Chrome_option.add_argument('--headless')
                driver=Chrome(executable_path=CHROME_DIR,chrome_options=Chrome_option)
                Logger.logger.info("启动谷歌浏览器,请稍等")
                driver.maximize_window()
            if browser.lower()=="ie":
               op=Options()
               op.add_argument('--headless')
               op.set_capability(op.IGNORE_PROTECTED_MODE_SETTINGS,True)
               driver=Ie(executable_path=IE_DIR,ie_options=op)
               Logger.logger.info("启动ie浏览器,请稍等")
               driver.maximize_window()
        else:
            if (browser.lower() == "firefox"):
                driver = Firefox(executable_path=FIREFOX_DIR)
                Logger.logger.info("启动火狐浏览器,请稍等")
                driver.maximize_window()
            if browser.lower() == "chrome":
                driver = Chrome(executable_path=CHROME_DIR)
                Logger.logger.info("启动谷歌浏览器,请稍等")
                driver.maximize_window()
            if browser.lower() == "ie":
                op.set_capability(op.IGNORE_PROTECTED_MODE_SETTINGS, True)
                driver = Ie(executable_path=IE_DIR)
                Logger.logger.info("启动ie浏览器,请稍等")
                driver.maximize_window()
        return driver


