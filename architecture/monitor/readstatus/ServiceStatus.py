# -*- coding:utf-8 -*-
import redis

from BaseStatus import BaseStatus
from constants import REDIS_HOST, REDIS_PORT, REDIS_DB, QUERY_RESULT, PROCESS_RESULT
from tools import obj2Dic


class ServiceStatus(BaseStatus):
    """
    Server status monitor
    """

    def __init__(self):
        self.processNum = -1
        self.qpsSucc = -1
        self.qpsFail = -1
        self.redisUsability = -1
        self.redisMem = -1
        self.redisSize = -1
        self.avgRT = "-1"
        self.senderNum = -1

    def readStatus(self):
        result = self.__serviceInfo()
        self.processNum = result["goProcessNum"]
        redisProccNum = result["redisProccNum"]
        self.senderNum = result["senderProccNum"]
        self.qpsSucc = result["qpsSucc"]
        self.qpsFail = 0
        self.avgRT = result["avgRT"]
        if int(redisProccNum) > 0:
            self.redisUsability = True
            self.redisMem, self.redisSize = self.__redisInfo()
        else:
            self.redisUsability = False

    def toJson(self):
        return obj2Dic([self])[0]

    def __serviceInfo(self):
        result = {'goProcessNum': -1,'redisProccNum': -1,"senderProccNum": -1, "qpsSucc": -1,"avgRT": "-1"}
        try:
            #打开进程文件读取内容 go  redis sender
            with open(PROCESS_RESULT, 'r') as f:
                line = f.readline()
                print "line :", line
                lines = str(line).strip().split(" ")
                print lines
                result['goProcessNum'] = int(lines[0])
                result['redisProccNum'] = int(lines[1])
                result['senderProccNum'] = int(lines[2])
        except Exception, e:
            print "PROCESS_RESULT fail"
            print 'str(e):\t\t', str(e)
        try:
            with open(QUERY_RESULT, 'r') as f:
                line = f.readline()
                lines = str(line).strip().split(" ")
                result['qpsSucc'] = int(str(lines[1]))
                result['avgRT'] = str(lines[2])
            if len(result) != 5:
                raise Exception
        except:
            print "fail to get service info"
        print result
        return result

    def __redisInfo(self):
        try:
            r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
            size = r.dbsize()
            mem = r.info()
            return mem['used_memory_human'], size
        except:
            print "fail to read redis info"
            return (-1,-1)


if __name__ == "__main__":
    """main entry"""
    serviceStatus = ServiceStatus()
    serviceStatus.readStatus()
    print serviceStatus.toJson()
