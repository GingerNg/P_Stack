import json
import time
import simplejson
import simdjson

"""
python的三个json工具比较
    0.0020477771759033203
    0.0008437633514404297
    0.0008678436279296875

simplejson和simdjson(https://github.com/TkTech/pysimdjson)速度相当,会比json包快一个数量级
"""

def demo_simplejson(fin):

    doc = simplejson.loads(fin)
    # print(doc)

def demo_simdjson(fin):

    # doc = simdjson.ParsedJson(fin.read()).to_obj()
    # doc = simdjson.loads(fin)
    doc = simdjson.ParsedJson(fin).to_obj()
    # print(doc)

def demo_json(fin):
    load_dict = json.loads(fin)
    # print(load_dict)

if __name__ == '__main__':
    fin = open('apache_builds.json', 'rb').read()

    start = time.time()
    demo_json(fin)
    print(time.time()-start)

    start = time.time()
    demo_simdjson(fin)
    print(time.time()-start)

    start = time.time()
    demo_simplejson(fin)
    print(time.time()-start)
