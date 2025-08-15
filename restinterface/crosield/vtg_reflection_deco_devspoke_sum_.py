#!/usr/bin/python
#coding: UTF-8

import time, os

from .vtg_template_ import *
from .vtg_device_ import *
from .vtg_appliance_ import *

from ...director.reflection_deco_ import VTGThread_reflectionDeco

def fmttab_(data):
    df = data.sort_values(by = 'device',ascending = True)
    return df

vtg_devspokesum_ = []
vtg_devspokesum_set = set()
vtg_devspokesum_id_ = []
import pandas as pd

#
def devspokesum(self):
    # 2020.7.4 reflection_deco
    ## print("[%s]" % threading.current_thread().getName())
    thread_posted = threading.current_thread().getName()
    # print("[%s]" % thread_posted)
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
    if (deviceOrgName == self.__deviceOrg and "Deployed" == workflowStatus and None != devSpoke):
        # print(devSpoke)
        item = devSpoke
        len_previous_vtg_devspokesum_set_ = len(vtg_devspokesum_set)
        vtg_devspokesum_set.add(item)
        len_next_vtg_devspokesum_set_ = len(vtg_devspokesum_set)
        vtg_devspokesum_id_.append(str(item))
        vtg_devspokesum_.append(self.__deviceName)
        if (len_previous_vtg_devspokesum_set_ == len_next_vtg_devspokesum_set_):
            print("!")
            for itembasic in sorted(vtg_devspokesum_):
                if ( item in itembasic ):
                    print( "the %s exists on once more configuration: %s" % (item, itembasic))
            print(".")
        else:
            print(item, self.__deviceName)
        # 2020.9.2
        data = {'device': vtg_devspokesum_, 'spoke': vtg_devspokesum_id_}
        example2 = pd.DataFrame(data = data)
        example2.set_index('spoke', inplace = True)
        # print(example)
        ex22_ = example2.groupby('spoke', as_index = False).apply(fmttab_) # 2022.1.25 fmttab_
        #
        example = pd.DataFrame(data = data)
        # print(example)
        ex21_ = example.groupby('spoke').device.sum().reset_index('spoke')
        ranges_ex21_ = [ item.count("-CPE-") for item in ex21_.device ]
        ex21_['ranges'] = ranges_ex21_
        ex21_['device'] = "="
        print(ex22_)
        print(ex21_)


def devspokesuminspectorModel(orgName):
    appliance = VTG_appliance(deviceorg = orgName)
    _, d = appliance.location_
    data = json.loads(d)
    print(json.dumps(data, indent=4))
    devicesName_ = [ tc['applianceName'] for tc in data["List"]['value'] if tc['type'] != 'controller' and tc['type'] != 'hub' ]
    # 2020.3.10 clear function
    global vtg_devspoke_
    vtg_devspokesum_.clear()
    global vtg_devspokesum_set
    vtg_devspokesum_set.clear()
    global vtg_devspokesum_id_
    vtg_devspokesum_id_.clear()
    setattr(VTGThread_reflectionDeco, "run", devspokesum)
    for item in devicesName_:
        delay = "0"
        thread_post = delay + ':' + item + ':' + orgName
        refdeco = VTGThread_reflectionDeco(thread_name = ("%s" % thread_post))
        refdeco.start()
    ## self.file_message(' Spokes Summary inspect by : ' + orgName +  ' execute startup...')
