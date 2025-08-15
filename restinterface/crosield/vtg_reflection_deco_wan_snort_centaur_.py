#!/usr/bin/python
#coding: UTF-8

from .vtg_interface_ import *
from ...director.reflection_deco_ import VTGThread_reflectionDeco

vtg_wan_snort_intf_ = []
vtg_wan_snort_intfset = set()
vtg_wan_snort_intf_id_ = []
import pandas as pd

#
def wan_snort(self):
    thread_posted = threading.current_thread().getName()
    self.__delay = int(thread_posted.split(":")[0])
    self.__deviceName = thread_posted.split(":")[1]
    self.__deviceOrg = thread_posted.split(":")[2]
    time.sleep(self.__delay)
    ##print("[%s]" % threading.current_thread().getName())
    dev = VTG_device(devicename = self.__deviceName)
    _, deviceOrgName = dev.deviceOrgName_()
    if (deviceOrgName == self.__deviceOrg):
        # 2020.4.9 devicesName -> org_ping
        intf = VTG_interfaces(devicename = self.__deviceName, deviceorg = self.__deviceOrg)
        hostName = intf.default_wan_table_()
        rc, d = intf.unit_()
        if (200 == rc):
            data = json.loads(d)
            text_intf_ = ""
            for butt in data['org_intf']:
              if ("wan" == butt['type'] and "MPLS" not in butt['vrf'].upper()):
                #print(butt)
                if "up" == butt['if-oper-status']:
                    _, d = dev.pings_wan_(hostname = hostName, routingInstance = butt['vrf'])
                    if "success" != d:
                        # 2020.6.1
                        text = ' ! ' + butt['vrf'] + ' ' + ': ' + butt['name'] + ' ' + self.__deviceName + '\n'
                        text_intf_ = text_intf_ + text
                        text_intf_brief_ = butt['vrf'] + ' ' + butt['service-provider']
                        vtg_wan_snort_intf_id_.append(self.__deviceName)
                        vtg_wan_snort_intf_.append(text_intf_brief_)
                else:
                    # 2020.10.14
                    text = ' ! ' + butt['vrf'] + ' ' + ': ' + butt['name'] + ' ' + self.__deviceName + '\n'
                    text_intf_ = text_intf_ + text
                    # 2021.1.15
                    intf.keydefval_(butt, 'if-proto-down', "['INFO']")
                    text_intf_brief_ = butt['vrf'] + ' ' + str(butt['if-proto-down'])
                    vtg_wan_snort_intf_id_.append(self.__deviceName)
                    vtg_wan_snort_intf_.append(text_intf_brief_)
            #print(self.__deviceName + self.__deviceOrg + text_intf_)
            print(text_intf_, self.__deviceName, self.__deviceOrg)
            print()
        else:
            print(" No Any Wan Online Info: " + self.__deviceName + ' ' + self.__deviceOrg)
            vtg_wan_snort_intf_id_.append(self.__deviceName)
            vtg_wan_snort_intf_.append("!")
        # 2020.6.25
        data = {'uplinkInMire': vtg_wan_snort_intf_, 'id': vtg_wan_snort_intf_id_}
        example = pd.DataFrame(data = data)
        # 2020.11.23
        example.set_index('id', inplace=True)
        #print(example)
        ex1 = example.groupby('id').uplinkInMire.sum().reset_index()
        size_ex1 = [ item.count(" ") for item in ex1.uplinkInMire ]
        ex1['size'] = size_ex1
        print(ex1)






