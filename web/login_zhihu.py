#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
 @File: login_zhihu.py
 @author: ginger 
 @software: PyCharm
 @desc: https://segmentfault.com/a/1190000005778518
"""

import requests,time
from bs4 import BeautifulSoup
def get_captcha(data):
    with open('captcha.gif','wb') as fp:
        fp.write(data)
    return input('输入验证码：')

def login(username,password,oncaptcha):
    sessiona = requests.Session()
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
    _xsrf = BeautifulSoup(sessiona.get('https://www.zhihu.com/#signin',headers=headers).content,'html.parser').find('input',attrs={'name':'_xsrf'}).get('value')
    captcha_content = sessiona.get('https://www.zhihu.com/captcha.gif?r=%d&type=login'%(time.time()*1000),headers=headers).content
    data = {
        "_xsrf":_xsrf,
        "email":username,
        "password":password,
        "remember_me":True,
        "captcha":oncaptcha(captcha_content)
    }
    resp = sessiona.post('https://www.zhihu.com/login/email',data,headers=headers).content
    print(resp)
    return resp

if __name__ == "__main__":
    login('XXXX','XXXX',get_captcha)