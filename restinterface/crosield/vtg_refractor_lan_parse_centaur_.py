#!/usr/bin/python
#coding: UTF-8
from .vtg_attemptable_ import *
from ...director.refractor_ import VTGThread_refractor, maximize, thread_chain
import pandas as pd
from .vtg_appliance_ import *
from tqdm import tqdm
from functools import lru_cache
from ...director.fusable_ import Wansnort


def lanparseModel(orgName):
    # 2021.1.20 _refractor
    setattr(VTGThread_refractor, "run", lan_parse)
    _, d = VTG_appliance(deviceorg = orgName).location_
    # print(json.dumps(json.loads(data), indent = 4))
    devicesName_ = [ tc['applianceName'] for tc in json.loads(d).get('List').get('value') if  'controller' != tc['type'] and 'hub' != tc['type'] ]
    # 2023.2.28 appendless
    setattr(VTGThread_refractor, "vtg_lan_parse_if_", { ''.join([ devitem, ' ', item['value'] ]) : "is routing-singleton on reachable" 
        for devitem in devicesName_ for item in VTG_device(devicename = devitem).bindData 
        if all([ "staticaddress" in item['name'], 
                 "CPN" not in item['name'].upper(), 
                 "CU" not in item['name'].upper(), 
                 "CT" not in item['name'].upper(), 
                 "CM" not in item['name'].upper(), 
                 "WAN" not in item['name'].upper(), 
                 "INTERNET" not in item['name'].upper(), 
                 "MPLS" not in item['name'].upper() ]) })
    thread_table = [ maximize(item, orgName) for item in devicesName_ ]

    # 2023.3.12 thread_chain
    for ty in thread_chain(thread_table):
        ty.start()
    proc_bar = tqdm(thread_table)
    for p in thread_chain(proc_bar):
        proc_bar.set_postfix({"Parse Lan": '{}'.format(p)})
        p.join()

    # print(VTGThread_refractor.vtg_lan_parse_if_)
    dfprint({ 'ParseLan': [ value for value in VTGThread_refractor.vtg_lan_parse_if_.values() ], 'IntfId': [ key for key in VTGThread_refractor.vtg_lan_parse_if_.keys() ] })


def fmttab_(data):
    df = data.sort_values(by = 'ParseLan', ascending = True)
    return df[~df.ParseLan.isin([
        Wansnort['NPA'].value.center(30, ' '),
        Wansnort['LTEM'].value.center(30, '-'), ] 
    )]


def dfprint(data):
    example = pd.DataFrame(data = data)
    example.set_index('IntfId', inplace = True)
    ex_centaur_ = example.groupby('IntfId',as_index = False).apply(fmttab_)
    print('\r{}'.format(ex_centaur_), end = '')
    print()


@lru_cache(maxsize = 3)
def lan_parse(self):
    setattr(VTG_interface, "default_lan_tables_", default_lan_tables_)
    self.__delay = threading.current_thread().delay
    self.__deviceName = threading.current_thread().deviceName
    self.__deviceOrg = threading.current_thread().deviceOrg
    time.sleep(int(self.__delay))
    with VTG_interface(devicename = self.__deviceName, deviceorg = self.__deviceOrg) as (uio, intf):
        if ("..U.." != uio):
            for butt in intf.orgintfinside_(uio):
                if "up" == butt['if-oper-status']:
                    # (" @ pageJson_pings_wans: ", pageJson_pings_lans, self.__deviceName, butt['vrf'])
                    hostName = intf.default_lan_tables_
                    for i in range(len(hostName)):
                        if "success" != VTG_device(devicename = self.__deviceName).pingw_(hostname = hostName[i], routingInstance = butt['vrf'], count = 1):
                            # print(butt, intf, hostName[i])
                            # print("]RSR[", self.__deviceName, butt['vrf'], hostName[i])
                            self.vtg_lan_parse_if_.update({ ''.join([ self.__deviceName, ' ', butt.get('address')[0].get('ip') ]) : ''.join([ butt['name'].upper(), ' ', Lansnort['RSR'].value[0] ]).center(30, '~') })
                        else:
                            try:
                                self.vtg_lan_parse_if_.pop(''.join([ self.__deviceName, ' ', butt.get('address')[0].get('ip') ]))
                            except Exception as err:
                                print("{k} : to skip the redundance")
                else:
                    self.vtg_lan_parse_if_.update({ ''.join([ self.__deviceName, ' ', butt.get('address')[0].get('ip') ]) : ''.join([ butt['name'].upper(), ' ', Lansnort['LMB'].value[0] ]).center(30, '-') })