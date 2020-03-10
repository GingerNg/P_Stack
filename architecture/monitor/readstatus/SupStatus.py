# -*- coding:utf-8 -*-
# Author:  chenhailong --<chenhailong@chinadep.com>
# Created: 2017/5/19
#
from BaseStatus import BaseStatus
from tools import obj2Dic
import time
import os
from xml.dom import minidom
from constants import path, busilog, b_step, nginxlog, n_step, s_b_step, s_n_step, sup_qps, orderPath

MSGERR = {}
MSGWARN = {}
########################################################################
class SupStatus(BaseStatus):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        super(BaseStatus, self).__init__()
        #self.supStatistics = ''
        self.supData = ''
    
    def readStatus(self):
        supData = SupData()
        supStatistics = SupStatistics()
        #self.supStatistics = supStatistics.readStatus()
        endtime = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
        self.supData = supData.readStatus(endtime)
    
    def toJson(self):
        jsonData = obj2Dic([self])[0]

        jsonData["MSGERR"] = MSGERR
        jsonData["MSGWARN"] = MSGWARN
        return  jsonData 



########################################################################
class SupStatistics(object):
    '''供方供数统计数据'''
    '''暂时 不用'''
    def readStatus(self):
        
        supCount = 0
        loadCount = 0
        resposCount = 0
        try:
            f = open("supinfo", mode='r')
            line = f.readline()
            lineList = line.split('|@|')
            supCount = lineList[0]
            loadCount = lineList[1]
            resposCount = lineList[2]   
        except Exception, e:
            pass
        return {"supCount":supCount, "loadCount":loadCount, "resposCount":resposCount}
    
