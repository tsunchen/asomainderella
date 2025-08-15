#!/usr/bin/python
#coding: UTF-8

from .vtg_interfaces_ import *
from ...director.reflection_deco_ import VTGThread_reflectionDeco
from .vtg_appliance_ import *

vtg_interface_monitor_intf_ = []
vtg_interface_monitor_intfset = set()
vtg_interface_monitor_intf_id_ = []
import pandas as pd
#

def interface_aurora(self):
    thread_posted = threading.current_thread().getName()
    self.__delay = int(thread_posted.split(":")[0])
    self.__deviceName = thread_posted.split(":")[1]
    self.__deviceOrg = thread_posted.split(":")[2]
    time.sleep(self.__delay)
    ##print("[%s]" % threading.current_thread().getName())
    dev = VTG_device(devicename = self.__deviceName)
    _, deviceOrgName = dev.deviceOrgName_()
    if (deviceOrgName == self.__deviceOrg):
        # 2020.3.23 devicesName -> org_intf
        intf = VTG_interfaces(devicename = self.__deviceName, deviceorg = self.__deviceOrg)
        d2, d = intf.unit_
        if (200 == d2):
            data = json.loads(d)
            text_intf_ = ""
            text_intf_brief_ = ""
            for butt in data['org_intf']:
                if "up" != butt['if-admin-status']: # != butt['if-oper-status']:
                    #text = ' ! ' + butt['network'] + ': ' + butt['name'] + ' ' + self.__deviceName + '\n'
                    # 2020.4.29 PPPoE no network attribute
                    text = ' ! ' + butt['vrf'] + ': ' + butt['name'] + ' ' + self.__deviceName + '\n'
                    text_intf_ = text_intf_ + text
                    text_intf_brief_ = butt['vrf']
                    vtg_interface_monitor_intf_id_.append(self.__deviceName)
                    vtg_interface_monitor_intf_.append(text_intf_brief_+' ')
            print(text_intf_, self.__deviceName, self.__deviceOrg)
        else:
            print(" No Any Up-Interface Info: " + self.__deviceName + ' ' + self.__deviceOrg)
            vtg_interface_monitor_intf_id_.append(self.__deviceName)
            vtg_interface_monitor_intf_.append("!")
        # 2020.6.1
        data = {'interface': vtg_interface_monitor_intf_, 'id': vtg_interface_monitor_intf_id_}
        example = pd.DataFrame(data = data)
        ex1 = example.groupby('id').interface.sum().reset_index('id')
        size_ex1 = [ item.count(" ") for item in ex1.interface ]
        ex1['size'] = size_ex1
        print(ex1)


def interfaceinspectorModel(orgName):
    appliance = VTG_appliance(deviceorg = orgName)
    _, d = appliance.location_()
    data = json.loads(d)
    print(json.dumps(data, indent=4))
    devicesName_ = [ tc['applianceName'] for tc in data["List"]['value'] if tc['type'] != 'controller' ]
    # 2020.3.10 clear function
    global vtg_interface_monitor_intf_
    vtg_interface_monitor_intf_.clear()
    global vtg_interface_monitor_intfset
    vtg_interface_monitor_intfset.clear()
    global vtg_interface_monitor_intf_id_
    vtg_interface_monitor_intf_id_.clear()
    setattr(VTGThread_reflectionDeco, "run", interface_aurora)
    for item in devicesName_:
        delay = "0"
        thread_post = delay + ':' + item + ':' + orgName
        refdeco = VTGThread_reflectionDeco(thread_name = ("%s" % thread_post))
        refdeco.start()
    ##self.file_message(' Aurora Interfaces inspect on : ' + orgName +  ' execute startup...')



#