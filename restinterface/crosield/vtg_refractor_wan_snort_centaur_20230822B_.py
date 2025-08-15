#!/usr/bin/python
#coding: UTF-8
from ...director.refractor_ import VTGThread_refractor, maximize
import pandas as pd
import threading
from .vtg_appliance_ import VTG_appliance
from tqdm import tqdm
from threading import Lock
from .vtg_attemptable_ import *
from .vcia.vcia_to_ping_ import *


def waninspectorModel(orgName):
    # 2022.12.13 globalless
    setattr(VTGThread_refractor, "vtg_wan_snort_intf_", [])
    setattr(VTGThread_refractor, "vtg_wan_snort_intf_id_", [])
    # 2021.1.20 _refractor
    setattr(VTGThread_refractor, "run", wan_snort)
    # overlte(self, butt, intf)
    setattr(VTGThread_refractor, "overlte", overlte)
    # alert(self, butt, inft)
    setattr(VTGThread_refractor, "alert", alert)
    # park(self, butt, inft)
    setattr(VTGThread_refractor, "park", park)
    # failover
    setattr(VTGThread_refractor, "failover", failover)
    _, d = VTG_appliance(deviceorg = orgName).location_
    data = json.loads(d)
    print(json.dumps(data, indent = 4))
    # hub internet, cpe internet
    try:
        devicesName_ = [ tc['applianceName'] for tc in data["List"]['value'] if  'controller' != tc['type'] and 'hub' != tc['type'] ]
    except Exception as e:
        # print(e)
        print(" Select the tenant priorly, please. ")
    else:
        thread_table = [ maximize(item, orgName) for item in devicesName_ ]
        for thread in thread_table:
            thread.start()
        proc_bar = tqdm(thread_table)
        for p in proc_bar:
            # proc_bar.set_description('No.{}'.format(p))
            proc_bar.set_postfix({"Envirolink": '{}'.format(p)})
            p.join()
        dfprint({'Envirolink': VTGThread_refractor.vtg_wan_snort_intf_, 'IntfId': VTGThread_refractor.vtg_wan_snort_intf_id_})


def fmttab_(data):
    df = data.sort_values(by = 'Envirolink', ascending = True)
    return df[~df.Envirolink.isin([
        ## "N.P.A".center(30, ' '),
        "LTE-Transport-VR ['MONITOR']".center(30, '-'), ] 
    )]


def dfprint(data):
    example = pd.DataFrame(data = data)
    # 2020.11.23
    example.set_index('IntfId', inplace = True)
    ex_centaur_ = example.groupby('IntfId', as_index = False).apply(fmttab_)
    # ex_centaur_ = example.groupby('IntfId', group_keys = False).apply(fmttab_) # 2022.1.25 fmttab_
    print('\r{}'.format(ex_centaur_), end = '') # 2022.5.10 print\r
    print()


def wan_snort(self):
    setattr(VTG_interface, "default_wan_table_", default_wantable_)
    self.__delay = threading.current_thread().delay
    self.__deviceName = threading.current_thread().deviceName
    self.__deviceOrg = threading.current_thread().deviceOrg
    time.sleep(int(self.__delay))
    with VTG_interface(devicename = self.__deviceName, deviceorg = self.__deviceOrg) as (uio, intf):
        if ("..U.." == uio):
            print(f'- ! Off Line: {self.__deviceName} {self.__deviceOrg}')
            self.vtg_wan_snort_intf_id_.append(self.__deviceName)
            self.vtg_wan_snort_intf_.append(Wansnort['CRITICAL'].value[0].center(30, '.'))
        else:
            for butt in intf.orgintfnocloudnet_(uio):
                if "up" == butt['if-oper-status']:
                    # (" @ pageJson_pings_wans: ", pageJson_pings_wans, self.__deviceName, butt['vrf'])
                    hostName = intf.default_wan_table_
                    for i in range(len(hostName)):
                        # print(butt['vrf'])
                        # 2023.5.28 VCIA chelator
                        vec = [ 
                            pure_out(end = ""),
                            # 2023.5.29 tag on chelator
                            lambda _: side_in(( 'ping', Wan(deviceName = self.__deviceName, hostname = hostName[i], routingInstance = butt['vrf'], count = 1) )),
                            lambda vectorIntf: pure_out(vectorIntf),
                        ]
                        # chelatores = reduce(lambda u, v: bind(u, v), vec).unpack()
                        # print("VCIA CHELATOR: ", chelatores)
                        #
                        # 2023.5.26 achelated-vector-ping
                        if "success" != reduce(lambda u, v: bind(u, v), vec).unpack():
                            self.failover(butt, intf, hostName[i])
                            print(".F.", self.__deviceName, butt['vrf'], hostName[i])
                else:
                    self.alert(butt, intf, Wansnort['ALERT'].value[0])


def failover(self, butt, intf, hostname):
    """ ('pageJson_pings_wans handler...') """
    setattr(VTG_interface, "intfoperup_", intfoperup_)
    maxnum_tback_ = 0
    try:
        for i in Attemptable_(nStart = maxnum_tback_, butt = butt, deviceName = self.__deviceName, hostName = hostname, ok = "success", intf = intf):
            print('- Attempted: {}'.format(maxnum_tback_ - i))
    except Exception as err:
        print("err: ", err)
    else:
        # ("handler.park")
        self.park(butt, intf, Wansnort['PARK'].value[0])
    finally:
        # ("handler.overlte")
        self.overlte(butt, intf, Wansnort['OVERLTE'].value[0])


def park(self, butt, intf, tag):
    # PARK, Suspended Pause Parking [NHP]
    text_intf_brief_ = ''.join([ butt['vrf'], ' ', tag ])
    self.vtg_wan_snort_intf_id_.append(self.__deviceName)
    self.vtg_wan_snort_intf_.append(text_intf_brief_.center(30, '.'))


def alert(self, butt, intf, tag):
    # 2021.1.15 # intf.keydefval_(butt, 'if-proto-down', "['INFO']")
    # 2022.1.14 interface unit to insert
    intf.keydefval_(butt, 'if-proto-down', Wansnort['INFO'].value[0])
    intf.keydefval_(butt, 'network', Wansnort['ETHER'].value[0])
    # 2021.4.13 unknown network
    if (butt['network']).upper() in ["WAN2", "LTE"]:
        text_intf_brief_ = ''.join([ butt['vrf'], ' ', str(butt['if-proto-down']) ])
    else:
        # ALERT, INFO, MONITOR
        text_intf_brief_ = ''.join([ butt['vrf'], ' ', tag ]) if "MONITOR" not in butt['if-proto-down'] else ''.join([ butt['vrf'], ' ', str(butt['if-proto-down']) ])
    self.vtg_wan_snort_intf_id_.append(self.__deviceName)
    self.vtg_wan_snort_intf_.append(text_intf_brief_.center(30, '-'))


def overlte(self, butt, intf, tag):
    if "tvi-0/3001.0" == butt['name']:
        intf.keydefval_(butt, 'network', Wansnort['ETHER'].value[0])
    if "LTE" == butt['network'].upper(): # Over the LTE
        if int(butt['current-rx-bps']) > 4096 or int(butt['current-tx-bps']) > 1024:
            text_intf_brief_ = ''.join([ butt['vrf'], ' ', tag ])
            self.vtg_wan_snort_intf_id_.append(self.__deviceName)
            self.vtg_wan_snort_intf_.append(text_intf_brief_.center(30, '.'))