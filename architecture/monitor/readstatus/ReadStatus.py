# -*- coding:utf-8 -*-
# Author:  chenhailong --<chenhailong@chinadep.com>
# Created: 2017/5/19
#
import urllib
import urllib2
from constants import DasURL, supPath, persistPath
from SysStatus import SysStatus
from SupStatus import SupStatus
from DemStatus import DemStatus
from ReadQPSDetail import ReadQPSDetail
from ServiceStatus import ServiceStatus
import ConfigParser
import json
import time
########################################################################
class ReadStatus(object):
    """"""
    #----------------------------------------------------------------------
    def persist(self):
        '''持久化到文件 或 数据库'''
        warnLevel = {"warnLevel": "OK"}
        try:
            jsonSup = self.__getSupConf()
            jsonMonitor = self.__readStatus()
            jsonMonitor_msg = jsonMonitor["msg"]
            if len(jsonMonitor_msg["SYSINFO"]["MSGWARN"]) > 0 or len(jsonMonitor_msg["SUPINFO"]["MSGWARN"]) > 0:
                warnLevel = {"warnLevel": "WARN"}
            if len(jsonMonitor_msg["SYSINFO"]["MSGERR"]) > 0 or len(jsonMonitor_msg["SUPINFO"]["MSGERR"]) > 0:
                warnLevel = {"warnLevel": "ERR"}
        except Exception, e:     
            warnLevel = {"warnLevel": str(e)}
        moniTarget = {"moniTarget": "MONITOR"}
        jsonStatus = dict(moniTarget.items() + warnLevel.items() + jsonSup.items() + jsonMonitor.items())      
        curTime = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
        data = dict({"curTime":curTime}, **jsonStatus)
        
        # post data to DAS
        self.__post(data)
        # persiit data to file
        self.__persist(data)
        
    def __persist(self, data):
        try:
            f = open(persistPath, mode='a')
            f.write(json.dumps(data))
            f.write("\n")            
        except Exception, e:
            pass
        finally:
            f.close()     
        
    def __post(self, data):
        data = json.dumps(data)
        req = urllib2.Request(DasURL, data=data)
        try:
            res = urllib2.urlopen(req, timeout=5)
            if res.getcode() == 200:
                print "send success"
        except Exception, e:
            print "error in urlopen"        
        
    def __readStatus(self):
        start = time.clock()
        jsonStatus = {}
        # system info
        sysStatus = SysStatus()
        sysStatus.readStatus()
        
        # service info
        serviceStatus = ServiceStatus()
        serviceStatus.readStatus()
        
        # sup info
        supStatus = SupStatus()
        supStatus.readStatus()
        
        # dem info
        demStatus = DemStatus()
        demStatus.readStatus()

        #QPS detail
        qpsDetail = ReadQPSDetail()
        qpsDetail.readStatus()

        jsonStatus["SYSINFO"] = sysStatus.toJson()
        jsonStatus["SERINFO"] = serviceStatus.toJson()
        
        jsonStatus["SUPINFO"] = supStatus.toJson()
        jsonStatus["DEMINFO"] = demStatus.toJson()
        jsonStatus["QPSINFO"] = qpsDetail.toJson()

        end = time.clock()
        print "time use: ",end - start
        print jsonStatus
        return {"msg":jsonStatus}
    
    def __getSupConf(self):
        memId = ''
        nodeId = ''
        try:
            conf = ConfigParser.ConfigParser()
            conf.read(supPath)
            memId = conf.get("service", "account_id")
            nodeId = conf.get("node", "node_id")
        except Exception as e:
            msg = "读取配置文件失败"
            return {"memId":"-1", "nodeId":"-1"}
        return {"memId":memId, "nodeId":nodeId}

if __name__ == "__main__" :
    '''this is the main method'''
    readStatus = ReadStatus()
    
    readStatus.persist()