########################################################################
class SupData(object):
    """供方，数据"""

    
    def readStatus(self, endtime):
        # busilog test
        #endtime = "201705222235"
        querySuccess = self.__calcuStatus(self.__rFileFromTail(endtime), endtime)
        # unit test for nginx log
        #endtime = '201705222240'
        queryTotal = self.__nCalcuStatus(self.__nFileFromTail(endtime) ,endtime)
        return dict({"querySuccess":querySuccess}, **queryTotal)
    
    # busilog 日志分析
    def __rFileFromTail(self, endtime):
        try:
            path = busilog + "." + time.strftime("%Y%m%d", time.localtime(time.time()))
            # busilog test
            #path = "/home/chinadep/busilog/busi.log.err.20170522"
            f = open(path, mode='r')
        except Exception, e:
            MSGERR["BUSILOG"] = "业务日志读取失败"
            return []
        # 步长
        step = b_step
        totalStep = step
        line = f.readline()
        size = len(line) + 1
        while step > s_b_step:
            try:
                f.seek(-totalStep*size, 2) 
                
                f.readline()
                curLine = f.readline()
                lineList = curLine.split('|@|')
                if lineList[2] + lineList[3][:-2] < endtime:
                    step = step/2
                    # 总 offset
                    totalStep = totalStep - step     
                else: 
                    # 快增满减
                    # 总 offset
                    totalStep = totalStep + step                     
            except Exception, e:
                if totalStep-step == 0:
                    f.seek(0)
                else:
                    f.seek(-(totalStep-step)*size , 2)
                result = f.readlines()[1:]
                f.close()
                return result                     
            
        f.seek(-(totalStep+step)*size, 2)
        result = f.readlines()[1:]
        f.close()
        return result
    
    
    def __calcuStatus(self, lines, endtime):
        print "busilog: ",len(lines)
        orderIDDic = self.__getTaskID()
        
        orderIDDic["excludeTaskID"] = 0
        for line in lines:
            lineList = line.split('|@|')
            if len(lineList) < 3:
                continue
            if  lineList[2] + lineList[3][:-2] == endtime and lineList[1] == '11':
                for item in lineList[6].split(","):
                    if item in orderIDDic.keys():
                        orderIDDic[item] = orderIDDic[item] + 1
                    else:
                        orderIDDic["excludeTaskID"] = orderIDDic["excludeTaskID"] + 1
        return {"taskID":orderIDDic.keys(), "Count":orderIDDic.values()}   
    
    def __getTaskID(self):
        """返回 {taskID:0......}"""
        taskIDDic = {}
        try:
            dom = minidom.parse(orderPath)
            orderDtlList = dom.getElementsByTagName('order_dtl_list')
            orderDtlInfos = orderDtlList[0].getElementsByTagName("order_dtl_info")

            for dltInfoNode in orderDtlInfos:
                nodes = dltInfoNode.getElementsByTagName("taskId")
                if nodes:
                    taskIDDic[nodes[0].childNodes[0].data] = 0
        except Exception, e:
            pass
        return taskIDDic
        
    #def __calcuStatus(self, lines, endtime):
        #orderIDDic = self.__getOrderIDDic()
        #count = { orderIDDic[key] : 0 for key in orderIDDic.keys() }
        #count["excludeOrder"] = 0
        #for line in lines:
            #lineList = line.split('|@|')
            #if len(lineList) < 3:
                #continue
            #if  lineList[2] + lineList[3][:-2] == endtime and lineList[1] == '21':
                #for item in lineList[6].split(","):
                    #if item in orderIDDic.keys():
                        #count[orderIDDic[item]] = count[orderIDDic[item]] + 1
                    #else:
                        #count["excludeOrder"] = count["excludeOrder"] + 1
        #return {"orderID":count.keys(), "count":count.values()}  
    
    #def __getOrderIDDic(self):
        #"""从订单配置文件名中获取订单号 返回{taskID:orderID...}"""
        #orderPath = "D:\\sample\\"
        
        #taskAndOrederDic = {}
        #if os.path.exists(orderPath):
            #fileList = os.listdir(orderPath)
            #for fileItem in fileList:
                #if os.path.isfile(orderPath + fileItem):
                    #if fileItem.startswith("order_route_") and fileItem.endswith(".xml"):
                        #taskAndOrederDic = dict(taskAndOrederDic, **self.__analyzeXML(orderPath, fileItem))
        #return taskAndOrederDic
    
    #def __analyzeXML(self, path, xmlFile):
        #""" 返回当前文件 {taskID:orderID...}"""
        #taskAndOrder = {}
        #try:
            #orderID = xmlFile.split("_")[2][:-4]
            #dom = minidom.parse(path + xmlFile)
            #svcInfoNodeList = dom.getElementsByTagName('svc_info')
            #taskIdStr = ''
            #for svcInfoNode in svcInfoNodeList:  
                #taskIdListNode = svcInfoNode.getElementsByTagName("taskIdList")[0]
                #taskIdNodes = taskIdListNode.getElementsByTagName("taskId") 
                #for node in taskIdNodes:
                    #taskAndOrder[node.childNodes[0].nodeValue] = orderID
        #except Exception, e:
            #pass
        #return taskAndOrder

    # nginx日志分析
    def __nFileFromTail(self, endtime):
        try:
            f = open(nginxlog, mode='r')
        except Exception, e:
            MSGERR["NGINXLOG"] = "NGINX日志读取失败"
            return []
        # 步长
        step = n_step
        totalStep = step
        line = f.readline()
        size = len(line) + 1
        while step > s_n_step:
            try:
                f.seek(-totalStep*size, 2) 
                
                f.readline()
                curLine = f.readline()
                lineList = curLine.split(" ")
                curTime = time.strftime("%Y%m%d%H%M",time.strptime(lineList[3][1:],'%d/%b/%Y:%H:%M:%S'))
                if  curTime < endtime:
                    step = step/2
                    # 总 offset
                    totalStep = totalStep - step
                else:  
                    # 快增满减
                    # 总 offset
                    totalStep = totalStep + step                     
            except Exception, e:
                if totalStep-step == 0:
                    f.seek(0)
                else:
                    f.seek(-(totalStep-step)*size , 2) 
                result = f.readlines()[1:]
                f.close()
                return result                         
            
        f.seek(-(totalStep+step)*size, 2)
        result = f.readlines()[1:]
        f.close()
        return result     

    def __nCalcuStatus(self, lines, endtime):
        print "nginx: ",len(lines)
        count = {}
        queryTotal = 0
        for line in lines:
            lineList = line.split(' ')
            if len(lineList) < 9 or len(lineList[3]) < 20:
                continue            
            curTime =  lineList[3][1:3] + lineList[3][13:15] +  lineList[3][16:18] #time.strftime("%Y%m%d%H%M",time.strptime(lineList[3][1:],'%d/%b/%Y:%H:%M:%S'))
            if curTime == endtime[-6:] :
                if lineList[6] == path:
                    queryTotal = queryTotal + 1
                    if not count.has_key(lineList[8]):
                        count[lineList[8]] = 1
                    else:
                        count[lineList[8]] = count[lineList[8]] + 1
        if queryTotal > sup_qps:
            MSGWARN["SUPQPS"] = "请求供方总数超过" + str(sup_qps)
        return {"code":count.keys(), "codeCount": count.values(), "queryTotal": queryTotal}     

if __name__ == "__main__" :
    '''this is the main method'''
    supStatus = SupStatus()
    supStatus.readStatus()
    print supStatus.toJson()
