#!/usr/bin/python
#coding: UTF-8
from threading import Thread
from threading import Lock


'''
Type1:
        ...
        
        setattr(VTGThread_refractor, "run", wan_snort)
        thread_table = [ threadTab(item, orgName) for item in devicesName_ ]
        ...

def threadTab(threadItem, org):
    delay = "0"
    thread_post = threadItem
    refrac = VTGThread_refractor(thread_name = ("%s" % thread_post))
    refrac.__setattr__("delay", delay)
    refrac.__setattr__("deviceName", threadItem)
    refrac.__setattr__("deviceOrg", org)
    return refrac


Type2:
        ...
        for item in devicesName_:
            delay = "0"
            thread_post = item
            refrac = VTGThread_refractor(thread_name = ("%s" % thread_post))
            refrac.__setattr__("delay", delay)
            refrac.__setattr__("deviceName", item)
            refrac.__setattr__("deviceOrg", orgName)
            refrac.start()
        for thread in thread_table:
            thread.start()
        for thread in thread_table:
            thread.join()


Type3: from tqdm import tqdm

    thread_table = [ maximize(item, orgName) for item in devicesName_ ]
    for thread in thread_table:
        thread.start()
    proc_bar = tqdm(thread_table)
    for p in proc_bar:
        # proc_bar.set_description('No.{}'.format(p))
        proc_bar.set_postfix({"ParseLan": '{}'.format(p)})
        p.join()

'''
def thread_chain(*args, **kwargs):
    for threadjob_ in args:
        yield from threadjob_


def maximize(item, orgName):
    delay = "0"
    refrac = VTGThread_refractor(thread_name = ("%s" % (thread_post := item)))
    refrac.__setattr__("delay", delay)
    refrac.__setattr__("deviceName", item)
    refrac.__setattr__("deviceOrg", orgName)
    return refrac


class VTGThread_refractor(Thread):
    # 2021.1.20 refractor
    # 2020.7.4  reflection_deco
    # 2020.2.19 replace with def __init__(self, thread_name, delay, devicename, deviceorg):
    # 2020.2.14 thread adding with devicetypelist 
    #

    def __init__(self, *args, **kwargs):
        # implict self.__gNum_of_thread = 10000000
        # implict self.__delay
        # implict self.__deviceName
        # implict self.__deviceOrg
        # implict self.__iThread
        super().__init__(name = kwargs['thread_name'])