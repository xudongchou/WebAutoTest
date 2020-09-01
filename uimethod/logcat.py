"""
@project:code
@author:lenovo
@file:logcat.py
@ide:PyCharm
@time:2020/8/27 15:35
@month:八月
使用 logging模块进行二次封装的日志模块
"""
import logging
import os
class Log():
    def __init__(self):
        basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        log_dir = "/logs/"
        log_filepath = basedir + log_dir +'cc.log'
        self.logger = logging.getLogger('ATX')
        self.logger.setLevel(logging.DEBUG)

        fh = logging.FileHandler(log_filepath,encoding='utf-8',mode='a')
        fh.setLevel(logging.DEBUG)

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(filename)s - %(message)s')

        # formatter = logging.Formatter('%(asctime)s'
        #                               + ' - %(levelname)s'
        #
        #                               + ' - %(message)s' + ' _%(name)s' + ' - %(levelname)s' + ' - %(lineno)d' + ' - %(module)s' + ' - %(message)s')


        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
    def d(self, msg,*args, **kwargs):
        self.logger.debug(msg, *args, **kwargs)
        print(msg, *args, **kwargs)
    def i(self, msg, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)
        print(msg, *args, **kwargs)
    def w(self, msg, *args, **kwargs):
        self.logger.warning(msg, *args, **kwargs)
    def c(self, msg, *args, **kwargs):
        self.logger.critical(msg, *args, **kwargs)

    def e(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)