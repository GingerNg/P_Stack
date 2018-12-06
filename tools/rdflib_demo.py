# ­*­ coding: utf­8 ­*­
"""
@author: ginger
@file: rdflib_demo.py
@time: 2018/8/31 19:08


"""

# 导入nt文件
from rdflib import Graph, RDF

g = Graph()

'''
format: 'rdf/xml' 'xml', 'n3', 'nt', 'trix', 'rdfa'
'''
g.parse("icd10.nt", format="n3")

# 打印图的大小
print(len(g))  # prints 2

# 遍历所有三元组
import pprint

for stmt in g:
    pprint.pprint(stmt)

if __name__ == "__main__":
    from rdflib import Graph

    g = Graph()
