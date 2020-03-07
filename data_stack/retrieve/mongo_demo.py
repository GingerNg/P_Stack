from utils.mongo_utils import MongoDao
"""
https://www.cnblogs.com/wzndkj/p/9411251.html
建立索引：
db.getCollection("retrieve_ginger").ensureIndex({'name':'text','content':'text'})

//db.getCollection("retrieve_collection_dev").find({})
//db.getCollection("retrieve_ginger").getIndexes()
//db.getCollection("retrieve_ginger").ensureIndex({'name':'text','content':'text'})
db.getCollection("retrieve_ginger").find({$text:{$search:'"知识图谱" "ort" "otr"'}})   // 与
//db.getCollection("retrieve_ginger").find({$text:{$search:'知识图谱 KG 发展报告'}})  // or
"""

if __name__ == '__main__':
    mongodao = MongoDao(url='mongodb://192.168.1.218:8014/',
                         db='retrieve_db',
                         coll_name='retrieve_ginger')
    condition_and = {
        "$text":{
            # "$search":"\"知识图谱\" \"ort\" \"希拉里\""
            "$search":"\"知识图谱\" \"ort\" \"希拉里\""
        }
    }
    condition_or = {
        "$text": {
            "$search": "未来"
        }
    }

    res = mongodao.search(filter=condition_or)
    for r in res:
        print(r)