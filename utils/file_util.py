#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
 @File: file_util.py
 @author: ginger 
 @software: PyCharm  
 @time: 17-11-9 下午8:28
 @desc:
 @source: https://www.cnblogs.com/lovebread/archive/2009/12/24/1631108.html
 在python中定义私有变量只需要在变量名或函数名前加上 "__"两个下划线，那么这个函数或变量就会为私有的了
 https://www.cnblogs.com/xuxn/archive/2011/07/27/read-a-file-with-python.html


w     以写方式打开，
a     以追加模式打开 (从 EOF 开始, 必要时创建新文件)
r+     以读写模式打开
w+     以读写模式打开 (参见 w )
a+     以读写模式打开 (参见 a )
rb     以二进制读模式打开
 https://www.cnblogs.com/dkblog/archive/2011/02/24/1980651.html
"""
from __future__ import print_function
import datetime
import shutil
import os
import fileinput
import time


# f = open('testfile','r')

# tem = f.read(10) # read(size)
# print tem

# print f.readline() # return a string added \n

# print f.readlines(2)
# when reach the end of the file , it returns a ''

# f.close()
#
# f_2 = open('testfile','w')
# f_2.write('This is a test\n')
# write string into the file, remove the previous content

# print f_2.tell()


def read_file(file_path):
    file_object = open(file_path, 'r')
    try:
        all_the_text = file_object.read()
        return all_the_text
    finally:
        file_object.close()


def write_file(file_path, content):
    file_object = open(file_path, 'w')   # w  wb binary
    try:
        file_object.write(content)
    finally:
        file_object.close()


def read_file_by_line(file_path):
    file_object = open(file_path, 'r')
    try:
        one_line_text = file_object.readline()
        # if one_line_text:
        #     file_object.close()
        return one_line_text
    finally:
        file_object.close()


# tail -f
def read_all_lines(file_path):
    file_object = open(file_path, 'r')
    while True:
        time.sleep(1)
        one_line = file_object.readline()
        print(one_line, end='')  # print 输出不换行


'''
https://www.cnblogs.com/xuxn/archive/2011/07/27/read-a-file-with-python.html
'''


def read_all_file_by_line(file_path):
    line_list = []
    for line in fileinput.input(file_path):
        line_list.append(line)
    return line_list


def find_all_file(directory):
    list_path = os.listdir(directory)
    all_file_path = []
    for i in range(0, len(list_path)):
        path = os.path.join(directory, list_path[i])
        if os.path.isfile(path):
            all_file_path.append(path)
    return all_file_path


def file_filter(file_paths, by_what=None):
    return file_paths


def make_directory_by_time():
    dir_name = ''
    return dir_name


def move_file(source_path, target_path):
    pass


def get_all_file_size(path):
    pass


def read_recovery_info(recovery_path):
    if recovery_path is None:
        return 0
    else:
        return read_file_by_line(recovery_path)


def get_line_number(file_path):
    pass

# https://www.cnblogs.com/strongYaYa/p/7200357.html


def get_all_file_name(file_dir, file_mime='.jpg'):
    file_names = []
    for file_name in os.listdir(file_dir):
        file_split_text = os.path.splitext(file_name)
        if file_split_text[1] == file_mime:
            file_names.append(file_split_text[0].split("_")[0])
    return file_names


    # print os.path.dirname(directory)  # 返回父目录
    # print os.path.basename(directory)
    # print os.listdir(directory)
'''
判断文件是否存在
os.path.isfile('d:/assist')
'''


def isexisted(file_path):
    return os.path.exists(file_path)


# https://www.cnblogs.com/iderek/p/8035757.html


def overdue_clean(file_path, days):
    """
    定期删除文件夹中的过期数据
    :param file_path:
    :return:
    """
    ds = list(os.walk(file_path))  # [0][1]  # 获得所有文件夹的信息列表
    del ds[0]
    for d in ds:  # 遍历该列表
        if (len(d[2]) == 0 or _is_overdue(d, days)):
            shutil.rmtree(d[0])


def _is_overdue(d, days):
    """
    文件夹是否过期
    :param d: d[0]:根目录, d[1]:子目录list, d[2]:子文件list
    :param days:
    :return:
    """
    for x in d[2]:  # 遍历这些文件
        now = datetime.datetime.now()  # 获取当前时间
        delta = datetime.timedelta(days=0)
        ctime = datetime.datetime.fromtimestamp(
            os.path.getctime(os.path.join(d[0], x)))  # 获取文件创建时间
        if ctime < (now - delta):  # 若创建于delta天前
            return True
    return False


def main():
    read_all_lines("FILE_PATH")


if __name__ == '__main__':
    if __name__ == "__main__":
        overdue_clean("PATH", 1)
