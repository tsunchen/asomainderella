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
headers16 = [ 'name', 'hostInf', 'mac', 'ifOperStatus', 'ifAdminStatus', 'vrf', 'network', 'description', 'type', 'configuredRXbps', 'currentRXbps', 'measuredDownlinkBps', 'configuredTXbps', 'currentTXbps', 'measuredUplinkBps', 'address' ]
headers15 = [ 'name', 'hostInf', 'mac', 'ifOperStatus', 'ifAdminStatus', 'vrf', 'network', 'type', 'configuredRXbps', 'currentRXbps', 'measuredDownlinkBps', 'configuredTXbps', 'currentTXbps', 'measuredUplinkBps', 'address' ]
from pprint import pprint
import asyncio
# from .vtg_vector_ import Group, Wan, default_wantable_, Wansnort


def aiolaninspectorModel(orgName):
    # print("pre_mem", mem.memory_usage())
    # 2022.12.13 globalless
    setattr(VTGThread_refractor, "vtg_lan_snort_intf_", [])
    setattr(VTGThread_refractor, "vtg_lan_snort_intf_id_", [])
    # 2021.1.20 _refractor
    setattr(VTGThread_refractor, "run", aiolan_snort)
    _, d = VTG_appliance(deviceorg = orgName).location_
    # print(json.dumps(json.loads(data), indent = 4))
    devicesName_ = [ tc['applianceName'] for tc in json.loads(d).get('List').get('value') if all([ 'controller' != tc['type'], 'hub' != tc['type'] ]) ]

    thread_table = [ maximize(item, orgName) for item in devicesName_ * 1 ]

    # 2023.3.12 thread_chain
    [ ty.start() for ty in thread_chain(thread_table) ]
    proc_bar = tqdm(thread_table)
    for p in thread_chain(proc_bar):
        proc_bar.set_postfix({"Centauraio Snort Lan": '{}'.format(p)}); p.join()

    dfprint({'SnortLan': VTGThread_refractor.vtg_lan_snort_intf_, 'IntfId': VTGThread_refractor.vtg_lan_snort_intf_id_})
    # print("post_mem", mem.memory_usage())


def fmttab_(data):
    df = data.sort_values(by = 'SnortLan', ascending = True)
    return df[ df.SnortLan.isin([ slan for slan in df.SnortLan if all([ "YF-ChongQing-LAN-VR-WAN" not in slan ]) ]) ]
    # df.SnortLan.isin([ slan for slan in df.SnortLan if all([ "YF-ChongQing-LAN-VR-WAN" not in slan ]) ])
    # slan for slan in df.SnortLan if all([ "YF-ChongQing-LAN-VR-WAN" not in slan ])
    '''
    _Slan = []
    for slan in df.SnortLan:
        slan_bool_ = [ "YF-ChongQing-LAN-VR-WAN" not in slan ]
        if all(slan_bool_):
            _Slan.append(slan)
    return df[df.SnortLan.isin(_Slan)]
    '''


def dfprint(data):
    example = pd.DataFrame(data = data)
    example.set_index('IntfId', inplace = True)
    ex_centaur_ = example.groupby('IntfId',as_index = False).apply(fmttab_)
    print('\r{}'.format(ex_centaur_), end = '')
    print()


async def shebang(self, hostNamei, butt, count):
    """ count = 1 """
    devshebang = VTG_device(devicename = self.__deviceName)
    state, _ = await devshebang.aoipingstre_(hostname = hostNamei, routingInstance = butt.vrf, count = count)
    if "success" != state:
        print(devshebang, state)
        # print(f"- {devshebang} {state} {hostNamei} playing through on 2nd round")
        # state_2ndr, _ = await devshebang.aoipingstre_(hostname = hostNamei, routingInstance = butt.vrf, count = count)
        # if "success" != state_2ndr:
        self.vtg_lan_snort_intf_id_.append(self.__deviceName)
        self.vtg_lan_snort_intf_.append(reduce(lambda s, t: s + t, [ butt.name.upper().split('/')[1], ' ', Lansnort['RSR'].value[0], ' ', hostNamei, ' ', butt.vrf ]).center(30, '~'))


async def main_todo(self, intf, butt):
    start = time.perf_counter()
    hostName = intf.default_lan_tables_
    ## await asyncio.sleep(4.25)

    coros = [ self.shebang(hostName[i], butt, count = 4) for i in range(len(hostName)) ]

    results = await asyncio.gather(*coros, return_exceptions = True)

    #for r in results:
    #    pprint(r)

    end = time.perf_counter()
    print(f"{butt.name} took: {end - start:.2f}s")


@lru_cache(maxsize = 8)
def aiolan_snort(self):
    setattr(VTGThread_refractor, "main_todo", main_todo)
    setattr(VTGThread_refractor, "shebang", shebang)
    setattr(VTG_interface, "default_lan_tables_", default_lan_tables_)
    self.__delay = threading.current_thread().delay
    self.__deviceName = threading.current_thread().deviceName
    self.__deviceOrg = threading.current_thread().deviceOrg
    time.sleep(int(self.__delay))
    with VTG_interface(devicename = self.__deviceName, deviceorg = self.__deviceOrg) as (uio, intf):
        if "..U.." == uio:
            print(f'- ! Off-Line: {self.__deviceName} {self.__deviceOrg}')
            self.vtg_lan_snort_intf_id_.append(self.__deviceName)
            self.vtg_lan_snort_intf_.append(Wansnort['CRITICAL'].value[0].center(30, '.'))
        else:
            Vehiclerface15 = namedtuple('Vehiclerface15', headers15)
            vehintf15 = [ Vehiclerface15(*oiinv.values()) for oiinv in iter(intf.orgintfinside_(uio)) if 15 == len(oiinv) ]
            # pprint(vehintf15)

            Vehiclerface16 = namedtuple('Vehiclerface16', headers16)
            vehintf16 = [ Vehiclerface16(*oiinv.values()) for oiinv in iter(intf.orgintfinside_(uio)) if 16 == len(oiinv) ]
            # pprint(vehintf16)

            vehintf = vehintf15 + vehintf16
            for butt in vehintf:
                if "up" == butt.ifOperStatus:
                    # (" @ pageJson_pings_wans: ", pageJson_pings_lans, self.__deviceName, butt['vrf'])
                    # self.main_todo(intf, butt)
                    aiopingstreloop = asyncio.new_event_loop()
                    asyncio.set_event_loop(aiopingstreloop)
                    # asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
                    ## asyncio.get_event_loop().run_until_complete(self.main_todo(intf, butt))
                    aiopingstreloop.run_until_complete(self.main_todo(intf, butt))
                else:
                    self.vtg_lan_snort_intf_id_.append(self.__deviceName)
                    self.vtg_lan_snort_intf_.append(reduce(lambda s, t: s + t, [ butt.name.upper().split('/')[1], ' ', Lansnort['LMB'].value[0] ]).center(30, ' '))