#!/usr/bin/python
#coding: UTF-8
from .vtg_device_ import *
from ...director.reflection_deco_ import VTGThread_reflectionDeco
from .vtg_appliance_ import *
vtg_device_binddata_ = []
vtg_device_binddata_lanset = set()


def lans(self):
    # 2020.7.4 reflection_deco
    thread_posted = threading.current_thread().getName()
    self.__delay = int(thread_posted.split(":")[0])
    self.__deviceName = thread_posted.split(":")[1]
    self.__deviceOrg = thread_posted.split(":")[2]
    time.sleep(self.__delay)
    dev = VTG_device(devicename = self.__deviceName)
    _, deviceOrgName = dev.deviceOrgName_()
    if (deviceOrgName == self.__deviceOrg):
        _, deviceTemplateVariableAttrs = dev.bindData_()
        for item in deviceTemplateVariableAttrs:
            # 2020.12.11
            lanitem = ""
            # 2020.3.13 HA CONCEPT
            # if ( "static" in item['name'] and "CU" not in item['name'] and "CT" not in item['name'] and "CM" not in item['name'] and "Wan" not in item['name'] and "Internet" not in item['name'] and "Mpls" not in item['name']):
            if all([ "staticaddress" in item['name'], 
                     "CU" not in item['name'].upper(),
                     "CT" not in item['name'].upper(),
                     "CM" not in item['name'].upper(),
                     "WAN" not in item['name'].upper(),
                     "INTERNET" not in item['name'].upper(),
                     "MPLS" not in item['name'].upper()
            ]):
                # print(item['value'], item['name'], self.__deviceName)
                # devicelanset.add(item['value'])
                # 2020.2.19 len_previousset comparing with len_nextset
                len_previous_vtg_device_binddata_lanset_ = len(vtg_device_binddata_lanset)
                lanitem = lanitem + item['value']
                vtg_device_binddata_lanset.add(lanitem)
                len_next_vtg_device_binddata_lanset_ = len(vtg_device_binddata_lanset)
                # 2020.2.20 vtg_device_binddata_.append(item['value'] + "_" + item['name'] + self.__deviceName)
                vtg_device_binddata_.append((lanitem, item['name'], self.__deviceName))
                if (len_previous_vtg_device_binddata_lanset_ == len_next_vtg_device_binddata_lanset_):
                    print(" !")
                    for itembinddata in sorted(vtg_device_binddata_, key = lambda lan: lan[0]):
                        if ( lanitem in itembinddata ):
                            print( "the %s exists on once more configuration: %s" % (lanitem, itembinddata[1] + itembinddata[2] ))
                    print(" .")
                else:
                    if ("" == lanitem):
                        print("Lan is DHCP", self.__deviceName)
                    else:
                        print(f'{lanitem:>24} @ {self.__deviceName:<40}')
                        # print(lanitem, item['name'], self.__deviceName)


def lanorginspectorModel(orgName):
    _, d = VTG_appliance(deviceorg = orgName).location_
    # print(json.dumps(json.loads(d), indent = 4))
    try:
        devicesName_ = [ tc['applianceName'] for tc in json.loads(d)["List"]['value'] if tc['type'] != 'controller' ]
    except Exception as e:
        # print(e)
        print(" Select the tenant priorly, please. ")
    else:
        # 2020.3.10 clear function
        global vtg_device_binddata_ 
        vtg_device_binddata_.clear()
        global vtg_device_binddata_lanset
        vtg_device_binddata_lanset.clear()
        # 2020.7.4 reflection_deco #thread_list = [ VTGThread_reflectionDeco(thread_name = ("%s" % "0" + ':' + item + ':' + orgName)) for item in devicesName_ ]
        setattr(VTGThread_reflectionDeco, "run", lans)
        for item in devicesName_:
            delay = "0"
            thread_post = delay + ':' + item + ':' + orgName
            refdeco = VTGThread_reflectionDeco(thread_name = ("%s" % thread_post))
            refdeco.start()