#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
 @File: handler_demo.py
 @author: ginger 
 @software: PyCharm  
 @time: 18-2-7 下午3:43
 @desc: 
"""
"""
组件: Logger 日志等级 -> Filter,--> Handler  --> Formatter
"""
import logging
import logging.handlers
import datetime
# logging.basicConfig(level=logging.DEBUG)  # 默认是warn?
logger = logging.getLogger('mylogger')
print (logger.name)
logger.setLevel(logging.INFO)

dev_handler = logging.handlers.TimedRotatingFileHandler('dev.log', when='midnight', interval=1, backupCount=7)
dev_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

prod_handler = logging.FileHandler('prod.log')
prod_handler.setLevel(logging.ERROR)
prod_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

# logger.addHandler(dev_handler)
logger.addHandler(prod_handler)

logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')

test_logger = logging.getLogger("test")
stream_hander = logging.StreamHandler()
stream_hander.setLevel(logging.INFO)
test_logger.addHandler(stream_hander)
test_logger.info("this is stream log")


k = 1
project = None


def pppp():
    for k, x in {"1":"2","2":"3"}.items():
        if x:
            if project:
                return k == project
            else: return True

iters = [iter(x) for k, x in {"1":"2","2":"3"}.items()
         if x and (k == project if project  else True)]  # 如果x存在,且x==project
print (type(iters))
for x in iters:
    for y in x:
        print (y)
    

print (iter([1,2,3,4]))  # listiterator object

print ([x**2 for x in range(10)])

def show(x):
    print (x)
print ([show(x) for k, x in {"1":"2","2":"3"}.items()])

if x:
    print ("fal")
if None:
    print ("none")
else:
    print ("es")



# python click 命令行工具