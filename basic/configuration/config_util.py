# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
http://blog.csdn.net/qq_21398167/article/details/48005003

https://www.cnblogs.com/franknihao/p/7300752.html
"""
import configparser
import string
import os
import sys

file_name = "test.conf"
cf = configparser.ConfigParser()

cf.read(file_name)

#return all section
secs = cf.sections()
print ('sections:', secs)

opts = cf.options("datastorage")
print ('options:', opts)

kvs = cf.items("datastorage")
print ('datastorage:', kvs)

#read by type
db_host = cf.get("datastorage", "db_host")
db_port = cf.getint("datastorage", "db_port")
db_user = cf.get("datastorage", "db_user")
db_pass = cf.get("datastorage", "db_pass")

#read int
threads = cf.getint("concurrent", "thread")
processors = cf.getint("concurrent", "processor")

print ("db_host:", db_host)
print ("db_port:", db_port)
print ("db_user:", db_user)
print ("db_pass:", db_pass)

print ("thread:", threads)
print ("processor:", processors)


#modify one value and write to file
cf.set("datastorage", "db_pass", "xgmtest")
cf.write(open("test.conf", "w"))

print (" using ConfigObj")
from configobj import ConfigObj
config = ConfigObj(file_name)
#
value1 = config["concurrent"]['processor']
print (value1)
#
section1 = config['datastorage']
value3 = section1['db_port']
#
# you could also write
# value3 = config['section1']['keyword3']
# value4 = config['section1']['keyword4']
