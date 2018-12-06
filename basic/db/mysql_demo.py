#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
mysql 安装使用教程：
http://www.cnblogs.com/liuchangchun/p/4099003.html

需安装Mysql-python(Python interface to MySQL)

'''

import pymysql as MySQLdb
def get_conn(host='XX.XX.XX.XX>XX',port=3306,user='XXX' ,password='XXX',db='test'):
    return MySQLdb.connect(
        host=host,
        port=3306,
        user=user,
        passwd=password,
        db=db,
    )
"""
mysql CRUD
"""

'''
demo
'''
if __name__=='__main__':
    conn = MySQLdb.connect(
        host='XX.XX.XX.XX',
        port=3306,
        user='XXX',
        passwd='XX',
        db='test',
    )
    cursor = conn.cursor()  # 创建游标

    # 3、设置输入输出的字符编码以及自动提交
    cursor.execute('set names utf8')
    cursor.execute('set autocommit = 1')  # 0:false   1:true

    # 4、编写sql语句：crud
    # sql  = "insert into tb_user (name, pwd) values('zlc','123456')"  #增
    # sql  = "insert into tb_user (name, pwd) values('zlc_1','123456')"  #增
    # sql = "delete from tb_user where id={0}".format(2)   #删
    name = "'张三'"
    age = 111
    update_sql = "update teacher set age=%s where name = %s"  #改
    sql = 'select * from teacher'

    print (update_sql % (age, name))
    cursor.execute(update_sql % (age, name))
    # 5、执行sql并且得到结果集
    cursor.execute(sql)

    # 得到结果集有三种方式：全部 cursor.fetchall()    单个 cursor.fetchone()  多条 cursor.fetchmany(n)
    result = cursor.fetchall()
    for i in range(len(result)):
        print (result[i][0])
    # print(result)
    # print type(result)
    # print len(result)

    # cursor.execute(
    #     'create table user (id varchar(20) primary key, name varchar(20))')  #  _mysql_exceptions.OperationalError: (1050, "Table 'user' already exists")
    # cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])

    # 关闭游标和连接
    # cursor.rowcounts
    conn.commit()
    cursor.close()
