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
import asyncio
from .vtg_vector_ import Wan, default_wantable_
from ...director.fusable_ import Wansnort, Lansnort
import polars as pl


async def shebang(self, hostNamei, butt, count):
    if "up" == butt['if-oper-status']:
        """ count > 1 """
        devshebang = VTG_device(devicename = self.__deviceName)
        state, res = await devshebang.aoipingstre_(hostname = hostNamei, routingInstance = butt['vrf'], count = count)
        if "success" != state:
            print(devshebang, state)
            self.vtg_lan_snort_intf_id_.append(self.__deviceName)
            self.vtg_lan_snort_intf_.append(reduce(lambda s, t: s + t, [ butt['name'].upper().split('/')[1], ' ', Lansnort['RSR'].value[0], ' ', hostNamei, ' ', butt['vrf'] ]).center(30, '~'))
        packloss = res.split("\n")[-4:][2].split()[5]
        # print(self.__deviceName, packloss)
        if "0%" != packloss:
            self.vtg_lan_snort_intf_id_.append(self.__deviceName)
            self.vtg_lan_snort_intf_.append(reduce(lambda s, t: s + t, [ butt['name'].upper().split('/')[1], " R.Pack.Loss. ", packloss, ' ', hostNamei, ' ', butt['vrf'] ]).center(30, ' '))
    else:
        self.vtg_lan_snort_intf_id_.append(self.__deviceName)
        self.vtg_lan_snort_intf_.append(reduce(lambda s, t: s + t, [ butt['name'].upper().split('/')[1], ' ', Lansnort['LMB'].value[0] ]).center(30, ' '))


async def alan2do(self, intf, butt):
    start = time.perf_counter()
    hostName = intf.default_lan_tables_
    ## await asyncio.sleep(4.25)
    coros = [ self.shebang(hostName[i], butt, count = 1) for i in range(len(hostName)) ]
    results = await asyncio.gather(*coros, return_exceptions = True)
    end = time.perf_counter()
    # print(f"{self.__deviceName}.{butt['name']} spent {end - start:.2f}s")


def alaninspectorModel(orgName):
    # print("pre_mem", mem.memory_usage())
    # 2022.12.13 globalless
    setattr(VTGThread_refractor, "vtg_lan_snort_intf_", [])
    setattr(VTGThread_refractor, "vtg_lan_snort_intf_id_", [])
    # 2021.1.20 _refractor
    setattr(VTGThread_refractor, "run", lan_snort)
    _, d = VTG_appliance(deviceorg = orgName).location_
    # print(json.dumps(json.loads(data), indent = 4))
    devicesName_ = [ tc['applianceName'] for tc in json.loads(d).get('List').get('value') if all([ 'controller' != tc['type'], 'hub' != tc['type'] ]) ]
    thread_table = [ maximize(item, orgName) for item in devicesName_ * 1 ]
    # 2023.3.12 thread_chain
    proc_bar = tqdm(thread_table)
    [ ty.start() for ty in thread_chain(thread_table) ]
    # 2024.3.8 comprehensive
    [ p.join() for p in thread_chain(proc_bar)]
    # [ proc_bar.set_postfix({"Acentaur Snort Lan": '{}'.format(p)}) for p in thread_chain(proc_bar) ]
    # [ proc_bar.set_description('-> {}'.format(p)) for p in proc_bar ]
    # dfprint({'SnortLan': VTGThread_refractor.vtg_lan_snort_intf_, 'IntfId': VTGThread_refractor.vtg_lan_snort_intf_id_})
    # print("post_mem", mem.memory_usage())
    dfprintpl({'SnortLan': VTGThread_refractor.vtg_lan_snort_intf_, 'IntfId': VTGThread_refractor.vtg_lan_snort_intf_id_})


def fmt_shadowing_(data):
    # 2024.3.8 pola shadowing
    df = data.sort('IntfId')
    return df.filter(
        pl.col('SnortLan').str.contains("YF-ChongQing-LAN-VR-WAN").is_not()
    )


def dfprintpl(data):
    '''
    pl.Config.set_tbl_cols(10)
    pl.Config.set_fmt_str_lengths(10)
    pl.Config.set_tbl_width_chars(70)
    pl.Config.set_tbl_rows(2)
    pl.Config.set_tbl_formatting('NOTHING')
    pl.Config.set_tbl_column_data_type_inline(True)  
    pl.Config.set_tbl_dataframe_shape_below(True)
    ''' 
    # 2024.3.4 tbl_rows = 32
    cfg = pl.Config()
    cfg.set_tbl_rows(32).set_fmt_str_lengths(52)
    example = pl.DataFrame(data = data)
    # 2024.2.28 express
    try:
        ex_centaur_ = example.group_by('IntfId').apply(fmt_shadowing_)
    except Exception as e:
        print(" Error caused by LAN is empty. ")
    else:
        print('\r{}'.format(ex_centaur_), end = '') 
        print()


def fmt_tab_(data):
    df = data.sort_values(by = 'SnortLan', ascending = True)
    return df[ df.SnortLan.isin([ slan for slan in df.SnortLan if all([ "YF-ChongQing-LAN-VR-WAN" not in slan ]) ]) ]


def dfprint(data):
    example = pd.DataFrame(data = data)
    example.set_index('IntfId', inplace = True)
    ex_centaur_ = example.groupby('IntfId', as_index = False).apply(fmt_tab_)
    print('\r{}'.format(ex_centaur_), end = '')
    print()


@lru_cache(maxsize = 8)
def lan_snort(self):
    setattr(VTGThread_refractor, "alan2do", alan2do)
    setattr(VTGThread_refractor, "shebang", shebang)
    setattr(VTG_interface, "default_lan_tables_", default_lan_tables_)
    self.__delay = threading.current_thread().delay
    self.__deviceName = threading.current_thread().deviceName
    self.__deviceOrg = threading.current_thread().deviceOrg
    time.sleep(int(self.__delay))
    with VTG_interface(devicename = self.__deviceName, deviceorg = self.__deviceOrg) as (uio, intf):
        if (Wansnort['CRITICAL'].value[0] == uio):
            print(f'- ! Off-Line: {self.__deviceName} {self.__deviceOrg}')
            self.vtg_lan_snort_intf_id_.append(self.__deviceName)
            self.vtg_lan_snort_intf_.append(Wansnort['CRITICAL'].value[0].center(30, '.'))
        else:
            apingstreloop = asyncio.new_event_loop()
            asyncio.set_event_loop(apingstreloop)
            [ apingstreloop.run_until_complete(self.alan2do(intf, butt)) for butt in intf.orgintfinside_(uio) ]