#!/usr/bin/python
#coding: UTF-8
from ...director.reflection_deco_ import VTGThread_reflectionDeco
from .vtg_appliance_ import *
from .vtg_org_ import *
import pandas as pd

vtg_device_path_ = []
vtg_device_path_pmset = set()

def fmttab_(data):
    df = data.sort_values(by = 'Remote', ascending = True)
    return df

def dfprint(data):
    example = pd.DataFrame(data = data)
    example.set_index('PLP', inplace = True)
    # print(example)
    ex_centaur_ = example.groupby('PLP', group_keys = False).apply(fmttab_) # 2024.10.14 group_keys
    # ex_centaur_ = example.groupby('PLP', as_index = False).apply(fmttab_) # 2022.1.25 fmttab_
    # print(ex_centaur_)
    print('\r{}'.format(ex_centaur_), end = '') # 2022.5.10 print\r
    print()

"""
    Path MPLS
"""
def pathmpls(self):
    # 2020.7.4 reflection_deco
    ## print("[%s]" % threading.current_thread().getName())
    thread_posted = threading.current_thread().getName()
    # print("[%s]" % thread_posted)
    self.__delay = int(thread_posted.split(":")[0])
    self.__deviceName = thread_posted.split(":")[1]
    self.__deviceOrg = thread_posted.split(":")[2]
    time.sleep(self.__delay)
    try:
        _, pathmetrics = VTG_org(devicename = self.__deviceName, deviceorg = self.__deviceOrg).path_pathmetrics_
        pathmetricsd = [ list(rpathmetric.values())[0] for rpathmetric in pathmetrics ]
    except KeyError:
        vtg_device_path_pmset.add(self.__deviceName)
        vtg_device_path_.append(','.join([self.__deviceName, self.__deviceName, "100"]))
    else:
        for pathmetric in pathmetricsd:
            if all([ "CPE" not in pathmetric, "controller" not in pathmetric]):
                _, pathmetricremote = VTG_org(devicename = self.__deviceName, deviceorg = self.__deviceOrg).path_pathmetric_remote_(pathmetric)
                pathmetricremoted = json.loads(pathmetricremote)
                for pathmetricr in pathmetricremoted['path-list']:
                    if ('MPLS' == pathmetricr['local-circuit'].upper()):
                        if ('0.00' != str(pathmetricr['pdu-loss-percentage'])):
                            vtg_device_path_.append(','.join([ self.__deviceName, pathmetric, str(pathmetricr['pdu-loss-percentage']) ]))


def pathmplsinspectorModel(orgName):
    import pandas as pd
    appliance = VTG_appliance(deviceorg = orgName)
    _, apploc = appliance.location_
    data = json.loads(apploc)
    print(json.dumps(data, indent = 4))
    devicesName_ = [ tc['applianceName'] for tc in data["List"]['value'] if all([tc['type'] != 'branch', tc['type'] != 'controller']) ]
    global vtg_device_path_
    vtg_device_path_.clear()
    global vtg_device_path_pmset
    vtg_device_path_pmset.clear()
    # 2020.7.4 reflection_deco
    setattr(VTGThread_reflectionDeco, "run", pathmpls)
    thread_table = []
    for item in devicesName_:
        delay = "0"
        thread_post = delay + ':' + item + ':' + orgName
        refdeco = VTGThread_reflectionDeco(thread_name = ("%s" % thread_post))
        thread_table.append(refdeco)
    for thread in thread_table:
        thread.start()
    for thread in thread_table:
        thread.join()
    localBranch, remoteBranch, loc_remote_plp = [], [], []
    for item in vtg_device_path_:
        local, remote, plp = item.split(',')
        # localBranch.append(local)
        remoteBranch.append(remote)
        loc_remote_plp.append("<!>") # 2024.10.14 Local replaced with PLP
    data = {'PLP': loc_remote_plp, 'Remote': remoteBranch}
    dfprint(data)
    ## df.to_csv(f'E:\\pyvenv\\Envs\\py3deco\\netlayor\\PLP_{orgName}_.csv')
    print("@ Recommandation based by MPLS Precision ")
    # self.file_message(' Path Mpls inspected by : ' + orgName +  ' execute is finish.')


"""
    Path Metrics
"""
def pathmetrics(self):
    # 2020.7.4 reflection_deco
    ## print("[%s]" % threading.current_thread().getName())
    thread_posted = threading.current_thread().getName()
    # print("[%s]" % thread_posted)
    self.__delay = int(thread_posted.split(":")[0])
    self.__deviceName = thread_posted.split(":")[1]
    self.__deviceOrg = thread_posted.split(":")[2]
    time.sleep(self.__delay)
    try:
        _, pathmetrics = VTG_org(devicename = self.__deviceName, deviceorg = self.__deviceOrg).path_pathmetrics_
        pathmetricsd_ = [ list(rpathmetric.values())[0] for rpathmetric in pathmetrics ]
    except KeyError:
        vtg_device_path_pmset.add(self.__deviceName)
        vtg_device_path_.append(','.join([self.__deviceName, self.__deviceName, "100", "100"]))
    else:
        for pathmetric in pathmetricsd_:
            _, pathmetricremote = VTG_org(devicename = self.__deviceName, deviceorg = self.__deviceOrg).path_pathmetric_remote_(pathmetric)
            pathmetricremoted = json.loads(pathmetricremote)
            for pathmetricr in pathmetricremoted['path-list']:
                vtg_device_path_.append(','.join([ self.__deviceName, pathmetric, str(pathmetricr['two-way-delay']), str(pathmetricr['pdu-loss-percentage']) ]))


def pathmetricsinspectorModel(orgName):
    import pandas as pd
    appliance = VTG_appliance(deviceorg = orgName)
    _, apploc = appliance.location_
    data = json.loads(apploc)
    print(json.dumps(data, indent = 4))
    devicesName_ = [ tc['applianceName'] for tc in data["List"]['value'] if tc['type'] != 'controller' ]
    global vtg_device_path_
    vtg_device_path_.clear()
    global vtg_device_path_pmset
    vtg_device_path_pmset.clear()
    # 2020.7.4 reflection_deco
    setattr(VTGThread_reflectionDeco, "run", pathmetrics)
    thread_table = []
    for item in devicesName_:
        delay = "0"
        thread_post = delay + ':' + item + ':' + orgName
        refdeco = VTGThread_reflectionDeco(thread_name = ("%s" % thread_post))
        thread_table.append(refdeco)
    for thread in thread_table:
        thread.start()
    for thread in thread_table:
        thread.join()
    print(f' - Number of the Dissociate Branch: {len(vtg_device_path_pmset)}')
    print(vtg_device_path_pmset)
    localBranch, remoteBranch, loc_remote_twd, loc_remote_plp = [], [], [], []
    for item in vtg_device_path_:
        local, remote, twd, plp = item.split(',')
        localBranch.append(local)
        remoteBranch.append(remote)
        loc_remote_twd.append(twd)
        loc_remote_plp.append(plp)
    edge_data = zip(localBranch, remoteBranch, loc_remote_twd, loc_remote_plp)
    df = pd.DataFrame(edge_data, columns = ['Local', 'Remote', 'TwoWayDelay', 'PduLossPercentage'])
    df.to_csv(f'E:\\pyvenv\\Envs\\py3deco\\netlayor\\Pathmetrics_{orgName}_.csv')
    # print('$' * 40)
    # self.file_message(' Path Metrics inspected by : ' + orgName +  ' execute is finish.')