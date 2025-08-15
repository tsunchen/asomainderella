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
from rich.progress import Progress
from .time_probe_ import time_probe
from .vtg_volumector_ import PseudoSpoke


def dfprint(data) -> None:
    example = pd.DataFrame(data = data)
    example.set_index('device', inplace = True)
    example.sort_index(inplace = True)
    try:
        ex_df_devspokepriorityinspector_ = example.groupby('device', group_keys = False).apply(fmttab_)
    except Exception as e:
        print(" - DFPrintal: ", e)
    else:
        print('\r{}'.format(ex_df_devspokepriorityinspector_), end = '')
        print()


def fmttab_(data):
    return data.sort_values(by = 'spOke',ascending = True)


def devspokepasspertotal10sinspectorModel(orgName) -> None:

    pd.set_option('display.width', 200)  # 将总宽度设置为200个字符
    pd.set_option('display.max_colwidth', 100) # 将单列最大宽度设置为100个字符

    # 2022.12.13 globalless
    setattr(VTGThread_refractor, "vtg_devspokepriority_", [])
    # setattr(VTGThread_refractor, "vtg_devspokepriority_set", set())
    setattr(VTGThread_refractor, "vtg_devspokepriority_id_", [])
    _, d = VTG_appliance(deviceorg = orgName).location_
    # print(json.dumps(json.loads(d), indent = 4))
    devicesName_ = [ tc['applianceName'] for tc in json.loads(d).get("List").get('value') if tc['type'] != 'controller' and tc['type'] != 'hub' ]
    # 2021.1.20 _refractor
    setattr(VTGThread_refractor, "run", devspokepasspertotal10s)
    #
    thread_table = [ maximize(item, orgName) for item in devicesName_ ]
    [ thread.start() for thread in thread_table ]
    proc_bar = tqdm(thread_table)
    for p in thread_chain(proc_bar):
        proc_bar.set_postfix({"Cyber Tunnel": '{}'.format(p)}); p.join()
    #
    dfprint({'device': VTGThread_refractor.vtg_devspokepriority_, 'spOke': VTGThread_refractor.vtg_devspokepriority_id_})
    # 2024.4.7
    # print("Execution times for Pass per Total sequence using threading:", devspokepasspertotal10s.get_execution_times())
    # print("Total time for Pass per Total sequence using threading:", devspokepasspertotal10s.get_total_time(), "seconds")
    print("Average time for Pass per Total sequence using threading:", devspokepasspertotal10s.get_total_time() / len(devspokepasspertotal10s.get_execution_times()), "seconds")


async def shebang(self, devspokegrouphub_tunnelyield, item) -> None:
    """ range = 1 """
    sdnshebang = VTG_sdwan(devicename = self.__deviceName, deviceorg = self.__deviceOrg)
    itemres = [ await sdnshebang.devsla_path_metrics_aggregated_last_10s_brief_prime_spokegrouphub_(sgty) for sgty in devspokegrouphub_tunnelyield ]
    item += '* ' + ",".join(set(itemres))
    # self.vtg_devspokepriority_set.add(item)
    if "!" in item:
        # 2024.2.15 sub_progress task_id
        with Progress() as progress:
            self.vtg_devspokepriority_id_.append(str(item))
            self.vtg_devspokepriority_.append("" + self.__deviceName)
            task_id = progress.add_task(self.__deviceName)
            while not progress.finished:
                progress.update(task_id, advance = 1)


async def tunneltodo(self, devspokegrouphub_tunnelyield, item) -> None:
    # start = time.perf_counter()
    ## await asyncio.sleep(4.25)
    coros = [ self.shebang(devspokegrouphub_tunnelyield, item) ]
    await asyncio.gather(*coros, return_exceptions = True)
    # end = time.perf_counter()
    # print(f"{self.__deviceName} took {end - start:.2f}s")


@time_probe
def devspokepasspertotal10s(self) -> None:
    setattr(VTG_spokegroup, "default_pseudosg_", default_pseudosg_)
    setattr(VTGThread_refractor, "tunneltodo", tunneltodo)
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
    print(f"{devtemplateName}@{devSpoke}")
    aoiloop = asyncio.new_event_loop()
    asyncio.set_event_loop(aoiloop)
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    # -----------------------------------------------------------------
    # devSpoke is not None，Hub? on 4th AUG, 2025
    # -----------------------------------------------------------------
    hub_definitions = PseudoSpoke(volume="Volume-Vector").hub
    hubs_for_tenant = hub_definitions.get(self.__deviceOrg, [])

    if devSpoke is None or devSpoke in hubs_for_tenant:

        if devSpoke is not None:
            print(f"INFO: {devSpoke} is a hub for {self.__deviceOrg} {self.__deviceName}. Running pseudo-spoke connection logic for all devices.")

        sg = VTG_spokegroup(deviceorg = self.__deviceOrg)
        # pseudoSG = sg.default_pseudosg_
        ## 2024.12.10 Volume Vector for PseudoSpoke
        psg = PseudoSpoke(volume = "Volume-Vector").default_vector(self.__deviceOrg)
        for i in range(len(psg)):
            print(psg[i])
            devspokegrouphub_tunnelyield = [ psg[i] ]
            # print("devspokegrouphub_tunnelyield: ", devspokegrouphub_tunnelyield)
            aoiloop.run_until_complete(self.tunneltodo(devspokegrouphub_tunnelyield, psg[i]))

    else:
        # print(f"INFO: {devSpoke} is a hub for {self.__deviceOrg} {self.__deviceName}. Running pseudo-spoke connection logic.")
        # print("devSpoke is Some")
        # if all([ deviceOrgName == self.__deviceOrg, "Deployed" == workflowStatus, devSpoke is not None ]):
        # print("20240201 - devSpoke : ", devSpoke)
        # 2020.10.20 Spoke Prime
        sg = VTG_spokegroup(deviceorg = self.__deviceOrg)
        _, _ = sg.devspokegroup_(devSpoke)
        # 2020.10.21 devspokegroup_hubs_
        devspokegrouphub_tunnelyield = sg.devspokegroup_hub_priority_()
        # print("devspokegrouphub_tunnelyield: ", devspokegrouphub_tunnelyield)
        aoiloop.run_until_complete(self.tunneltodo(devspokegrouphub_tunnelyield, devSpoke))