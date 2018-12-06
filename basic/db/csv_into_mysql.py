# encoding: utf-8


import pymysql as MySQLdb

MEM_ORDER_INFO_COLS = ("demMemId", "demMemName", "supMemId", "supMemName", "orderId", "name", "status", "settModCd", "orderInitTime", "orderConfirmTime", "orderEffectDate", "orderExpiryDate", "needCache", "cacheTime", "settPeriod", "settType", "prdtType")
MEM_ORDER_INFO_QS = """
SELECT
%s
FROM
mall_mem_order_info
WHERE
orderId='%s'
""" % (','.join(MEM_ORDER_INFO_COLS), '%s')

MEM_ORDER_DTL_INFO_COLS = ("taskId", "orderId", "connObjId", "connObjNo", "connObjCatCd", "expectPrice", "prdtIdCd", "supMemId")
MEM_ORDER_DTL_INFO_QS = """
SELECT
%s
FROM
mall_mem_order_dtl_info
WHERE
taskId='%s'
""" % (','.join(MEM_ORDER_DTL_INFO_COLS), '%s')

PRDT_VAL_MODE_COLS = ("connObjNo", "valuationModeCd", "valuationPrice")
PRDT_VAL_MODE_QS = """
SELECT
%s
FROM
sup_prdt_val_mode
WHERE
connObjNo='%s'
""" % (','.join(PRDT_VAL_MODE_COLS), '%s')

ORDER_TASKID_QS = """
SELECT DISTINCT taskId FROM mall_mem_order_dtl_info WHERE orderId='%s'
"""

INSERT_HOTEL = """
Insert into hotel_ctrip 
(hotel_id,hotel_name,hotel_level_ctrip,hotel_level,hotel_diamond,hotel_address,
hotel_province,hotel_city,hotel_district,hotel_location,hotel_price,hotel_price_span,hotel_feature,hotel_country)
values (%s)
"""
import threading
lock = threading.Lock()
def getConnection():
    lock.acquire()
    conn = MySQLdb.connect(host="XX.XX.XX.XX", port=3306, user="root", passwd="XXX",charset='utf8')
    try:
        conn.select_db("knowledge_mix")
    except BaseException as e:
        conn.close()
        raise e
    lock.release()
    return conn


def queryMemOrderInfo(conn, orderId):
    """查询订单表"""
    cursor = conn.cursor()
    cursor.execute(MEM_ORDER_INFO_QS % (orderId, ))
    row = cursor.fetchone()
    if row:
        return dict(zip(MEM_ORDER_INFO_COLS, row))
    else:
        return None


def queryMemOrderDtlInfo(conn, taskId):
    """查询订单明细表"""
    cursor = conn.cursor()
    cursor.execute(MEM_ORDER_DTL_INFO_QS % (taskId, ))
    row = cursor.fetchone()
    if row:
        return dict(zip(MEM_ORDER_DTL_INFO_COLS, row))
    else:
        return None


def queryPrdtValMode(conn, connObjNo):
    """查询可供产品计价方式"""
    cursor = conn.cursor()
    cursor.execute(PRDT_VAL_MODE_QS % (connObjNo, ))
    row = cursor.fetchone()
    if row:
        return dict(zip(PRDT_VAL_MODE_COLS, row))
    else:
        return None


def queryTaskIdsByOrderId(conn, orderId):
    taskIds = []

    sql = ORDER_TASKID_QS % (orderId,)
    cursor = conn.cursor()
    cursor.execute(sql)
    for row in cursor.fetchall():
        taskIds.append(row[0])

    cursor.close()
    return taskIds

def insertHotel(conn, hotel):
    sql = INSERT_HOTEL % (",".join(hotel))
    # print sql
    cursor = conn.cursor()
    cursor.execute(sql)
    cursor.close()
    # conn.commit()

import os
def find_all_file(directory):
    list_path = os.listdir(directory)
    all_file_path = []
    for i in range(0,len(list_path)):
        path = os.path.join(directory,list_path[i])
        if os.path.isfile(path):
            all_file_path.append(path)
    return all_file_path

def csv_into_mysql(csv_path):
    conn = getConnection()
    with open(csv_path) as f:
        datareader = csv.reader(f);
        for hotel in list(datareader):
            ii = []
            for item in hotel:
                ii.append("'"+item+"'".encode("utf8"))
            print (",".join(ii))
            try:
                insertHotel(conn,ii)
            except Exception as e:
                print (e.message)
                continue
        conn.commit()

import csv
if __name__ == '__main__':

    file_path_list = find_all_file("PATH")
    print (file_path_list[1])
    print (len(file_path_list))
    for csv_path in file_path_list:
        csv_into_mysql(csv_path)
