# ­*­ coding: utf­8 ­*­
"""
@author: ginger
@file: baidu_api.py
@time: 2018/8/6 18:28
"""
import json

import requests

"""鉴权认证机制"""
# client_id 为官网获取的AK， client_secret 为官网获取的SK
a_k = "XXX"
s_k = "XXX"


host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s'
oauth_url = host %(a_k,s_k)
response = requests.get(oauth_url)
print(response.content)

d_json = {}
access_token = "XXXX"
d_json["title"] = "iphone手机出现“白苹果”原因及解决办法，用苹果手机的可以看下"
d_json["content"] = "如果下面的方法还是没有解决你的问题建议来我们门店看下成都市锦江区红星路三段99号银石广场24层01室。在通电的情况下掉进清水，这种情况一不需要拆机处理。尽快断电。用力甩干，但别把机器甩掉，主意要把屏幕内的水甩出来。如果屏幕残留有水滴，干后会有痕迹。^H3 放在台灯，射灯等轻微热源下让水分慢慢散去。"
keyword_url = "https://aip.baidubce.com/rpc/2.0/nlp/v1/keyword?access_token=%s" % access_token

header = {"Content-Type":"application/json"}

response = requests.post(keyword_url,json=d_json,headers=header)

content = response.content
if (content):
    print(content.decode("gbk"))