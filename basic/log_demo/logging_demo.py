#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
 @File: logging_demo.py
 @author: ginger 
 @software: PyCharm  
 @time: 18-2-8 上午8:40
 @desc:
 @source: https://blog.csdn.net/yypsober/article/details/51800120
 https://www.cnblogs.com/kill-signal/archive/2012/10/10/2718002.html
 https://www.cnblogs.com/cp-vbird/archive/2016/07/06/5646876.html
"""
import logging
import logging.config


def getLogging():
    return logging.getLogger("logger_test1")

def getLogging2():
    return logging.getLogger("logger_test2")

def getLogging3():
    return logging.getLogger("logger_root")


logging.config.fileConfig('log_demo.conf')  # 仅第一次读取有效
logger1 = getLogging()
logger2 = getLogging2()
# logger3 = getLogging2()
logger1.debug("this is an test1 debug!")
logger2.debug("this is test2 debug")
logger1.info("this is an test1! info ")
logger2.info("this is test2 info ")
logger1.warning("this is an test1! warn")
logger2.warning("this is test2 warn")
logger1.error("this is an test1!error")
logger2.error("this is test2 error")
# logger3.info("this is root")
