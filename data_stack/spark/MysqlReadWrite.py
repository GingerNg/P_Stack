#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
 @author: ginger 
 @software: PyCharm  
 @time: 17-11-3 上午9:47
 @desc:
"""

from pyspark.sql import SQLContext
from pyspark import SparkContext
# spark 读取mysql
sc = SparkContext("local", "Simple App")
sqlContext = SQLContext(sc)
dataframe_mysql = sqlContext.read.format("jdbc").options(url="jdbc:mysql://127.0.0.1:3306/spark_db", driver="com.mysql.jdbc.Driver", dbtable="spark_table", user="root", password="root").load()
dataframe_mysql.show()