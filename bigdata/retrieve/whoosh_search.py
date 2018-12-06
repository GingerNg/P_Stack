# ­*­ coding: utf­8 ­*­
"""
@author: ginger
@file: whoosh_search.py
@time: 2018/8/29 18:32
"""

from whoosh.index import open_dir
from whoosh.query import *

index = open_dir("path", indexname='blog_index')  # 读取建立好的索引


def find(words):
    with index.searcher() as searcher:
        myquery = And([
            Or([Term("html", w), Term("title", w)])
            for w in words
        ]
        )
        results = searcher.search(myquery, limit=None)
        for res in results:
            print(res['title'], res['url'])


s = 'vue webpack'
words = [w.strip() for w in s.split()]
find(words)