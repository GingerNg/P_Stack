# ­*­ coding: utf­8 ­*­
"""
@file: mongo_utils.py
@time: 2018/4/16 9:59
"""
import json
import os
from io import BytesIO
import sys

import bson
import pymongo
from pymongo import MongoClient


class MongoDao(object):
    def __init__(self, db_name, coll_name, client=None, url=None):
        if client is not None:
            self.collection = client[db_name][coll_name]
        elif url is not None:
            self.collection = self._get_coll(
                url=url, db=db_name, coll_name=coll_name)
        else:
            raise Exception("--")

    def _get_coll(self, url, db, coll_name):
        db = _get_db(url, db)
        return db[coll_name]

    def _get_db(self, url, db):
        client = _get_connection(url)
        return client[db]

    def _get_connection(self, url):
        return MongoClient(url)

    def count(self, filter={}):
        return self.collection.count(filter=filter)

    def search_one(self, filter={}):
        return self.collection.find_one(filter, no_cursor_timeout=True)

    def search(self, filter={}):
        return self.collection.find(filter, no_cursor_timeout=True)

    def insert_one(self, data={}):
        self.collection.insert_one(document=data)

    def update_one(self, filter={}, data={}, upsert=False):
        """
        upsert = update + insert
        :param filter:
        :param data:
        :param upsert:
        :param collection:
        :return:
        """
        self.collection.update_one(filter=filter, update={
                                   "$set": data}, upsert=upsert)

    def update_many(self, filter={}, update={}):
        self.collection.update_many(filter=filter, update=update)

    def pagination_search(self, filter={}, sort=[], skip=0, limit=10):
        """
        https://www.cnblogs.com/linhan/p/4248679.html
        :param filter:
        :return:
        """
        return self.collection.find(filter).sort(sort).\
            skip(skip=skip).limit(limit=limit)

    def search_upsert_one(self, filter={}, data={}, ids={}):
        """
        :param filter:
        :param data:
        :param ids: {"key1":1,"key2":0} 合并(1)or覆盖(0)
        :return:
        """
        if filter is not {}:
            record = self.collection.find_one(filter=filter)
        else:
            record = None
        if record:
            for id_key, v in ids.items():
                if id_key in record:
                    if v == 1 and isinstance(data[id_key], record[id_key]):
                        data[id_key] += record[id_key]
                    else:
                        data[id_key] = record[id_key]
            self.collection.update_one(filter=filter, update={"$set": data})
        else:
            # 插入
            self.collection.insert_one(document=data)


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
        # conn = MongoClient('10.101.12.23', 27017)
        conn = MongoClient('101.132.167.173', 8003)
        db = conn.mydb
        coll = db.test_set
        with open(file_path, 'rb') as myimage:
            content = BytesIO(myimage.read())
            coll.save(dict(
                content=bson.binary.Binary(content.getvalue()),
                filename=file_path.split(".")[0],
                file_format=file_path.split(".")[1]
            ))
    except Exception as e:
        print(e)
        sys.exit(1)
    # finally:
    #     imgput.close()  todo


def file_read_binary(plugin_name, file_path=None):
    """
    从mongo中读文件，文件为二进制
    :return:
    """
    try:
        # fin = open(os.path.join(file_path,plugin_name), "wb")
        # img = fin.read()
        # data = StringIO(img)
        # fin.close()
        conn = MongoClient('101.132.167.173', 8003)
        db = conn.mydb
        files = db.test_set
        res = files.find_one({"filename": plugin_name})
        fin = open(os.path.join(file_path, plugin_name) +
                   "." + res["file_format"], "wb")
        print(res)
        content = res['content']

        fin.write(content)
        # print('sum:', files.count())
        # insertimg = imgput.put(data)
        # print insertimg
    except Exception as e:
        print(e)
        sys.exit(1)


def _get_connection(url):
    return MongoClient(url)


def _get_db(url, db):
    client = _get_connection(url)
    return client[db]


def _get_coll(url, db, coll_name):
    db = _get_db(url, db)
    return db[coll_name]


def search(url, db, coll_name, filter={}):
    collection = _get_coll(url=url, db=db, coll_name=coll_name)
    return collection.find(filter)


def get_collection_names(url):
    """
    获取mongodb所有数据库对应的collection名
    :param url:
    :return:
    """
    client = _get_connection(url)
    d = dict((db, [collection for collection in client[db].collection_names()])
             for db in client.database_names())
    return d

