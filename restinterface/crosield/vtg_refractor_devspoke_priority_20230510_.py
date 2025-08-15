#!/usr/bin/python
#coding: UTF-8
import time, os
import pandas as pd
from .vtg_sdwan_ import *
from .vtg_spokegroup_ import *
from .vtg_template_ import *
from .vtg_device_ import *
from ...director.refractor_ import VTGThread_refractor, maximize
from .vtg_appliance_ import *
from tqdm import tqdm

def dfprint(data):
    example = pd.DataFrame(data = data)
    example.set_index('device', inplace = True)
    # print(example.sort_values(by = 'spOke'))
    ex_df_devspokepriorityinspector_ = example.groupby('device', as_index = False).apply(fmttab_)
    print('\r{}'.format(ex_df_devspokepriorityinspector_), end = '')
    print()


def fmttab_(data):
    df = data.sort_values(by = 'spOke',ascending = True)
    return df


def devspokepriorityinspectorModel(orgName):
    # 2022.12.13 globalless
    setattr(VTGThread_refractor, "vtg_devspokepriority_", [])
    setattr(VTGThread_refractor, "vtg_devspokepriority_set", set())
    setattr(VTGThread_refractor, "vtg_devspokepriority_id_", [])
    appliance = VTG_appliance(deviceorg = orgName)
    _, d = appliance.location_
    data = json.loads(d)
    print(json.dumps(data, indent = 4))
    try:
        devicesName_ = [ tc['applianceName'] for tc in data["List"]['value'] if tc['type'] != 'controller' and tc['type'] != 'hub' ]
    except Exception as e:
        # print(e)
        print(" Select the tenant priorly, please. ")
    else:
        # 2021.1.20 _refractor
        setattr(VTGThread_refractor, "run", devspokepriority)
        thread_table = [ maximize(item, orgName) for item in devicesName_ ]
        for thread in thread_table:
            thread.start()
        proc_bar = tqdm(thread_table)
        for p in proc_bar:
            # proc_bar.set_description('No.{}'.format(p))
            proc_bar.set_postfix({"SPOKE": '{}'.format(p)})
            p.join()
        dfprint({'device': VTGThread_refractor.vtg_devspokepriority_, 'spOke': VTGThread_refractor.vtg_devspokepriority_id_})


def devspokepriority(self):
    self.__delay = threading.current_thread().delay
    self.__deviceName = threading.current_thread().deviceName
    self.__deviceOrg = threading.current_thread().deviceOrg
    time.sleep(int(self.__delay))
    # 2020.9.2 devicesName -> devSpoke(Deployed)
    device = VTG_device(devicename = self.__deviceName)
    _, devtemplateName = device.templateName_()
    # print(devtemplateName)
    _, deviceOrgName = device.deviceOrgName_()
    _, workflowStatus = device.workflowStatus_()
    template = VTG_template(pst = devtemplateName)
    _, devSpoke = template.spoke_()
    if all([ deviceOrgName == self.__deviceOrg, "Deployed" == workflowStatus, devSpoke is not None ]):
        # print(devSpoke)
        item = devSpoke
        len_previous_vtg_devspokepriority_set_ = len(self.vtg_devspokepriority_set)
        # item += "[100%]"
        # 2020.10.20 Spoke Prime
        sg = VTG_spokegroup(deviceorg = self.__deviceOrg)
        _, _ = sg.devspokegroup_(devSpoke)
        ## devspokegrouphubs = sg.devspokegroup_hubs_()
        sdn = VTG_sdwan(devicename = self.__deviceName, deviceorg = self.__deviceOrg)
        # 2020.10.21 devspokegroup_hubs_
        devspokegrouphub_priority = sg.devspokegroup_hub_priority_()
        itemres = [ sdn.devsla_path_metrics_aggregated_last_1m_brief_prime_(devspokegrouphub_priority) for _ in range(2) ] # 2022.7.26 deep multipuly
        item += '* ' + ",".join(set(itemres))
        # + item append
        if "+" in item:
            self.vtg_devspokepriority_set.add(item)
            len_next_vtg_devspokepriority_set_ = len(self.vtg_devspokepriority_set)
            self.vtg_devspokepriority_id_.append(str(item))
            self.vtg_devspokepriority_.append("" + self.__deviceName)