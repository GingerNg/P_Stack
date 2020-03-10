# -*- coding:utf-8 -*-
from BaseStatus import BaseStatus
from constants import QUERY_RESULT, BUSI_LOG_PATH, orderPath, DEM_ROLE
from tools import obj2Dic
import os
from xml.dom import minidom

taskOrderMap = dict()

class DemStatus(BaseStatus):
    def __init__(self):
        self.taskIds = list()
        self.requestOk = list()         #producer  状态24 code：000000
        self.requestFail =list()        #producer  状态22 code: 030002
        self.requestKafka = list()      #producer  状态22 code: 031006
        self.requestSup = list()        #consumer  状态ALL
        self.requestCacheSucc = list()  #consumer  状态23 code:001000
        self.requestCacheFail = list()  #consumer  状态22 code:001000

    def readStatus(self):
        requestInfo = self.__requestInfo()
        for record in requestInfo:
            self.taskIds.append(record)
            self.requestOk.append(requestInfo[record][0])
            self.requestFail.append(requestInfo[record][1])
            self.requestKafka.append(requestInfo[record][2])
            self.requestSup.append(requestInfo[record][3])
            self.requestCacheSucc.append(requestInfo[record][4])
            self.requestCacheFail.append(requestInfo[record][5])

    def toJson(self):
        return obj2Dic([self])[0]

    def __requestInfo(self):
        result = dict() #use a dict to store result, format is {orderId:(okCount, failCount)}
        try:
            with open(QUERY_RESULT, 'r') as f:
                lines = f.readlines()
                print "len(lines)", len(lines), lines
                if len(lines) < 2:
                    raise Exception
                #中间部分
                for i in range(0,len(lines)-2):
                    s = str(lines[i]).strip()
                    if len(s) > 0:
                        taskIdList = s.split(" ")
                        num = int(taskIdList[0])
                        taskId = taskIdList[1]
                        status = taskIdList[2]
                        code = taskIdList[3]
                        print taskIdList
                        if result.has_key(taskId):
                            if DEM_ROLE == "producer":
                                if status == '24' and code == '000000':
                                    result[taskId][0] = result[taskId][0] + num
                                if status == '22' and code == '030002':
                                    result[taskId][1] = result[taskId][1] + num
                                if status == '22' and code == '031006':
                                    result[taskId][2] = result[taskId][2] + num
                            else:
                                result[taskId][3] = result[taskId][3] + num
                                if status == '23' and code == '001000':
                                    result[taskId][4] = result[taskId][4] + num
                                if status == '22' and code == '001000':
                                    result[taskId][5] = result[taskId][5] + num
                        else:
                            statusList = [0, 0, 0, 0, 0, 0]
                            if DEM_ROLE == "producer":
                                if status == '24' and code == '000000':
                                    statusList[0] = statusList[0] + num
                                if status == '22' and code == '030002':
                                    statusList[1] = statusList[1] + num
                                if status == '22' and code == '031006':
                                    statusList[2] = statusList[2] + num
                            else:
                                statusList[3] = statusList[3] + num
                                if status == '23' and code == '001000':
                                    statusList[4] = statusList[4] + num
                                if status == '22' and code == '001000':
                                    statusList[5] = statusList[5] + num
                            result[taskId] = statusList
                return result
        except Exception, e:
            print "fail to get service info" + str(e)
            return result

    def __updateRecord(self, taskId, code, result):
        orderId = self.__lookup(taskId)
        if orderId == -1:
            return

        if code == '23' or code == '22':
            if result.get(orderId, -1) != -1:
                result[orderId][0] += 1
            else:
                result[orderId] = [1, 0]
        if code == '24':
            if result.get(orderId, -1) != -1:
                result[orderId][1] += 1
            else:
                result[orderId] = [0, 1]

    def __lookup(self, taskId):
        if taskOrderMap.get(taskId, -1) != -1:
            return taskOrderMap[taskId]
        else:
            self.__updateMap()
            return taskOrderMap.get(taskId, -1)

    def __updateMap(self):
        if os.path.exists(orderPath):
            fileList = os.listdir(orderPath)
            for fileItem in fileList:
                if os.path.isfile(orderPath+fileItem) and fileItem.startswith("order_route_") and fileItem.endswith(".xml"):
                    orderId = fileItem.split("_")[2][:-4]
                    try:
                        dom = minidom.parse(orderPath + fileItem)
                        svcInfoNodeList = dom.getElementsByTagName('svc_info')
                        for svcInfoNode in svcInfoNodeList:
                            taskIdListNode = svcInfoNode.getElementsByTagName("taskIdList")[0]
                            taskIdNodes = taskIdListNode.getElementsByTagName("taskId")
                            for node in taskIdNodes:
                                taskOrderMap[node.childNodes[0].nodeValue] = orderId
                    except Exception, e:
                        pass



if __name__ == "__main__":
    """main entry"""
    demStatus = DemStatus()
    demStatus.readStatus()
    print demStatus.toJson()
