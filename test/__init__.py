"""
@project:code
@author:lenovo
@file:__init__.py
@ide:PyCharm
@time:2020/9/1 18:24
@month:九月

"""
#将根目录加入sys.path中,解决命令行找不到包的问题
import sys
import os
sys.path.append("..")
# Base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# import_dir = Base_dir+"/setting/emailconfig.py"
# sys.path.append(Base_dir)
# sys.path.extend(Base_dir)