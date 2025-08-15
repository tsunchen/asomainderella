#!/usr/bin/python
#coding: UTF-8
from .vtg_attemptable_ import *
from ...director.refractor_ import VTGThread_refractor, maximize, thread_chain
import pandas as pd
from .vtg_appliance_ import *
from tqdm import tqdm
from functools import lru_cache, reduce
# import memory_profiler as mem
from collections import namedtuple
from pprint import pprint
from ...director.fusable_ import Wansnort, Lansnort
from .vtg_volumector_ import LAN


def laninspectorModel(orgName):
    # print("pre_mem", mem.memory_usage())
    # 2024.7.30 annex
    setattr(VTGThread_refractor, "annex", annex)
    # 2022.12.13 global parameter less
    setattr(VTGThread_refractor, "vtg_lan_snort_intf_", [])
    setattr(VTGThread_refractor, "vtg_lan_snort_intf_id_", [])
    # 2021.1.20 _refractor
    setattr(VTGThread_refractor, "run", lan_snort)

    _, d = VTG_appliance(deviceorg = orgName).location_

    devicesName_ = [ tc['applianceName'] for tc in json.loads(d).get('List').get('value') if all([ 'controller' != tc['type'], 'hub' != tc['type'] ]) ]

    thread_table = [ maximize(item, orgName) for item in devicesName_ * 1 ]

    # 2023.3.12 thread_chain
    [ ty.start() for ty in thread_chain(thread_table) ]
    proc_bar = tqdm(thread_table)
    for p in thread_chain(proc_bar):
        proc_bar.set_postfix({"Snort Lan": '{}'.format(p)}); p.join()

    dfprint({'SnortLan': VTGThread_refractor.vtg_lan_snort_intf_, 'IntfId': VTGThread_refractor.vtg_lan_snort_intf_id_})
    # print("post_mem", mem.memory_usage())


def fmttab_(data):
    df = data.sort_values(by = 'SnortLan', ascending = True)
    return df[ df.SnortLan.isin([ slan for slan in df.SnortLan if all([ "YF-ChongQing-LAN-VR-WAN" not in slan ]) ]) ]


def dfprint(data):
    example = pd.DataFrame(data = data)
    example.set_index('IntfId', inplace = True)
    ex_centaur_ = example.groupby('IntfId',as_index = False).apply(fmttab_)
    print('\r{}'.format(ex_centaur_), end = '')
    print()


@lru_cache(maxsize = 8)
def lan_snort(self):
    setattr(VTG_interface, "default_lan_tables_", default_lan_tables_)
    self.__delay = threading.current_thread().delay
    self.__deviceName = threading.current_thread().deviceName
    self.__deviceOrg = threading.current_thread().deviceOrg
    time.sleep(int(self.__delay))
    with VTG_interface(devicename = self.__deviceName, deviceorg = self.__deviceOrg) as (uio, intf):
        if (Wansnort['CRITICAL'].value[0] == uio):
            print(f'- ! Off-Line: {self.__deviceName} {self.__deviceOrg}')
            self.annex(id = self.__deviceName, val = Wansnort['CRITICAL'].value[0].center(30, '.'))
        else:
            for butt in intf.orgintfinside_(uio):
                if "up" == butt['if-oper-status']:
                    ## 2024.7.9 Volume Vector on LAN
                    hostName = LAN(volume = "Volume-Vector").default_vector(intf.orgName)

                    for i in range(len(hostName)):
                        sta, res = VTG_device(devicename = self.__deviceName).pingstre_(hostname = hostName[i], routingInstance = butt['vrf'], count = 1)
                        if "success" != sta:
                            self.annex(id = self.__deviceName, val = reduce(
                                lambda s, t: s + t, 
                                [ butt['name'].upper().split('/')[1], ' ', Lansnort['RSR'].value[0], ' ', hostName[i], ' ', butt['vrf'] ]
                                ).center(30, '~'))
                        else:
                            # 2024.8.22 found nil on the pong of ping
                            try:
                                packloss = res.split("\n")[-4:][2].split()[5]
                            except IndexError:
                                # print("- on the Error of Index - (", res, ")", self.__deviceName)
                                self.annex(id = self.__deviceName, val = reduce(
                                    lambda s, t: s + t, 
                                    [ butt['name'].upper().split('/')[1], ' ', "PongNil", ' ', hostName[i], ' ', butt['vrf'] ]
                                    ).center(30, ' '))
                            else:
                                if "0%" != packloss:
                                    self.annex(id = self.__deviceName, val = reduce(
                                        lambda s, t: s + t, 
                                        [ butt['name'].upper().split('/')[1], " R.Pack.Loss. ", packloss, ' ', hostName[i], ' ', butt['vrf'] ]
                                        ).center(30, ' '))
                else:
                    self.annex(id = self.__deviceName, val = reduce(
                        lambda s, t: s + t, 
                        [ butt['name'].upper().split('/')[1], ' ', Lansnort['LMB'].value[0] ]
                        ).center(30, ' '))


def annex(self, id, val):
    self.vtg_lan_snort_intf_id_.append(id)
    self.vtg_lan_snort_intf_.append(val)