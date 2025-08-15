#!/usr/bin/python
#coding: UTF-8

from .vtg_template_ import *
from .vtg_device_ import *
from ...director.reflection_deco_ import VTGThread_reflectionDeco
from .vtg_appliance_ import *

vtg_devspoke_ = []
vtg_devspoke_set = set()
vtg_devspoke_id_ = []
import pandas as pd

#
def devspoke(self):
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
    #print(devtemplateName)
    _, deviceOrgName = device.deviceOrgName_()
    _, workflowStatus = device.workflowStatus_()
    template = VTG_template(pst = devtemplateName)
    _, devSpoke = template.spoke_()
    if (deviceOrgName == self.__deviceOrg and "Deployed" == workflowStatus):
        #print("devSpoke", devSpoke)
        # 2020.12.10 when Spoke is none
        if (None == devSpoke):
            item = "( Spoke is None ) " + self.__deviceName 
        else:
            item = devSpoke
        len_previous_vtg_devspoke_set_ = len(vtg_devspoke_set)
        #
        vtg_devspoke_set.add(item)
        len_next_vtg_devspoke_set_ = len(vtg_devspoke_set)
        vtg_devspoke_id_.append(str(item))
        #
        vtg_devspoke_.append("" + self.__deviceName)
        if (len_previous_vtg_devspoke_set_ == len_next_vtg_devspoke_set_):
            print("!")
            for itembasic in sorted(vtg_devspoke_):
                if ( item in itembasic ):
                    print( "the %s exists on once more configuration: %s" % (item, itembasic))
            print(".")
        else:
            print(item, self.__deviceName)
        # 2020.9.2
        data = {'device': vtg_devspoke_, 'spoke': vtg_devspoke_id_}
        example = pd.DataFrame(data = data)
        print(example.sort_values(by = 'spoke'))


def devspokeinspectorModel(orgName):
    appliance = VTG_appliance(deviceorg = orgName)
    _, d = appliance.location_
    data = json.loads(d)
    print(json.dumps(data, indent=4))
    devicesName_ = [ tc['applianceName'] for tc in data["List"]['value'] if tc['type'] != 'controller' and tc['type'] != 'hub' ]
    # 2020.3.10 clear function
    global vtg_devspoke_
    vtg_devspoke_.clear()
    global vtg_devspoke_set
    vtg_devspoke_set.clear()
    global vtg_devspoke_id_
    vtg_devspoke_id_.clear()
    setattr(VTGThread_reflectionDeco, "run", devspoke)
    for item in devicesName_:
        delay = "0"
        thread_post = delay + ':' + item + ':' + orgName
        refdeco = VTGThread_reflectionDeco(thread_name = ("%s" % thread_post))
        refdeco.start()
    ## self.file_message(' Spokes inspect by : ' + orgName +  ' execute startup...')

#