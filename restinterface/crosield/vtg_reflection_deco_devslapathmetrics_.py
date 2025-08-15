#!/usr/bin/python
#coding: UTF-8

from .vtg_sdwan_ import *
from .vtg_spokegroup_ import *
from .vtg_template_ import *
from .vtg_device_ import *
from ...director.reflection_deco_ import VTGThread_reflectionDeco
from .vtg_appliance_ import *

vtg_devsla_ = []
vtg_devsla_set = set()
vtg_devsla_id_ = []
import pandas as pd

#
def devsla(self):
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
    _, devtemplateName = device.templateName_()
    # print(devtemplateName)
    _, deviceOrgName = device.deviceOrgName_()
    _, workflowStatus = device.workflowStatus_()
    template = VTG_template(pst = devtemplateName)
    _, devSpoke = template.spoke_()
    if (deviceOrgName == self.__deviceOrg and "Deployed" == workflowStatus):
        #print(devSpoke)
        item = devSpoke
        sg = VTG_spokegroup(deviceorg = self.__deviceOrg)
        _, _ = sg.devspokegroup_(devSpoke)
        devspokegrouphubs = sg.devspokegroup_hubs_()
        sdn = VTG_sdwan(devicename = self.__deviceName, deviceorg = self.__deviceOrg)
        sdn.devsla_path_metrics_aggregated_last_1m_brief_(devspokegrouphubs)


def devslainspectorModel(orgName):
    appliance = VTG_appliance(deviceorg = orgName)
    _, d = appliance.location_
    data = json.loads(d)
    print(json.dumps(data, indent=4))
    devicesName_ = [ tc['applianceName'] for tc in data["List"]['value'] if tc['type'] != 'controller' and tc['type'] != 'hub' ]
    # 2020.3.10 clear function
    global vtg_devsla_
    vtg_devsla_.clear()
    global vtg_devsla_set
    vtg_devsla_set.clear()
    global vtg_devsla_id_
    vtg_devsla_id_.clear()
    setattr(VTGThread_reflectionDeco, "run", devsla)
    thread_table = []
    for item in devicesName_:
        delay = "0"
        thread_post = delay + ':' + item + ':' + orgName
        refdeco = VTGThread_reflectionDeco(thread_name = ("%s" % thread_post))
        thread_table.append(refdeco)
    for thread in thread_table:
        thread.start()
    for thread in thread_table:
        thread.join()
    ## self.file_message(' Tubes Visibility inspect by : ' + orgName +  ' execute startup...')
    ## self.file_message(' Tubes Visibility inspect on : ' + orgName +  ' execute during ' + str((eT - sT).seconds) + ' sec')

#