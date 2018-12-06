# coding:utf8
# author:ginger

# dumps：序列化一个对象
# dump：将一个对象序列化存入文件

import json
data = {"spam":"foo","parrot":42} # dict
in_json = json.dumps(data)  # Encode the data  , object--> json
print (type(in_json)) # str
print (in_json)
print (type(json.loads(in_json)))

in_json_2 = json.dumps(data, sort_keys=True, indent=4, separators = (',', ': '), encoding ="gbk", ensure_ascii=True)



"""
dump：将一个对象序列化存入文件
dump()的第一个参数是要序列化的对象，第二个参数是打开的文件句柄
注意打开文件时加上以UTF-8编码打开

* 运行此文件之后在统计目录下会有一个data.json文件，打开之后就可以看到json类型的文件应该是怎样定义的

"""
def object_json_file(file_json,data):
    # with open(file_json, "w", encoding="UTF-8") as f_dump:   # python2.7不支持encoding这个参数
    with open(file_json, "w") as f_dump:
        json.dump(data, f_dump, ensure_ascii=False)  # Serialize

#  json-file --> dict
def json_file_to_obj(file_json):
    with open(file_json, "r") as f_dump:
        load = json.load(f_dump)
        return load

if __name__=='__main__':
    # object_json_file("data.json",data=data)

    list = [1,2,4,5]
    # print type(json.dumps(list))

