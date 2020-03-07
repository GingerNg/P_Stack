#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
使用mongodb存储文件，可以使用两种方式，一种是像存储普通数据那样，将文件转化为二进制数据存入mongodb，
另一种使用gridfs  适用于大尺寸文件
"""
import sys
from imp import reload
reload(sys)
from pymongo import MongoClient
import gridfs
from io import BytesIO


def file_save(file_path):
    try:
        fin = open(file_path, "rb")
        img = fin.read()
        data = BytesIO(img)
        fin.close()
        conn = MongoClient('XX.XX.XX.XX', 8003)
        db = conn.mydb
        imgput = gridfs.GridFS(db,'XX')
        insertimg = imgput.put(data)
        print (insertimg)
    except Exception as e:
        print (e)
        sys.exit(1)
    # finally:
    #     imgput.close()  todo

import bson.binary
def insertFile(file_path):
    """
    insert file whose size < 16M into mongodb
    :param file_path:
    :return:
    """
    try:
        fin = open(file_path, "rb")
        img = fin.read()
        data = BytesIO(img)
        fin.close()
        conn = MongoClient('XX.XX.XX.XX', 8003)
        db = conn.mydb
        coll = db.test_set
        with open(file_path, 'rb') as myimage:
            content = BytesIO(myimage.read())
            coll.save(dict(
                content=bson.binary.Binary(content.getvalue()),
                filename='testJs',
                file_format="js"
            ))
    except Exception as e:
        print (e)
        sys.exit(1)
    # finally:
    #     imgput.close()  todo

def file_read():
    """
    从mongo中读文件  gridfs
    :return:
    """
    try:
        # fin = open(file_path, "rb")
        # img = fin.read()
        # data = StringIO(img)
        # fin.close()
        conn = MongoClient('XX.XX.XX.XX', 8003)
        db = conn.mydb
        files = db.test_set.files
        print('sum:', files.count())
    except Exception as e:
        print (e)
        sys.exit(1)

def file_read_binary(file_path):
    """
    从mongo中读文件，文件为二进制
    :return:
    """
    try:
        fin = open(file_path, "wb")
        # img = fin.read()
        # data = StringIO(img)
        # fin.close()
        conn = MongoClient('XX.XX.XX.XX', 8003)
        db = conn.mydb
        files = db.test_set
        res = files.find_one({"filename":"testJs"})
        print (res)
        content = res['content']

        fin.write(content)
        # print('sum:', files.count())
        # insertimg = imgput.put(data)
        # print insertimg
    except Exception as e:
        print (e)
        sys.exit(1)




if __name__=="__main__":
    # file_save("testJs.html")
    file_read_binary("testJs_mongo.html")
    # insertFile("testJs.html")