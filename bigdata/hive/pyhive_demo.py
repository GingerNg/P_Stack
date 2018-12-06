#!/usr/bin/python
# coding=utf-8

"""
 @File: pyhive_demo.py
 @author: ginger 
 @software: PyCharm  
 @time: 17-11-14 下午3:33
 @desc:
 http://blog.csdn.net/gamer_gyt/article/details/52564335  python三种方式连接hive
 @bug:sasl/saslwrapper.h:22:23: fatal error: sasl/sasl.h: 没有那个文件或目录:
 @solution: https://stackoverflow.com/questions/22838752/hadoop-python-client-driver-for-hiveserver2-fails-to-install
"""
from pyhive import hive

# select insert alter delete


SELECT_HSQL = """
SELECT * FROM %s
"""


def selectFromTable(hivecConn, tableName):
    cnt = 0
    result = {}
    hql = SELECT_HSQL % (tableName)
    cursor = hivecConn.cursor()
    cursor.execute(hql)
    rows = cursor.fetchall()
    return rows
    # for row in cursor.fetchall():
    #     result[cnt] = row[0]
    #
    # cursor.close()
    # return result

if __name__ == '__main__':
    hiveConn = hive.connect('XX.XX.XX.XX', 10000)
    # print (hiveConn.getDB())
    result = selectFromTable(hiveConn, 'new_table')
    print (result)



