"""
@project:code
@author:lenovo
@file:send_email.py
@ide:PyCharm
@time:2020/8/28 15:29
@month:八月

"""
import yagmail
from setting.emailconfig import To_Users,Host,Username,Passwd
import os
def send_email():
    report_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\reports"
    report_name = '自动化报告.html'
    report_file = report_dir + report_name
    report_list = os.listdir(report_dir)
    print(report_list)
    print(os.listdir(report_dir))
    print(report_file)
    print(report_name)
    if report_name in report_list:
        ya = yagmail.SMTP(user=Username,password=Passwd,Host=Host)
        body = '这是自动化测试报告'
        subject = '自动化测试报告'
        ya.send(to=To_Users,subject=subject,contents=[body,report_file])
if __name__ == "__main__":
    send_email()