#!/usr/bin/env python
"""
https://github.com/chrismattmann/tika-python
http://localhost:9998/
"""
# import tika
# tika.initVM()
from tika import parser

parsed = parser.from_file('./chengdu.pdf',"http://localhost:9998/")
# parsed = parser.from_file('./P020190531573831612726.doc',"http://localhost:9998/")
# parsed = parser.from_file('./带图片文档.docx',"http://localhost:9998/")
# parsed = parser.from_file('./tika_file.html',"http://localhost:9998/")
print(parsed["metadata"])
# print(parsed["content"])
# print(parsed.keys())
open("./chengdu.txt","w").write(parsed["content"])

