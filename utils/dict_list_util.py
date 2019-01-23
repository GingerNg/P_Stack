#!/usr/bin/python
# -*- coding:utf-8 -*-
def convert_to_dict_list(objs):
    '''把对象列表转换为字典列表'''
    obj_arr = []

    for o in objs:
        #把Object对象转换成Dict对象
        dict = {}
        dict.update(o.__dict__)
        obj_arr.append(dict)

    return obj_arr

def class_to_dict(obj):
    '''把对象(支持单个对象、list、set)转换成字典'''
    is_list = obj.__class__ == [].__class__
    is_set = obj.__class__ == set().__class__

    if is_list or is_set:
        obj_arr = []
        for o in obj:
            #把Object对象转换成Dict对象
            dict = {}
            dict.update(o.__dict__)
            obj_arr.append(dict)
        return obj_arr
    else:
        dict = {}
        dict.update(obj.__dict__)
        return dict

def list2str(list):
    return ' '.join(list)

def str2list(str):
    list(map(int, '12345'))

# split: str--> list

class Student:
    name = ''
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age


stu = Student('XXX', 20)
if __name__=='__main__':
    print (convert_to_dict_list([stu, stu]))
    print (class_to_dict([stu, stu]))


    print(list2str(["taobao","baidu"]))