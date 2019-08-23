# ­*­ coding: utf­8 ­*­
import os
import sys
from io import BytesIO

import bson
from pymongo import MongoClient, ReturnDocument

class MongoDao(object):
    def __init__(self, url, db, coll_name):
        self.collection = self._get_coll(url=url, db=db, coll_name=coll_name)

    def _get_coll(self, url, db, coll_name):
        db = _get_db(url, db)
        return db[coll_name]

    def _get_connection(self, url):
        return MongoClient(url)

    def _get_db(self, url, db):
        client = _get_connection(url)
        return client[db]

    def search_one(self, filter={}):
        return self.collection.find_one(filter, no_cursor_timeout=True)

    def search(self, filter={}, sort_list=None, limit=None):
        if limit:
            if sort_list:
                return self.collection.find(filter).sort(key_or_list=sort_list).limit(limit)
            return self.collection.find(filter, no_cursor_timeout=True).limit(limit)
        else:
            if sort_list:
                return self.collection.find(filter, no_cursor_timeout=True).sort(key_or_list=sort_list)
            return self.collection.find(filter, no_cursor_timeout=True)

    def search_projection(self, filter={}, projection=None):
        return self.collection.find(filter=filter, no_cursor_timeout=True, projection=projection)

    def insert_one(self, data={}):
        self.collection.insert_one(document=data)

    def insert_many(self, documents):
        self.collection.insert_many(documents=documents)

    def update_one(self, filter={}, data={}, upsert=False):
        """
        upsert = update + insert
        :param filter:
        :param data:
        :param upsert:
        :param collection:
        :return:
        """
        self.collection.update_one(filter=filter, update={"$set": data}, upsert=upsert)

    def update_many(self, filter={}, data={}, upsert=False):
        self.collection.update_many(filter=filter, update={"$set": data}, upsert=upsert)

    def search_upsert_one(self, filter={}, data={}, ids={}):
        """
        :param filter:
        :param data:
        :param ids: {"key1":1,"key2":0} 合并(1)or保留(0)
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

    def create_index(self, keys):
        self.collection.create_index(keys=keys)

    def drop(self):
        self.collection.drop()

    def create_indexes(self, indexes):
        self.collection.create_indexes(indexes=indexes)

    def delete(self, _id, filter=None):
        if _id:
            self.collection.delete_one(filter={'_id': _id})
        elif filter:
            self.collection.delete_many(filter=filter)
        else:
            raise Exception('_id and filter cant all none')



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
        fin = open(os.path.join(file_path, plugin_name) + "." + res["file_format"], "wb")
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


def get_connection_hp(host, port):
    return MongoClient(host=host, port=port)


def _get_db(url, db):
    client = _get_connection(url)
    return client[db]


def get_coll(url, db, coll_name):
    db = _get_db(url, db)
    return db[coll_name]


def search(url, db, coll_name, filter={}):
    collection = get_coll(url=url, db=db, coll_name=coll_name)
    return collection.find(filter, no_cursor_timeout=True)


def search_one(url, db, coll_name, filter={}, collection=None):
    if collection is None:
        collection = get_coll(url=url, db=db, coll_name=coll_name)
    return collection.find_one(filter, no_cursor_timeout=True)


def fetch_one(url, db, coll_name, filter={}, ):
    collection = get_coll(url=url, db=db, coll_name=coll_name)
    # return collection.find_one(filter)
    return collection.find_one_and_update(filter,
                                          {"$set": {"status": "1"}},
                                          return_document=ReturnDocument.AFTER)


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


def update_one(url, db, coll_name, filter={}, data={}, upsert=False, collection=None):
    if collection is None:
        collection = get_coll(url=url, db=db, coll_name=coll_name)
    collection.update_one(filter=filter, update={"$set": data}, upsert=upsert)
    # db.stu.update_one({"age": 18}, {"$set": {"age": 100}})


def update_many(url, db, coll_name, filter={}, data={}, upsert=False, collection=None):
    if collection is None:
        collection = get_coll(url=url, db=db, coll_name=coll_name)
    collection.update_many(filter=filter, update={"$set": data}, upsert=upsert)
    # db.stu.update_one({"age": 18}, {"$set": {"age": 100}})


def insert_one(url, db, coll_name, data={}):
    collection = get_coll(url=url, db=db, coll_name=coll_name)
    collection.insert_one(document=data)


def insert_or_update_one(url, db, coll_name, filter={}, data={}, id_key=None):
    collection = get_coll(url=url, db=db, coll_name=coll_name)
    if filter is not {}:
        record = collection.find_one(filter=filter)
    else:
        record = None
    if record:
        # 更新
        if "update_time" in record:
            data["update_time"] = record["update_time"]
        if id_key is not None:
            data[id_key] = record[id_key]
        collection.update_one(filter=filter, update={"$set": data})
    else:
        # 插入
        collection.insert_one(document=data)


def save_or_update_one(url, db, coll_name, filter={}, data={}):
    collection = get_coll(url=url, db=db, coll_name=coll_name)
    record = collection.find_one(filter=filter)
    if record:
        # 更新
        data["D_id"] = record["D_id"]
        collection.update_one(filter=filter, update={"$set": data})
    else:
        # 插入
        collection.insert_one(document=data)

def total_count(url,db,coll_name,filter = None):
    """
    统计mongo数据量
    :param url:
    :param db:
    :param coll_name:
    :param filter:
    :return:
    """
    collection = get_coll(url=url, db=db, coll_name=coll_name)
    if filter is None:
        return collection.count()
    else:
        return collection.find(filter).count()



