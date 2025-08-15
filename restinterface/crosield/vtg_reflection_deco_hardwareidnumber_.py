#!/usr/bin/python
#coding: UTF-8
from .vtg_device_ import *
from ...director.reflection_deco_ import VTGThread_reflectionDeco
from .vtg_appliance_ import *

vtg_device_basic_ = []
vtg_device_basic_hinset = set()


def hardwareidnumber(self):
    # 2020.7.4 reflection_deco
    ## print("[%s]" % threading.current_thread().getName())
    thread_posted = threading.current_thread().getName()
    # print("[%s]" % thread_posted)
    self.__delay = int(thread_posted.split(":")[0])
    self.__deviceName = thread_posted.split(":")[1]
    self.__deviceOrg = thread_posted.split(":")[2]
    self.__deviceUUID = thread_posted.split(":")[3]
    time.sleep(self.__delay)
    # print(self.__deviceName, self.__deviceUUID)
    try:
        _, d = VTG_appliance(deviceorg = self.__deviceOrg).hardware_(self.__deviceUUID)
        data = json.loads(d)
        # print(self.__deviceName, data['versanms.Hardware']['hardWareSerialNo'])
        item = data['versanms.Hardware']['hardWareSerialNo']
    except KeyError as e:
        print(self.__deviceName, '( No Hardware ID Number Found )') # print(self.__deviceName, 'No {} Found'.format(e))
    else:
        len_previous_vtg_device_basic_hinset_ = len(vtg_device_basic_hinset)
        vtg_device_basic_hinset.add(item)
        len_next_vtg_device_basic_hinset_ = len(vtg_device_basic_hinset)
        vtg_device_basic_.append(self.__deviceName  + "_" + str(item))
        if (len_previous_vtg_device_basic_hinset_ == len_next_vtg_device_basic_hinset_):
            print("!")
            for itembasic in sorted(vtg_device_basic_):
                if ( item in itembasic ):
                    print( "the %s exists on once more configuration: %s" % (item, itembasic))
            print(".")
        else:
            print(self.__deviceName, item)


def hinorginspectorModel(orgName):
    setattr(VTGThread_reflectionDeco, "run", hardwareidnumber)
    appliance = VTG_appliance(deviceorg = orgName)
    _, d = appliance.location_
    data = json.loads(d)
    # print(json.dumps(data, indent = 4))
    appliancetc = [ tc for tc in data["List"]['value'] if tc['type'] != 'controller' ]
    global vtg_device_basic_
    vtg_device_basic_.clear()
    global vtg_device_basic_hinset
    vtg_device_basic_hinset.clear()
    # 2020.7.4 reflection_deco
    for item in appliancetc:
        delay = "0"
        thread_post = delay + ':' + item['applianceName'] + ':' + orgName + ':' + item['applianceUuid']
        refdeco = VTGThread_reflectionDeco(thread_name = ("%s" % thread_post))
        refdeco.start()
    ## self.file_message(' Hardware ID Number inspected by : ' + orgName +  ' execute startup...')