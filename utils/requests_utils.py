# ­*­ coding: utf­8 ­*­
#!/usr/bin/python
"""
@author: ginger
@file: requests_utils.py
"""
import json
from urllib.parse import urljoin

import requests

'''
python requests 调用restful api
'''


class MessageSender():
    def __init__(self, url, resource_pos=None):
        self.__url = url
        self.__resource_pos = resource_pos

    def __composite_target_url(self, resource_pos):
        if resource_pos is None:
            target_url = urljoin(self.__url, self.__resource_pos)
        else:
            # target_url = urljoin(self.__url, resource_pos)
            target_url = self.__url + resource_pos
        return target_url

    def message_send(self, data, resource_pos=None):
        headers = {"Content-Type": "application/json"}
        target_url = self.__composite_target_url(resource_pos)
        print(target_url)
        data_json = json.dumps(data)
        result = requests.post(target_url, headers=headers, data=data_json)
        return result

    def message_multipart_post(self, file_path, resource_pos=None):
        target_url = self.__composite_target_url(resource_pos)
        print(target_url)
        files = {'file': open(file_path, 'rb')}
        # r = requests.post(url, data, files=files)
        d_json = {"test": "test"}
        return requests.post(url=target_url, files=files, data=d_json).text

    def message_get(self, resource_pos):
        target_url = urljoin(self.__url, resource_pos)
        return requests.get(target_url).text

    def message_put(self, data, resource_pos):
        headers = {"Content-Type": "application/json"}  # 必需
        target_url = self.__composite_target_url(resource_pos)
        data_json = json.dumps(data)
        return requests.put(target_url, headers=headers, data=data_json).text

    def message_delete(self, resource_pos, data):
        headers = {"Content-Type": "application/json"}  # 必需
        target_url = urljoin(self.__url, resource_pos)
        data_json = json.dumps(data)
        return requests.delete(target_url, headers=headers, data=data_json).text


def file_extension(path):
    return os.path.splitext(path)[1]


if __name__ == '__main__':
    # post test
    #
    # parse_pos = "/parse"
    #
    # upload_pos = "/store/upload/"
    #
    # # print type(resource_pos3)
    #
    # data = {"title": "copy a book"}
    #
    # msg_sender = MessageSender(root_url)
    #
    # print(msg_sender.message_multipart_post("test.xlsx",resource_pos = parse_pos))

    # msg_sender.message_put(data, resource_pos3)

    # print open('result.txt', 'rb')
    # print message_send(root_url, resource_pos1, data)    # <Response [201]>
    # print msg_sender.message_multipart_post(file_path='result.txt',resource_pos=resource_pos2)
    # get test
    # print message_get(root_url,resource_pos=resource_pos)

    # put test
    # data = {"done":False}
    # print message_put(root_url, resource_pos)
    # content = response.content
    # is_parsed = content["is_parsed"]
    # print(is_parsed)
    # with open("test.data","wb") as f:
    #     f.write(response.content)

    import os.path

    print(file_extension('wxPython'))
