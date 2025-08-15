#!/usr/bin/python
#coding: UTF-8
# from .vtg_attemptable_ import *
from ...director.refractor_ import VTGThread_refractor, maximize, thread_chain
import pandas as pd
from .vtg_appliance_ import *
from tqdm import tqdm
from functools import lru_cache, reduce
# import memory_profiler as mem
from collections import namedtuple
from pprint import pprint
import asyncio
import yaml
import json
from .vtg_interface_ import VTG_interface
from ...director.fusable_ import Wansnort, Lansnort


async def shebang(self, item, butt, count):
    l_value = list(dict(yaml.load(yaml.dump(item), Loader = yaml.BaseLoader)).values())
    if ( 2 == len(l_value) ):
        lan_pageJson_pings_ = []
        if butt['name'] == l_value[1]:
            # print(" - Interport: [" + l_value[1] + "]")
            # print(" - Count of camouflage: ", len(l_value[0]), self.__deviceName)
            if 1 < len(l_value[0]):
                for item in l_value[0]:
                    pageJson_pings_, res = await VTG_device(devicename = self.__deviceName).aoipingstre_(hostname = item['ip'], routingInstance = item["routing-instance"], count = count)
                    if "success" == pageJson_pings_:
                        lan_pageJson_pings_.append(item['ip'])
                        if len(lan_pageJson_pings_) >= 2:
                            break
                    # print('- lan_res : {}@{}={}'.format( item["routing-instance"], item["ip"], pageJson_pings_ ))
            try:
                assert 1 < len(lan_pageJson_pings_)
            except:
                print(" ! No more than one entry over the local area network ! ")
                self.vtg_lan_camouflage_intf_id_.append(self.__deviceName)
                self.vtg_lan_camouflage_intf_.append(reduce(lambda s, t: s + t, [ butt['name'].upper().split('/')[1], ' ', Lansnort['DC'].value[0], ' ', butt['vrf'] ]).center(30, '~'))


async def alan2do(self, intf, butt):
    start = time.perf_counter()
    ## await asyncio.sleep(4.25)
    _, d = intf.entry_
    data_yaml = yaml.dump(json.loads(d))
    dict_yaml_ = yaml.load(data_yaml, Loader = yaml.BaseLoader)
    coros = [ self.shebang(item, butt, count = 2) for item in dict_yaml_["collection"]["arp:interface"] ]
    results = await asyncio.gather(*coros, return_exceptions = True)
    end = time.perf_counter()
    print(f"{self.__deviceName}.{butt['name']} spent {end - start:.2f}s")


def alanreliableModel(orgName):
    # print("pre_mem", mem.memory_usage())
    # 2022.12.13 globalless
    setattr(VTGThread_refractor, "vtg_lan_camouflage_intf_", [])
    setattr(VTGThread_refractor, "vtg_lan_camouflage_intf_id_", [])
    # 2021.1.20 _refractor
    setattr(VTGThread_refractor, "run", lan_reliable)
    _, d = VTG_appliance(deviceorg = orgName).location_
    # print(json.dumps(json.loads(data), indent = 4))
    devicesName_ = [ tc['applianceName'] for tc in json.loads(d).get('List').get('value') if all([ 'controller' != tc['type'], 'hub' != tc['type'] ]) ]
    thread_table = [ maximize(item, orgName) for item in devicesName_ * 1 ]
    # 2023.3.12 thread_chain
    [ ty.start() for ty in thread_chain(thread_table) ]
    proc_bar = tqdm(thread_table)
    for p in thread_chain(proc_bar):
        proc_bar.set_postfix({"Acentaur Reliable Lan": '{}'.format(p)}); p.join()
    dfprint({'CamouflageLan': VTGThread_refractor.vtg_lan_camouflage_intf_, 'IntfId': VTGThread_refractor.vtg_lan_camouflage_intf_id_})
    # print("post_mem", mem.memory_usage())


def fmttab_(data):
    df = data.sort_values(by = 'CamouflageLan', ascending = True)
    return df[ df.CamouflageLan.isin([ clan for clan in df.CamouflageLan if all([ "YF-ChongQing-LAN-VR-WAN" not in clan ]) ]) ]


def dfprint(data):
    example = pd.DataFrame(data = data)
    example.set_index('IntfId', inplace = True)
    ex_centaur_ = example.groupby('IntfId', as_index = False).apply(fmttab_)
    print('\r{}'.format(ex_centaur_), end = '')
    print()


@lru_cache(maxsize = 8)
def lan_reliable(self):
    setattr(VTGThread_refractor, "alan2do", alan2do)
    setattr(VTGThread_refractor, "shebang", shebang)
    self.__delay = threading.current_thread().delay
    self.__deviceName = threading.current_thread().deviceName
    self.__deviceOrg = threading.current_thread().deviceOrg
    time.sleep(int(self.__delay))
    with VTG_interface(devicename = self.__deviceName, deviceorg = self.__deviceOrg) as (uio, intf):
        # if "..U.." == uio:
        if (Wansnort['CRITICAL'].value[0] == uio):
            print(f'- ! Off-Line: {self.__deviceName} {self.__deviceOrg}')
            self.vtg_lan_camouflage_intf_id_.append(self.__deviceName)
            self.vtg_lan_camouflage_intf_.append(Wansnort['CRITICAL'].value[0].center(30, '.'))
        else:
            for butt in intf.orgintfinside_(uio):
                if "up" == butt['if-oper-status']:
                    apingstreloop = asyncio.new_event_loop()
                    asyncio.set_event_loop(apingstreloop)
                    # asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
                    apingstreloop.run_until_complete(self.alan2do(intf, butt))
                else:
                    self.vtg_lan_camouflage_intf_id_.append(self.__deviceName)
                    self.vtg_lan_camouflage_intf_.append(reduce(lambda s, t: s + t, [ butt['name'].upper().split('/')[1], ' ', Lansnort['LMB'].value[0] ]).center(30, ' '))