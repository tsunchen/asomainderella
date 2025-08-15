#!/usr/bin/python
#coding: UTF-8
from .vtg_template_ import *
from .vtg_device_ import *
from .vtg_appliance_ import *
from ...director.refractor_ import VTGThread_refractor, maximize, thread_chain
import pandas as pd
from tqdm import tqdm


def fmttab_(data):
    df = data.sort_values(by = 'device',ascending = True)
    return df


def devspokesumm(self):
    self.__delay = threading.current_thread().delay
    self.__deviceName = threading.current_thread().deviceName
    self.__deviceOrg = threading.current_thread().deviceOrg
    time.sleep(int(self.__delay))
    # 2020.9.2 devicesName -> devSpoke(Deployed)
    device = VTG_device(devicename = self.__deviceName)
    _, devtemplateName = device.templateName_()
    # print(devtemplateName)
    _, deviceOrgName = device.deviceOrgName_()
    _, workflowStatus = device.workflowStatus_()
    template = VTG_template(pst = devtemplateName)
    _, devSpoke = template.spoke_()
    if (deviceOrgName == self.__deviceOrg and "Deployed" == workflowStatus and devSpoke is not None):
        self.vtg_devspokesum_set.add(devSpoke)
        self.vtg_devspokesum_id_.append(str(devSpoke))
        self.vtg_devspokesum_.append(self.__deviceName)


def dfprint_spoke(data):
    example = pd.DataFrame(data = data)
    example.set_index('spoke', inplace = True)
    ex_df_devspokesummaryinspector_ = example.groupby('spoke', as_index = False).apply(fmttab_)
    print('\r{}'.format(ex_df_devspokesummaryinspector_), end = '')
    print()


def dfprint_spoke_summary(data):
    example = pd.DataFrame(data = data)
    ex_df_devspokesummaryinspector_ = example.groupby('spoke').device.sum().reset_index('spoke')
    ranges_ex21_ = [ item.count("CPE") for item in ex_df_devspokesummaryinspector_.device ]
    ex_df_devspokesummaryinspector_['ranges'] = ranges_ex21_
    ex_df_devspokesummaryinspector_['device'] = "="
    print(ex_df_devspokesummaryinspector_)


def devspokesumminspectorModel(orgName):
    setattr(VTGThread_refractor, "vtg_devspokesum_", [])
    setattr(VTGThread_refractor, "vtg_devspokesum_set", set())
    setattr(VTGThread_refractor, "vtg_devspokesum_id_", [])
    _, d = VTG_appliance(deviceorg = orgName).location_
    data = json.loads(d)
    print(json.dumps(data, indent=4))
    devicesName_ = [ tc['applianceName'] for tc in json.loads(d).get("List").get('value') if tc['type'] != 'controller' and tc['type'] != 'hub' ]
    setattr(VTGThread_refractor, "run", devspokesumm)
    thread_table = [ maximize(item, orgName) for item in devicesName_ ]
    [ thread.start() for thread in thread_table ]
    proc_bar = tqdm(thread_table)
    for p in thread_chain(proc_bar):
        proc_bar.set_postfix({"Cyber Tunnel": '{}'.format(p)}); p.join()
    # 2023.5.24
    data = {'device': VTGThread_refractor.vtg_devspokesum_, 'spoke': VTGThread_refractor.vtg_devspokesum_id_}
    dfprint_spoke_summary(data)
    dfprint_spoke(data)