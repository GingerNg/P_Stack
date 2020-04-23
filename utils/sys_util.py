# !/usr/bin/env python
# -*- coding:utf-8 -*-
import struct
import fcntl
import socket
# 获取本机电脑名
myname = socket.getfqdn(socket.gethostname())
myaddr = socket.gethostbyname(myname)
# print(myname)
# print(myaddr)


def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', bytes(ifname[:15], 'utf-8')))[20:24])


def main():
    # get_ip_address('wlp4s0') # IOError: [Errno 19] No such device
    print(get_ip_address('lo'))  # 127.0.0.1
    print(get_ip_address('ens33'))
    # addrs = socket.getaddrinfo(socket.gethostname(), None)
    # for item in addrs:
    #     print(item)


if __name__ == '__main__':
    main()
