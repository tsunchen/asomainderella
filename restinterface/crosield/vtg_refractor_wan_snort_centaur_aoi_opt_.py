#!/usr/bin/python
#coding: UTF-8
from .vtg_attemptable_ import *
from ...director.refractor_ import VTGThread_refractor, maximize
import pandas as pd
from .vtg_appliance_ import *
from tqdm import tqdm
from threading import Lock
import asyncio
from ...director.fusable_ import Wansnort, Lansnort
from .vtg_vector_ import default_wantable_
import polars as pl
# from .asyncinventories.async_iterator_ import AsyncIteratorWrapper


def waninspectorModelaoi(orgName):
    setattr(VTGThread_refractor, "wantodo", wantodo)
    setattr(VTGThread_refractor, "shebang", shebang)
    # 2022.12.13 globalless
    setattr(VTGThread_refractor, "vtg_wan_snort_intf_", [])
    setattr(VTGThread_refractor, "vtg_wan_snort_intf_id_", [])
    # 2021.1.20 _refractor
    setattr(VTGThread_refractor, "run", wan_snortaoi)
    # overlte(self, butt, intf)
    setattr(VTGThread_refractor, "overlte", overlte)
    # alert(self, butt, inft)
    setattr(VTGThread_refractor, "alert", alert)
    # park(self, butt, inft)
    setattr(VTGThread_refractor, "park", park)
    # failover
    setattr(VTGThread_refractor, "failover", failover)
    # hoperight
    setattr(VTGThread_refractor, "hoperight", hoperight)
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
        proc_bar = tqdm(thread_table)
        [ thread.start() for thread in thread_table ]
        [ p.join() for p in proc_bar ]
        # [ proc_bar.set_description('-> {}'.format(p)) for p in proc_bar ]
        dfprintpd({'Envirolink': VTGThread_refractor.vtg_wan_snort_intf_, 'IntfId': VTGThread_refractor.vtg_wan_snort_intf_id_})
        dfprintpl({'Envirolink': VTGThread_refractor.vtg_wan_snort_intf_, 'IntfId': VTGThread_refractor.vtg_wan_snort_intf_id_})


def fmt_shadowing_(data):
    # 2024.2.29 pola shadowing
    df = data.sort('IntfId')
    return  df.filter(pl.col('Envirolink').is_in([
        ## "N.P.A".center(30, ' '),
        ## "LTE-Transport-VR [`.P.`]".center(30, '.'),
        "LTE-Transport-VR ['MONITOR']".center(30, '-'), ] 
        ).is_not()
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
        ex_centaur_ = example.group_by("Envirolink").apply(fmt_shadowing_)
    except Exception as e:
        print(" Error caused by WAN is empty. ")
    else:
        print('\r{}'.format(ex_centaur_), end = '') 
        print()


def fmt_tab_(data):
    df = data.sort_values(by = 'Envirolink', ascending = True)
    return df[~df.Envirolink.isin([
        ## "N.P.A".center(30, ' '),
        "LTE-Transport-VR ['MONITOR']".center(30, '-'), ] 
    )]


def dfprintpd(data):
    example = pd.DataFrame(data = data)
    # 2020.11.23
    example.set_index('IntfId', inplace = True)
    ex_centaur_ = example.groupby('IntfId', group_keys = False).apply(fmt_tab_) # 2022.1.25 fmt_tab_
    print('\r{}'.format(ex_centaur_), end = '') # 2022.5.10 print\r
    print()


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


def hoperight(self, tag):
    # 2024.3.2 painleft
    # Wansnort['CRITICAL'].value[0].center(30, '.')
    print(f'- ! Off Line: {self.__deviceName} {self.__deviceOrg}')
    self.vtg_wan_snort_intf_id_.append(self.__deviceName)
    self.vtg_wan_snort_intf_.append(tag)


async def shebang(self, butt, intf, hostNamei, count):
    # print(butt, intf, hostNamei, count)
    """ butt['if-oper-status'] 2024.3.2 """
    if "up" == butt['if-oper-status']:
        """ count = 1 """
        devshebang = VTG_device(devicename = self.__deviceName)
        state = await devshebang.aoipingw_(hostname = hostNamei, routingInstance = butt['vrf'], count = count)
        if "success" != state:
            self.failover(butt, intf, hostNamei)
            print(f" - {self.__deviceName} {butt['vrf']} {hostNamei} {devshebang}:{state}")
    else:
        self.alert(butt, intf, Wansnort['ALERT'].value[0])


async def wantodo(self, butt, intf):
    start = time.perf_counter()
    hostName = intf.default_wan_table_
    ## await asyncio.sleep(4.25)
    coros = [ self.shebang(butt, intf, hostName[i], count = 1) for i in range(len(hostName)) ]
    await asyncio.gather(*coros, return_exceptions = True)
    end = time.perf_counter()
    print(f"{self.__deviceName}.{butt['name']} took {end - start:.2f}s")


def wan_snortaoi(self):
    setattr(VTG_interface, "default_wan_table_", default_wantable_)
    self.__delay = threading.current_thread().delay
    self.__deviceName = threading.current_thread().deviceName
    self.__deviceOrg = threading.current_thread().deviceOrg
    # time.sleep(int(self.__delay))
    with VTG_interface(devicename = self.__deviceName, deviceorg = self.__deviceOrg) as (uio, intf):
        if (Wansnort['CRITICAL'].value[0] == uio):
            self.hoperight(Wansnort['CRITICAL'].value[0].center(30, '.'))
        else:
            ## [ self.alert(butt, intf, Wansnort['ALERT'].value[0]) for butt in intf.orgintfnocloudnet_(uio) if "down" == butt['if-oper-status'] ]
            aoipingwloop = asyncio.new_event_loop()
            asyncio.set_event_loop(aoipingwloop)
            # asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
            [ aoipingwloop.run_until_complete(self.wantodo(butt, intf)) for butt in intf.orgintfnocloudnet_(uio) ]