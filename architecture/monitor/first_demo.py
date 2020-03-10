#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author: ginger
@file: demo.py
@time: 2018/4/28 10:52
"""


import thread
import time
import socket
import psutil
from influxdb import InfluxDBClient

client=InfluxDBClient('localhost',8009,'','','grafana')
#获取本机IP
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 0))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
ip = get_ip()

def get_cpu(sec):
    """
    取cpu信息
    :param sec:
    :return:
    """
    while True:
        time.sleep(sec)
        info=psutil.cpu_percent(0)
        text=[
            {
                "measurement":"cpu_info",
                "tags":{
                           "host":ip
                },
                "fields":{
                            "percent":info
                }
            }
        ]
        print text

        client.write_points(text)
        print "--"

def get_memory(sec):
    while True:
        time.sleep(sec)
        info=psutil.virtual_memory()
        text=[
            {
                "measurement":"memory_info",
                    "tags":{
                           "host":ip
                },
                "fields":{
                            "mem_percent":info.percent,
                            "mem_used":info.used,
                            "mem_free":info.free,
                }
            }
        ]
        client.write_points(text)

def get_disk(sec):
    while True:
        time.sleep(sec)
        info=psutil.disk_usage('/')
        text=[
            {
                "measurement":"disk_info",
                "tags":{
                           "host":ip
                },
                "fields":{
                            "disk_used":info.used,
                            "disk_free":info.free,
                            "disk_percent":info.percent,
                }
            }
        ]
        client.write_points(text)


def get_network(sec):
    while True:
        time.sleep(sec)
        info = psutil.net_io_counters(pernic=True)['ens192']
        text=[
            {
                "measurement":"network_info",
                "tags":{
                           "host":ip
                },
                "fields":{
                            "bytes_sent":info.bytes_sent,
                            "bytes_recv":info.bytes_recv,
                }
             }
        ]
        client.write_points(text)
try:
    thread.start_new_thread( get_cpu,(1,))
except:
    print "ERROR:cpu unable to start thread"
try:
    thread.start_new_thread( get_memory, (1,))
except:
    print "ERROR:mem_ory unable to start thread"
try:
    thread.start_new_thread( get_disk, (1,))
except:
    print "ERROR:disk unable to start thread"
# try:
#     thread.start_new_thread( get_network,(1,))
# except:
#     print "ERROR:net unable to start thread"
while 1:
    pass