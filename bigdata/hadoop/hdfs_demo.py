# !/usr/bin/env python
# -*- coding:utf-8 -*-

# https://www.cnblogs.com/shoufengwei/p/5949791.html

from hdfs3 import HDFileSystem
hdfs = HDFileSystem(host='XX.XX.XX.XX', port=9000)


def mkdir(remotepath):
    if not exists(remotepath):
        hdfs.mkdir(dir)


def get(remotepath, localpath):
    if exists(remotepath):
        hdfs.get(remotepath, localpath)


# def put(localfile, remotefile):
#     dir = getDirPath(remotefile)
#     mkdir(dir)
#     hdfs.put(localfile, remotefile)


def exists(remotepath):
    return hdfs.exists(remotepath)


def delete(remotepath):
    if exists(remotepath):
        hdfs.rm(remotepath, recursive=True)

if __name__=='__main__':
    delete("PATH/test")
