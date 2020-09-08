#!/usr/bin/python
# -*- coding:utf-8 -*-
"""


https://www.cnblogs.com/yyds/p/6901864.html
日志级别:
DEBUG
INFO
NOTICE
WARNING
ERROR
CRITICAL
ALERT
EMERGENCY
"""
import logging

# configue format methods by logging.basicConfig
# 在配置日志器日志级别的基础上，在配置下日志输出目标文件和日志格式
# logging.basicConfig()函数一次性的简单配置工具(第二次使用时不再起作用)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='myapp.log_demo',
                    filemode='w')

# define StrenmHanddler, set level >=INFO to print
#################################################################################################
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
#################################################################################################


logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')
