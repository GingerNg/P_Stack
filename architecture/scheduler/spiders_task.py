#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
 @File: spiders_task.py
 @author: ginger 
 @software: PyCharm  
 @time: 17-11-26 下午9:34
 @desc: 
"""
from architecture.scheduler import spiders_executor
from utils import file_util

class spiders_tasks():
    def __init__(self, target_host, resource_pos, py_paths, result_path = None):
        self.__executor = spiders_executor()
        self.__sender = message_sender(target_host, resource_pos)
        self.__target_host = target_host
        self.__resource_pos = resource_pos
        self.__task_paths = py_paths
        self.__result_path = result_path
        self.__initialize()

    def __initialize(self):
        py_path_list = file_util.find_all_file(self.__task_paths)
        for i in range(0, len(py_path_list)):
            self.__executor.push(py_path_list[i])

    def execute_save_send_task_result(self, path):
        self.__executor.work_shell()
        if self.__result_path is None:
            self.__result_path = file_util.make_directory_by_time()
        file_util.move_file('/home/XXX', self.__result_path)
        files_size = file_util.get_all_file_size(self.__result_path)
        # while not self.__executor.done_queue.empty():
        #     self.__save_result_as_text(path=self.__result_path, result=self.__executor.done_queue.get())
        self.__save_result_as_text(self.__result_path, files_size)
        self.__send_task_result()

        # todo

    def __save_result_as_text(self, result):
        pass

    def __send_task_result(self, data):
        self.__sender.message_send(data)

if __name__ == '__main__':
    spiders_tasks = spiders_tasks('XX:XXX','mail_task','/home/XXXX/py_path',"20171126")
    spiders_tasks.execute_save_send_task_result()