#!/usr/bin/python
# -*- coding:utf-8 -*

import requests
import json
def coordinate_covert(locations):
    """
    http://lbs.amap.com/api/webservice/guide/api/convert/
    参数：
    key
    locations
    coordsys
    sig
    output
    :return:
    """
    amap_url = "http://restapi.amap.com/v3/assistant/coordinate/convert"
    key = "041cea4faa49c3055cfb3b59f6680e4d"
    # locations = ""
    url = "%s?locations=%s&coordsys=%s&output=%s&key=%s" % (amap_url,locations,"baidu","json",key)
    print (url)
    response = requests.get(url=url)
    result = response.text
    resultObj = json.loads(result)
    if resultObj["status"] == 1:
        return resultObj["locations"]
    else:
        print (resultObj["info"])
        raise Exception

if __name__=="__main__":
    locations = "116.481499,39.990475|116.481499,39.990375"
    print (coordinate_covert(locations))


