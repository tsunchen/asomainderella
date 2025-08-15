#!/usr/bin/python
#coding: UTF-8

import time, os
import pandas as pd

from .vtg_sdwan_ import *
from .vtg_spokegroup_ import *
from .vtg_template_ import *
from .vtg_device_ import *

from ...director.reflection_deco_ import VTGThread_reflectionDeco

vtg_devspokepriority_ = []
vtg_devspokepriority_set = set()
vtg_devspokepriority_id_ = []


#
def devspokepriority(self):
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
        len_previous_vtg_devspokepriority_set_ = len(vtg_devspokepriority_set)
        # item += "[100%]"
        # 2020.10.20 Spoke Prime
        sg = VTG_spokegroup(deviceorg = self.__deviceOrg)
        rn, sgdev = sg.devspokegroup_(devSpoke)
        ##devspokegrouphubs = sg.devspokegroup_hubs_()
        sdn = VTG_sdwan(devicename = self.__deviceName, deviceorg = self.__deviceOrg)
        # 2020.10.21 devspokegroup_hubs_
        devspokegrouphub_priority = sg.devspokegroup_hub_priority_()
        #
        item += sdn.devsla_path_metrics_aggregated_last_1m_brief_prime_(devspokegrouphub_priority)
        #
        # + item append
        if "+" in item:
            vtg_devspokepriority_set.add(item)
            len_next_vtg_devspokepriority_set_ = len(vtg_devspokepriority_set)
            vtg_devspokepriority_id_.append(str(item))
            vtg_devspokepriority_.append("" + self.__deviceName)
        # 
        df_devspokepriorityinspector = {'device': vtg_devspokepriority_, 'spoke': vtg_devspokepriority_id_}
        example = pd.DataFrame(data = df_devspokepriorityinspector)
        print(example.sort_values(by = 'spoke'))







#


