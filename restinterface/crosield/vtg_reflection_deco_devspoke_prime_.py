#!/usr/bin/python
#coding: UTF-8

import time, os

from .vtg_sdwan_ import *
from .vtg_spokegroup_ import *
from .vtg_template_ import *
from .vtg_device_ import *

from ...director.reflection_deco_ import VTGThread_reflectionDeco

vtg_devspokeprime_ = []
vtg_devspokeprime_set = set()
vtg_devspokeprime_id_ = []
import pandas as pd

#
def devspokeprime(self):
    # 2020.7.4 reflection_deco
    ##print("[%s]" % threading.current_thread().getName())
    thread_posted = threading.current_thread().getName()
    #print("[%s]" % thread_posted)
    self.__delay = int(thread_posted.split(":")[0])
    self.__deviceName = thread_posted.split(":")[1]
    self.__deviceOrg = thread_posted.split(":")[2]
    time.sleep(self.__delay)
    # 2020.9.2 devicesName -> devSpoke(Deployed)
    device = VTG_device(devicename = self.__deviceName)
    rn, devtemplateName = device.templateName_()
    #print(devtemplateName)
    rn, deviceOrgName = device.deviceOrgName_()
    rn, workflowStatus = device.workflowStatus_()
    template = VTG_template(pst = devtemplateName)
    rn, devSpoke = template.spoke_()
    if (deviceOrgName == self.__deviceOrg and "Deployed" == workflowStatus):
        #print(devSpoke)
        item = devSpoke
        len_previous_vtg_devspokeprime_set_ = len(vtg_devspokeprime_set)
        # item += "[100%]"
        # 2020.10.20 Spoke Prime
        sg = VTG_spokegroup(deviceorg = self.__deviceOrg)
        rn, sgdev = sg.devspokegroup_(devSpoke)
        ##devspokegrouphubs = sg.devspokegroup_hubs_()
        sdn = VTG_sdwan(devicename = self.__deviceName, deviceorg = self.__deviceOrg)
        # 2020.10.21 devspokegroup_hubs_
        devspokegrouphub_prime = sg.devspokegroup_hub_prime_()
        item += sdn.devsla_path_metrics_aggregated_last_1m_brief_prime_(devspokegrouphub_prime) ##devspokegrouphubs)
        #
        # + item append
        if "+" in item:
            vtg_devspokeprime_set.add(item)
            len_next_vtg_devspokeprime_set_ = len(vtg_devspokeprime_set)
            vtg_devspokeprime_id_.append(str(item))
            vtg_devspokeprime_.append("" + self.__deviceName)
        '''
        #
        vtg_devspokeprime_set.add(item)
        len_next_vtg_devspokeprime_set_ = len(vtg_devspokeprime_set)
        vtg_devspokeprime_id_.append(str(item))
        #
        vtg_devspokeprime_.append("" + self.__deviceName)
        if (len_previous_vtg_devspokeprime_set_ == len_next_vtg_devspokeprime_set_):
            print("!")
            for itembasic in sorted(vtg_devspokeprime_):
                if ( item in itembasic ):
                    print( "the %s exists on once more configuration: %s" % (item, itembasic))
            print(".")
        else:
            print(item, self.__deviceName)
        '''
        # 2020.9.2
        data = {'device': vtg_devspokeprime_, 'spoke': vtg_devspokeprime_id_}
        example = pd.DataFrame(data = data)
        print(example.sort_values(by = 'spoke'))





#


