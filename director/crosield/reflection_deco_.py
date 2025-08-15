#!/usr/bin/python
#coding: UTF-8

from threading import Thread

#
class VTGThread_reflectionDeco(Thread):
    # 2020.7.4  reflection_deco
    # 2020.2.19 replace with def __init__(self, thread_name, delay, devicename, deviceorg):
    # 2020.2.14 thread adding with devicetypelist 
    #

    def __init__(self, *args, **kwargs):
        #self.gNum_of_thread = 10000000
        super().__init__(name = kwargs['thread_name'])

