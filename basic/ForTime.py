# -*- coding: utf-8 -*-
# ForTime.py
# @author Ginger
# @description 
# @created 2020-03-03T13:18:27.234Z+08:00
#

import time

# todo
import numpy as np


def mockdata():
    for _ in range(10):
        s = time.time()
        sum = 0
        for i in range(0, 10):
            sum += i
        print(time.time()-s)


def npmock():
    for _ in range(10):
        ars = np.arange(0, 100000, 1)
        s = time.time()
        sum = 0
        for a in ars:
            sum += a
        print(time.time() - s)


# import requests
if __name__ == '__main__':
    # math.pow(2, 3)
    # requests.get("http://www.baidu.com")
    mockdata()
    # print("--------")
    # npmock()
