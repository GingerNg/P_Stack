# ­*­ coding: utf­8 ­*­
"""
@author: ginger
@file: fastdfs_demo.py
@time: 2018/6/29 16:43
"""
# !/usr/local/bin/python2.7
import os
import time
import sys
from multiprocessing import Process

try:
    from fdfs_client.client import *
    from fdfs_client.exception import *
except ImportError:
    import_path = os.path.abspath('../')
    sys.path.append(import_path)
    from fdfs_client.client import *
    from fdfs_client.exceptions import *
# size_total = 0
if __name__ == '__main__':
    starttime = time.time()
    filenumbers = 100000  # number of processes

    client = Fdfs_client('/opt/fdfs_client-py/fdfs_client/client.conf')
    try:
        for i in range(filenumbers):
            filename = '/data/files/small/smallfile' + str(i)
            client.upload_by_filename(filename)
    except Exception as e:
        print
        "error" + str(e)
    endtime = time.time()
    # print "%d byte has been stored into the fdfs." % size_total
    print
    "%f seconds for sequence processing computation." % (endtime - starttime)
    # print size_total
