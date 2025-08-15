#!/usr/bin/python
#coding: UTF-8
from ...director.refractor_ import VTGThread_refractor, uuidify
import pandas as pd
from .vtg_appliance_ import VTG_appliance, threading, json
from tqdm import tqdm
import polars as pl


def hwidnumsinspectorModel(orgName):
    setattr(VTGThread_refractor, "run", hardwareidnumbers)
    setattr(VTGThread_refractor, "vtg_hw_id_num_", [])
    setattr(VTGThread_refractor, "vtg_hw_id_num_id_", [])
    _, d = VTG_appliance(deviceorg = orgName).location_
    data = json.loads(d)
    print(json.dumps(data, indent = 4))
    # hub internet, cpe internet
    try:
        appItems_ = [ tc for tc in data["List"]['value'] if  'controller' != tc['type'] ]
    except Exception as e:
        # print(e)
        print(" Select the tenant priorly, please. ")
    else:
        thread_table = [ uuidify(item['applianceName'], orgName, item['applianceUuid']) for item in appItems_ ]
        proc_bar = tqdm(thread_table)
        [ thread.start() for thread in thread_table ]
        [ p.join() for p in proc_bar ]

        dfprintpl({'SN': VTGThread_refractor.vtg_hw_id_num_, 'HWId': VTGThread_refractor.vtg_hw_id_num_id_})
        dfprintpd({'SN': VTGThread_refractor.vtg_hw_id_num_, 'HWId': VTGThread_refractor.vtg_hw_id_num_id_})


def fmt_shadowing_(data):
    # 2024.2.29 pola shadowing
    df = data.sort('HWId')
    return  df.filter(pl.col('SN').is_in([
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
        ex_centaur_ = example.group_by("SN").apply(fmt_shadowing_)
    except Exception as e:
        print(" Error caused by HWID is empty. ")
    else:
        print('\r{}'.format(ex_centaur_), end = '') 
        print()


def fmt_tab_(data):
    df = data.sort_values(by = 'SN', ascending = True)
    return df[~df.SN.isin([
        ## "N.P.A".center(30, ' '),
        "LTE-Transport-VR ['MONITOR']".center(30, '-'), ] 
    )]


def dfprintpd(data):
    example = pd.DataFrame(data = data)
    # 2020.11.23
    example.set_index('HWId', inplace = True)
    ex_centaur_ = example.groupby('HWId', group_keys = False).apply(fmt_tab_) # 2022.1.25 fmt_tab_
    print('\r{}'.format(ex_centaur_), end = '') # 2022.5.10 print\r
    print()


def hardwareidnumbers(self):
    # asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) # 2024.11.1 relocation
    self.__delay = threading.current_thread().delay
    self.__deviceName = threading.current_thread().deviceName
    self.__deviceOrg = threading.current_thread().deviceOrg
    # print(self.__deviceName, self.__deviceOrg)
    self.__deviceUUID =  threading.current_thread().deviceUUID
    # print(self.__deviceName, self.__deviceUUID)
    try:
        _, d = VTG_appliance(deviceorg = self.__deviceOrg).hardware_(self.__deviceUUID)
        data = json.loads(d)
        # print(self.__deviceName, data['versanms.Hardware']['hardWareSerialNo'])
        item = data['versanms.Hardware']['hardWareSerialNo']    
    except KeyError as e:
        # print(self.__deviceName, '( No Hardware ID Number Found )')
        self.vtg_hw_id_num_id_.append(self.__deviceName)
        self.vtg_hw_id_num_.append('( No Hardware ID Number Found. Device maybe down. )')
    else:
        self.vtg_hw_id_num_id_.append(self.__deviceName)
        self.vtg_hw_id_num_.append(item)