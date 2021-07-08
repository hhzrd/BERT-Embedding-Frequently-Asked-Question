# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2020-08-20 11:09:45
LastEditTime: 2021-07-08 11:50:42
Description: kill 进程
'''
import os


def kill_port(port):
    '''
    @Author: xiaoyichao
    @param {*}
    @Description: 根据端口号杀掉程序
    ''' 
    find_kill = "kill -9 $(lsof -i:%d -t)" % port
    try:
        result = os.popen(find_kill)
        print("%d端口程序kill 成功" % port)
        return result.read()
    except Exception:
        print("%d端口程序kill 失败" % port)