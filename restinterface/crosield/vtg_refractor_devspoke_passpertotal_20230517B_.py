#!/usr/bin/python
#coding: UTF-8
import time, os
import pandas as pd
from .vtg_sdwan_ import *
from .vtg_spokegroup_ import *
from .vtg_template_ import *
from .vtg_device_ import *
from ...director.refractor_ import VTGThread_refractor, maximize, thread_chain
from .vtg_appliance_ import *
from tqdm import tqdm
import asyncio


def dfprint(data):
    example = pd.DataFrame(data = data)
    example.set_index('device', inplace = True)
    # print(example.sort_values(by = 'spOke'))
    ex_df_devspokepriorityinspector_ = example.groupby('device', as_index = False).apply(fmttab_)
    print('\r{}'.format(ex_df_devspokepriorityinspector_), end = '')
    print()


def fmttab_(data):
    df = data.sort_values(by = 'spOke',ascending = True)
    return df


def devspokepasspertotalinspectorModel(orgName):
    # 2022.12.13 globalless
    setattr(VTGThread_refractor, "vtg_devspokepriority_", [])
    setattr(VTGThread_refractor, "vtg_devspokepriority_set", set())
    setattr(VTGThread_refractor, "vtg_devspokepriority_id_", [])
    _, d = VTG_appliance(deviceorg = orgName).location_
    # print(json.dumps(json.loads(d), indent = 4))
    devicesName_ = [ tc['applianceName'] for tc in json.loads(d).get("List").get('value') if tc['type'] != 'controller' and tc['type'] != 'hub' ]
    # 2021.1.20 _refractor
    setattr(VTGThread_refractor, "run", devspokepasspertotal)

    thread_table = [ maximize(item, orgName) for item in devicesName_ ]
    [ thread.start() for thread in thread_table ]

    for p in thread_chain(proc_bar := tqdm(thread_table)):
        proc_bar.set_postfix({"Cloud Gateway": '{}'.format(p)}); p.join()

    dfprint({'device': VTGThread_refractor.vtg_devspokepriority_, 'spOke': VTGThread_refractor.vtg_devspokepriority_id_})


async def shebang(self, devspokegrouphub_tunnelyield, item):
    """ range = 1 """
    sdnshebang = VTG_sdwan(devicename = self.__deviceName, deviceorg = self.__deviceOrg)
    itemres = [ await sdnshebang.devsla_path_metrics_aggregated_last_1m_brief_prime_spokegrouphub_(item) for _ in range(4) for item in devspokegrouphub_tunnelyield ]
    item += '* ' + ",".join(set(itemres))
    if "+" in item:
        self.vtg_devspokepriority_set.add(item)
        self.vtg_devspokepriority_id_.append(str(item))
        self.vtg_devspokepriority_.append("" + self.__deviceName)


async def main_todo(self, devspokegrouphub_tunnelyield, item):
    start = time.perf_counter()
    ## await asyncio.sleep(4.25)
    coros = [ self.shebang(devspokegrouphub_tunnelyield, item) ]
    results = await asyncio.gather(*coros, return_exceptions = True)
    end = time.perf_counter()
    print(f"{self.__deviceName} took {end - start:.2f}s")


def devspokepasspertotal(self):
    setattr(VTGThread_refractor, "main_todo", main_todo)
    setattr(VTGThread_refractor, "shebang", shebang)
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
    if all([ deviceOrgName == self.__deviceOrg, "Deployed" == workflowStatus, devSpoke is not None ]):
        # print(devSpoke)
        # 2020.10.20 Spoke Prime
        sg = VTG_spokegroup(deviceorg = self.__deviceOrg)
        _, _ = sg.devspokegroup_(devSpoke)
        # 2020.10.21 devspokegroup_hubs_
        devspokegrouphub_tunnelyield = sg.devspokegroup_hub_priority_()

        aoiloop = asyncio.new_event_loop()
        asyncio.set_event_loop(aoiloop)
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        aoiloop.run_until_complete(self.main_todo(devspokegrouphub_tunnelyield, devSpoke))