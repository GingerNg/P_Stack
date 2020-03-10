# -*- coding:utf-8 -*-
# Author:  chenhailong --<chenhailong@chinadep.com>
# Created: 2017/5/19    
#
from BaseStatus import BaseStatus
from tools import obj2Dic
import time
import os  
from collections import namedtuple  
from constants import cpu_rate, mem_rate, load_rate, disk_rate
########################################################################
disk_ntuple = namedtuple('partition',  'device mountpoint fstype')  
usage_ntuple = namedtuple('usage',  'total used free percent') 
MSGERR = {}
MSGWARN = {}
class SysStatus(BaseStatus):
    """系统信息"""
 
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        super(BaseStatus, self).__init__()
        self.CPU = ""
        self.Mem = ""
        self.Disk = ""
        self.Load = ""
    def readStatus(self):
        self.CPU = self.__cpu_stat()
        self.Mem = self.__memory_stat()
        self.Disk = self.__disk_stat()
        self.Load = self.__load_stat()
    def toJson(self):
        """"""
        jsonData = obj2Dic([self])[0]

        jsonData["MSGERR"] = MSGERR
        jsonData["MSGWARN"] = MSGWARN
        return  jsonData 
    #----------------------------------------------------------------------
    def __memory_stat(self):  
        '''mem info'''
        try:
            mem = {}  
            f = open("/proc/meminfo")  
            lines = f.readlines()  
            f.close()  
            for line in lines:  
                if len(line) < 2: continue  
                name = line.split(':')[0]  
                var = line.split(':')[1].split()[0] 
                if name in ['MemTotal', 'MemFree', 'Buffers', 'Cached']:
                    mem[name] = long(var) / 1024.0  
            mem['MemUsed'] = mem['MemTotal'] - mem['MemFree'] - mem['Buffers'] - mem['Cached']  
            if mem['MemUsed'] / mem['MemTotal'] > mem_rate:
                MSGWARN["MEM"] = "内存使用率超过" + str(mem_rate)
        except Exception, e:
            MSGERR["MEM"] = "内存使用情况读取失败"
            return ""        
        return mem     
    
    def __disk_stat(self):  
        '''disk info'''
        try:
            diskList = []
            lines = os.popen("df -hl").readlines()
            lineOne = lines[0].split()
            for item in lines[1:]:
                line = item.split()
                diskDic = {}
                diskDic[lineOne[0]] = line[0]
                diskDic[lineOne[1]] = line[1]
                diskDic[lineOne[2]] = line[2]
                diskDic[lineOne[3]] = line[3]
                diskDic[lineOne[4][:-1]] = "0." + line[4][:-1]
                diskDic[lineOne[5]] = line[5]
                diskList.append(diskDic)
                if diskDic[lineOne[4][:-1]] > str(disk_rate):
                
                    MSGWARN["DISK"] = "磁盘使用率超过" + str(disk_rate)
        except Exception, e:
            MSGERR["DISK"] = "磁盘使用情况读取失败"
            return ""
        return diskList  

    def __load_stat(self): 
        '''load info'''
        try:
            loadavg = {}  
            f = open("/proc/loadavg")  
            con = f.read().split()  
            f.close()  
            loadavg['lavg_1']=con[0]  
            loadavg['lavg_5']=con[1]  
            loadavg['lavg_15']=con[2]  
            loadavg['nr']=con[3]  
            loadavg['last_pid']=con[4]  
            if float(con[2]) > load_rate:
                MSGWARN["LOAD"] = "lavg_15负载超过" + str(load_rate)
        except Exception, e:
            MSGERR["LOAD"] = "负载使用情况读取失败"
            return ""
        return loadavg  
    
    def _read_cpu_usage(self):  
        """从/proc/stat读取当前系统cpu使用率""" 
        try:  
            fd = open("/proc/stat", 'r')  
            lines = fd.readlines()  
        finally:  
            if fd:  
                fd.close()  
        
        cpuList = []
        for line in lines:  
            l = line.split()
            if l[0].startswith('cpu'):  
                cpuList.append(l)  
        return cpuList  
       
    def __cpu_stat(self):  
        """ 
        get cpu avg used by percent 
        """ 
        try:
            cpustr1=self._read_cpu_usage()  
            time.sleep(0.1)  
            cpustr2=self._read_cpu_usage()  
               
            cpuRate = []
            for item in range(len(cpustr1)):
                cpustritem1 = cpustr1[item]
                usni1 = long(cpustritem1[1])+long(cpustritem1[2])+long(cpustritem1[3])+long(cpustritem1[5])\
                      +long(cpustritem1[6])+long(cpustritem1[7])+long(cpustritem1[4])  
                usn1 = long(cpustritem1[1])+long(cpustritem1[2])+long(cpustritem1[3]) 
                
                cpustritem2 = cpustr2[item]
                usni2 = long(cpustritem2[1])+long(cpustritem2[2])+long(cpustritem2[3])+long(cpustritem2[5])\
                      +long(cpustritem2[6])+long(cpustritem2[7])+long(cpustritem2[4])  
                usn2 = long(cpustritem2[1])+long(cpustritem2[2])+long(cpustritem2[3])
                rate = round(1.0*(usn2-usn1)/(usni2-usni1),4)
                cpuRateDic =  {cpustritem1[0]: rate}
                cpuRate.append(cpuRateDic)
                #  如果 CPU 使用率 超过
                if cpustritem1[0] == 'cpu':
                    if rate > cpu_rate:
                        MSGWARN["CPU"] = "cpu使用率超过" + str(cpu_rate)
        except Exception, e:
            MSGERR["CPU"] = "CPU使用情况读取失败"
            return ""
        return cpuRate 
    

    ##获取当前操作系统下所有磁盘  
    #def __disk_partitions(self, all=False):  
        #"""Return all mountd partitions as a nameduple. 
        #If all == False return phyisical partitions only. 
        #"""  
        #phydevs = []  
        #f = open("/proc/filesystems", "r")  
        #for line in f:  
            #if not line.startswith("nodev"):  
                #phydevs.append(line.strip())  
      
        #retlist = []  
        #f = open('/etc/mtab', "r")  
        #for line in f:  
            #if not all and line.startswith('none'):  
                #continue  
            #fields = line.split()  
            #device = fields[0]  
            #mountpoint = fields[1]  
            #fstype = fields[2]  
            #if not all and fstype not in phydevs:  
                #continue  
            #if device == 'none':  
                #device = ''  
            #ntuple = disk_ntuple(device, mountpoint, fstype)  
            #retlist.append(ntuple)  
        #return retlist  
    ##统计某磁盘使用情况，返回对象  
    #def __disk_usage(self, path):  
        #"""Return disk usage associated with path."""  
        #st = os.statvfs(path)  
        #free = (st.f_bavail * st.f_frsize)  / 1024.0 / 1024.0
        #total = (st.f_blocks * st.f_frsize)  / 1024.0 / 1024.0
        #used = (st.f_blocks - st.f_bfree) * st.f_frsize / 1024.0 / 1024.0
        #try:  
            #percent = ret = (float(used) / total) * 100 
            #if percent > disk_rate:
                #MSGWARN["DISK"] = "磁盘使用率超过" + disk_rate
        #except Exception, e:  
            #percent = 0  
        #return usage_ntuple(total, used, free, round(percent, 1))  
    
if __name__ == "__main__" :
    '''this is the main method'''
    sysStatus = SysStatus()
    sysStatus.readStatus()
    print sysStatus.toJson()
