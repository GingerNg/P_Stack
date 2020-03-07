# ­*­ coding: utf­8 ­*­
"""
@author: ginger
@file: whoosh_demo.py
@time: 2018/8/29 18:25

"""
from whoosh.index import create_in
from whoosh.fields import *
from jieba.analyse import ChineseAnalyzer
import json

# 导入中文分词工具
analyser = ChineseAnalyzer()

# 可以设置不同类型的索引
# schema = Schema(phone_name=TEXT(stored=True, analyzer=analyser),
#                 price=NUMERIC(stored=True),
#                 phoneid=ID(stored=True))  # 创建索引结构

schema = Schema(
    title=TEXT(stored=True, analyzer=analyser),
    html=TEXT(stored=True),
    url=TEXT(stored=True)
)
# path 为索引创建的地址，blog_index 为索引名称
ix = create_in("path", schema=schema, indexname='blog_index')

writer = ix.writer()
# 写入数据
with open('blogs.json', mode='r') as f:
    blogs = json.load(f)

for blog in blogs:
    writer.add_document(
        title=blog['title'],
        html=blog['html'],
        url=blog['url']
    )
writer.commit()
print("建立完成一个索引")