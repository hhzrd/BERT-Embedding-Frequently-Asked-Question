# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2020-08-20 11:09:45
LastEditTime: 2021-06-18 15:36:43
Description: kill 进程
'''
import os


def kill_port(port):

    find_kill = "kill -9 $(lsof -i:%d -t)" % port
    print(find_kill)
    result = os.popen(find_kill)
    return result.read()
