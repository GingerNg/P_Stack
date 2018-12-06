# ­*­ coding: utf­8 ­*­
"""
@author: ginger
@file: html_utils.py
@time: 2018/8/15 19:03
"""
def get_content(response):
    import chardet
    from readability import Document
    import html2text
    char_encoding = chardet.detect(response.content)   # bytes
    #print(char_encoding)
    if char_encoding["encoding"] == "utf-8" or char_encoding["encoding"] == "utf8":
        doc = Document(response.content.decode("utf-8"))
    else:
        doc = Document(response.content.decode("gbk","ignore"))
    title = doc.title()
    content = doc.summary()
    h = html2text.HTML2Text()
    h.ignore_links = True
    # h.ignore_images = True
    d_data = h.handle(content).replace("-\n","-")
    return d_data.rstrip()