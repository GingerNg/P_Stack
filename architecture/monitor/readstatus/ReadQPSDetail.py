# -*- coding:utf-8 -*-#
# Author:  lixintang --<xintangli_2012@163.com>
# Created: 2017-06-29 17:58

from BaseStatus import BaseStatus
from constants import QPS_DETAIL_FILE
from tools import obj2Dic

taskOrderMap = dict()

class ReadQPSDetail(BaseStatus):
    def __init__(self):
        self.qps = list()
        self.qpsTime = list()

    def readStatus(self):
        try:
            with open(QPS_DETAIL_FILE, 'r') as f:
                lines = f.readlines()
                if len(lines) == 0:
                    raise Exception;
                for i in range(len(lines)):
                    qpsLine = str(lines[i]).strip().split(" ")
                    self.qps.append(int(qpsLine[0]))
                    self.qpsTime.append(int(qpsLine[1]))
        except Exception, e:
            print "read qps detail err",e

    def toJson(self):
        return obj2Dic([self])[0]

if __name__ == "__main__":
    """main entry"""
    qpsDetail = ReadQPSDetail()
    qpsDetail.readStatus()
    print qpsDetail.toJson()