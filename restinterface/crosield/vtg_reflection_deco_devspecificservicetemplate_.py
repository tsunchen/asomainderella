#!/usr/bin/python
#coding: UTF-8
from .vtg_device_ import *
from ...director.reflection_deco_ import VTGThread_reflectionDeco
from .vtg_appliance_ import *

vtg_device_basic_ = []
vtg_device_basic_ssset = set()


def devspecificservicetemplate(self):
    # 2020.7.4 reflection_deco
    ## print("[%s]" % threading.current_thread().getName())
    thread_posted = threading.current_thread().getName()
    # print("[%s]" % thread_posted)
    self.__delay = int(thread_posted.split(":")[0])
    self.__deviceName = thread_posted.split(":")[1]
    self.__deviceOrg = thread_posted.split(":")[2]
    time.sleep(self.__delay)
    dev = VTG_device(devicename = self.__deviceName)
    _, deviceOrgName = dev.deviceOrgName_()
    if deviceOrgName == self.__deviceOrg:
        #_, item = dev.serialNumber_()
        _, item = dev.specificServiceTemplate_()
        _, items = dev.bindData_()
        len_previous_vtg_device_basic_ssset_ = len(vtg_device_basic_ssset)
        vtg_device_basic_ssset.add(item)
        len_next_vtg_device_basic_ssset_ = len(vtg_device_basic_ssset)
        vtg_device_basic_.append(str(item) + "_" + self.__deviceName)
        if (len_previous_vtg_device_basic_ssset_ == len_next_vtg_device_basic_ssset_):
            print("!")
            for itembasic in sorted(vtg_device_basic_):
                if ( item in itembasic ):
                    print( "the %s exists on once more configuration: %s" % (item, itembasic))
            print(".")
        else:
            print(item)


def devsstinspectorModel(orgName):
    # 2020.7.4 reflection_deco
    setattr(VTGThread_reflectionDeco, "run", devspecificservicetemplate)
    appliance = VTG_appliance(deviceorg = orgName)
    _, d = appliance.location_
    data = json.loads(d)
    print(json.dumps(data, indent = 4))
    devicesName_ = [ tc['applianceName'] for tc in data["List"]['value'] if tc['type'] != 'controller' ]
    global vtg_device_basic_
    vtg_device_basic_.clear()
    global vtg_device_basic_snset
    vtg_device_basic_ssset.clear()
    for item in devicesName_:
        delay = "0"
        thread_post = delay + ':' + item + ':' + orgName
        refdeco = VTGThread_reflectionDeco(thread_name = ("%s" % thread_post))
        refdeco.start()
    ## self.file_message(' Serial Number inspect by : ' + orgName +  ' execute startup...')