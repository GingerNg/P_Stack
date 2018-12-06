#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
 @desc:
 @author: ginger
 @software: PyCharm
 @time: 17-11-3 上午9:47
Py4J - A Bridge between Python and Java
"""

from pyspark.sql import SQLContext
from pyspark import SparkContext, SparkConf


# spark读取hdfs
conf = SparkConf().setAppName("demo_pyspark_hdfs")
sc = SparkContext(conf=conf)
sc.setLogLevel("info")
testFile = sc.textFile("hdfs://XX.XX.XX.XX:9000/user/XXX/test")
lines = testFile.collect()
sc.stop()
for line in lines:
    print (line)