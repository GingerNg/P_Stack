# ­*­ coding: utf­8 ­*­
"""
@author: ginger
@file: html2text_demo.py
@time: 2018/8/3 14:05
"""
import html2text
h = html2text.HTML2Text()
# h.ignore_links = True
# h.ignore_images = True
print(h.handle("<p>Hello, <a href='http://earth.google.com/'>world</a>! <img alt='' src='http://n.sinaimg.cn/translate/485/w512h773/20180728/aYof-hfxsxzf8508060.jpg'>"))


test_re = h.handle("<p>Hello, <a href='http://earth.google.com/'>world</a>! <img alt='' src='http://n.sinaimg.cn/translate/485/w512h773/20180728/aYof-hfxsxzf8508060.jpg'>")


test_re1 = test_re.replace("-\n","-")

print(test_re1)





