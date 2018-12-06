#!/usr/bin/python
# -*- coding:utf-8 -*-

import pandas as pd

data = pd.read_csv("tablib_demo.csv")

print (data)
print (data.columns)

print (data['area'])