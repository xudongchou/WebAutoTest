from uimethod.driverselect import SelectDriver
from uimethod.uiauto import WebUiMethod
from uimethod.helpers import Logger
driver=SelectDriver.mybrowser("firefox")
We=WebUiMethod
We.navigate(driver,"http://wwww.baidu.com")
We.wait(8)
We.webEdit(driver,"//*[@id='kw']","豆瓣")
We.wait(3)
We.webButton(driver,"//*[@id='su']")
We.wait(5)
We.screen_shot(driver)
We.wait(8)
We.exit(driver)
print("关闭浏览器")
# # We.wait(7)
# # path="D:\\code\\webauto\\ScreenShot"
# # We.screen_shot(driver,path)
