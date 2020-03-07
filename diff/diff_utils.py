#!/usr/bin/env python
# -*- coding: utf-8 -*-

import difflib
import sys

try:
    textfile1 = sys.argv[1]
    textfile2 = sys.argv[2]
except Exception as e:
    print("Error:" + str(e))
    print("Usage: python sample3.py filename1 filename2")
    sys.exit()


def readfile(filename):
    try:
        filehandle = open(filename, 'r')
        text = filehandle.read().splitlines()
        filehandle.close()
        return text
    except IOError as error:
        print('Read file Error:' + str(error))
        sys.exit()


text1_lines = readfile(textfile1)
text2_lines = readfile(textfile2)

d = difflib.HtmlDiff()
print(d.make_file(text1_lines, text2_lines))