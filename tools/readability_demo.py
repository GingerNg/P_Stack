# ­*­ coding: utf­8 ­*­
"""
@author: ginger
@file: readability_demo.py
@time: 2018/8/3 13:58
pip install readability-lxml
"""
import json

# from readability import Document
import requests

# url = "https://www.itcodemonkey.com/article/6311.html"
from readability.readability import Document

hexun_url = "http://forex.hexun.com/2018-08-06/193689736.html"  # 和讯网

stcn_url = "http://stock.stcn.com/2018/0806/14426643.shtml"  # 证券时报网

cnfol_url = "http://news.cnfol.com/toutiaojinghua/20180806/26727381.shtml"  # 中金在线

caijing_url = "http://economy.caijing.com.cn/20180806/4496288.shtml"  # 财经网

cnstock_url = "http://news.cnstock.com/news,bwkx-201808-4254977.htm"  # 中国证券网

fsina_url = "http://finance.sina.com.cn/stock/quanshang/qsyj/2018-08-06/doc-ihhhczfc1583148.shtml"  # 新浪财经

jrj_url = "http://finance.jrj.com.cn/2018/07/28132724874630.shtml"  # 金融街

wx_url = "http://mp.weixin.qq.com/s?__biz=MzA4MzQ4NDYwNg==&mid=2651719146&idx=4&sn=ba3e57eed140a34494bed7bfede496f5&chksm=840f6f3bb378e62d9d1e62f064c69afd8ee1c662f3918ceb53def774f662f5930ad7b5ec7332#rd"

testcases = list()
# testcases.append(hexun_url)

# header = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
# }
header = {"Content-Type": "application/json"}
response = requests.get(wx_url,headers=header)
print(type(response.text))    # str
print(type(response.content))

"""检查bytes的编码方式"""
import chardet
char_encoding = chardet.detect(response.content)   # bytes
# print(char_encoding)
if char_encoding["encoding"] == "utf-8" or char_encoding["encoding"] == "utf8":
    doc = Document(response.content.decode("utf-8"))
else:
    doc = Document(response.content.decode("gbk","ignore"))
title = doc.title()
content = doc.summary()
# print(doc.tags())

# print(doc.get_clean_html())

# print(doc.)

print(content)

# print(title)
# print(content)

# import html2text
# h = html2text.HTML2Text()
# h.ignore_links = True
# 
# h.ignore_images = True
# # h.abbr_data
# # print(h.handle(response.text).replace("-\n","-"))
# 
# print(h.handle(content).replace("-\n","-"))
# d_data = h.handle(content).replace("-\n","-")
# 
# """ner_ranking"""
# header = {"Content-Type":"application/json"}

# 
# d_json = {}
# # d_json["data"] =d_data
# # d_json["title"] = title
# d_json["title"] = "招股书"
# d_json["data"] = "小米招股书 发布"
# response = requests.post(ner_url,json=d_json,headers=header)
# print(json.loads(response.content))
# 
# 
# """keywords"""
# d_json = {}
# d_json["title"] = title
# d_json["content"] = d_data
# access_token = "24.4277998c6bdfebae2aba81c9667c93a2.2592000.1536143883.282335-11639900"
# keyword_url = "https://aip.baidubce.com/rpc/2.0/nlp/v1/keyword?access_token=%s" % access_token
# 
# header = {"Content-Type":"application/json"}
# 
# response = requests.post(keyword_url,json=d_json,headers=header)
# 
# content = response.content
# if (content):
#     print(content.decode("gbk"))
# # https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=Va5yQRHlA4Fq5eR3LT0vuXV4&client_secret=0rDSjzQ20XUj5itV6WRtznPQSzr5pVw2&

