"""
@project:code
@author:lenovo
@file:send_email.py
@ide:PyCharm
@time:2020/8/28 15:29
@month:八月

"""
import yagmail
from setting.emailconfig import To_Users,Email_Host,Username,Passwd
import os
class Send_Email:
    def send_email(self):
        report_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/reports/"
        report_name = '自动化报告.html'
        repfile = report_dir + report_name
        report_file = eval(repr(repfile).replace(r'\\','/'))
        report_list = os.listdir(report_dir)
        if report_name in report_list:
            ya = yagmail.SMTP(user=Username,password=Passwd,host=Email_Host)
            body ='''<!DOCTYPE html><html><head> </head><body><div style="width:auto;height:auto; top:auto;><p id="class1">各位亲：</p><p id="class2" style="text-indent: 2em;">附件自动化为测试报告，请审阅。</p></div></body></html> '''
            print(body)
            subject = '自动化测试报告'
            ya.send(to=To_Users,subject=subject,contents=body,attachments=repfile)

if __name__ == "__main__":
    s = Send_Email()
    s.send_email()