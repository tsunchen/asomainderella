#!/usr/bin/python
#coding: UTF-8
from .vtg_attemptable_ import *
from ...director.refractor_ import VTGThread_refractor, maximize
import pandas as pd
from .vtg_appliance_ import *
from tqdm import tqdm
from threading import Lock
from functools import lru_cache


def lansuspendsoryModel(orgName):
    # 2022.12.13 globalless
    setattr(VTGThread_refractor, "vtg_lan_suspend_intf_", [])
    setattr(VTGThread_refractor, "vtg_lan_suspend_intf_id_", [])
    # 2021.1.20 _refractor
    setattr(VTGThread_refractor, "run", lan_suspend)
    _, d = VTG_appliance(deviceorg = orgName).location_
    # print(json.dumps(json.loads(d), indent = 4))
    # hub internet, cpe internet
    try:
        devicesName_ = [ tc['applianceName'] for tc in json.loads(d).get('List').get('value') if  'controller' != tc['type'] and 'hub' != tc['type'] ]
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
            proc_bar.set_postfix({"QLan": '{}'.format(p)})
            p.join()
        dfprint({'QLan': VTGThread_refractor.vtg_lan_suspend_intf_, 'IntfId': VTGThread_refractor.vtg_lan_suspend_intf_id_})


def fmttab_(data):
    df = data.sort_values(by = 'QLan', ascending = True)
    return df[~df.QLan.isin([
        ## "N.P.A".center(30, ' '),
        "LTE-Transport-VR ['MONITOR']".center(30, '-'), ] 
    )]


def dfprint(data):
    example = pd.DataFrame(data = data)
    example.set_index('IntfId', inplace = True)
    example.sort_index(inplace = True)
    try:
        ex_centaur_ = example.groupby('IntfId',as_index = False).apply(fmttab_)
    except Exception as e:
        print(" - DFPrintal: ", e)
    else:
        print('\r{}'.format(ex_centaur_), end = '')
        print()


@lru_cache(maxsize = 8)
def lan_suspend(self):
    setattr(VTG_interface, "default_lan_tables_", default_lan_tables_)
    self.__delay = threading.current_thread().delay
    self.__deviceName = threading.current_thread().deviceName
    self.__deviceOrg = threading.current_thread().deviceOrg
    time.sleep(int(self.__delay))
    with VTG_interface(devicename = self.__deviceName, deviceorg = self.__deviceOrg) as (uio, intf):
        #print(uio, self.__deviceName)
        #'''
        if "...U..." == uio:
            print(f'- ! Off-Line: {self.__deviceName} {self.__deviceOrg}')
            self.vtg_lan_suspend_intf_id_.append(self.__deviceName)
            self.vtg_lan_suspend_intf_.append("UNREACHABLE".center(30, '.'))
            # self.vtg_lan_suspend_intf_.append(Wansnort.CRITICAL.value[0].center(30, '.'))
        else:
            for butt in intf.orgintfinside_(uio):
                lan_sus = '/api/config/devices/device/{}/config/interfaces/vni/%22{}%22/enable'.format(self.__deviceName, butt.get('name').partition('.')[0])
                d, rc = Restinterface(lan_sus, json.dumps(""), 'get').action_restinterface_()
                if json.loads(d).get('enable'):
                    # suspend on lan
                    _, rc = Restinterface(lan_sus, json.dumps({ "enable" : False }), 'put').action_restinterface_()
                    print(self.__deviceName, " - Lan >>> suspended ", rc)
                    self.vtg_lan_suspend_intf_id_.append(self.__deviceName)
                    self.vtg_lan_suspend_intf_.append("SUSPENDED".center(30, '.'))
                else:
                    # resume on lan
                    _, rc = Restinterface(lan_sus, json.dumps({ "enable" : True }), 'put').action_restinterface_()
                    print(self.__deviceName, " - Lan >>> resumed ", rc)
                    self.vtg_lan_suspend_intf_id_.append(self.__deviceName)
                    self.vtg_lan_suspend_intf_.append("RESUMED".center(30, '.'))
        #'''