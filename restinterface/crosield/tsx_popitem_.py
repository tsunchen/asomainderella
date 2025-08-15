#!/usr/bin/python
#coding: UTF-8
#from tkinter import *
import tkinter.messagebox
import json
from .cinirw_ import ReadConfigIni
from .vtg_overloop_ import *
from .popitem_pathmetric_dp_ import popitem_pathmetric_dataprocessor as DataProcessor
from .popitem_pathmetric_dp_ import popitem_pathmetric_edgedataprocessor as EdgeDataProcessor


def cohoMethod(method):
    def wrapper(self):
        setattr(self, method.__name__, method)
        return self
    return wrapper


# """ POPITEM """
def popitem_pathmetric(self):
        """ Path Metric on 4th May 2022 """
        from .vtg_org_ import VTG_org
        import pandas as pd
        import numpy as np
        print("lDoubleclick: ", self.fetchdevicenameByitem_brief)
        print()
        if ("PY_VAR3" == str(self.fetchdevicenameByitem_brief)):
            tkinter.messagebox.showinfo("Tip", "[Needing Parameter]: Popitem path-metrics")
        else:
            _, pathmetrics = VTG_org(devicename = self.fetchdevicenameByitem_brief, deviceorg = self.pulldevicenameByTenant.get()).path_pathmetrics_
            localbranch, remotebranch, lr_twd, localcircuit = [], [], [], []
            pathmetricsd = [ list(rpathmetric.values())[0] for rpathmetric in pathmetrics ]
            for pathmetric in pathmetricsd:
                if ("CPE" not in pathmetric and "controller" not in pathmetric):
                    _, pathmetricremote = VTG_org(devicename = self.fetchdevicenameByitem_brief, deviceorg = self.pulldevicenameByTenant.get()).path_pathmetric_remote_(pathmetric)
                    pathmetricremoted = json.loads(pathmetricremote)
                    ## print(pathmetricremoted)
                    for pathmetricr in pathmetricremoted['path-list']:
                        localbranch.append(self.fetchdevicenameByitem_brief)
                        remotebranch.append(pathmetric)
                        lr_twd.append(str(pathmetricr['two-way-delay']))
                        # 2024.9.19 localcircuit {'local-circuit'}
                        localcircuit.append(pathmetricr['local-circuit'])
            # Create an instance of the class with the data 2024.9.20
            edgedp = EdgeDataProcessor(remotebranch, lr_twd, localcircuit)
            # Process the data by adding random values and rounding
            edgedp.process_data()
            # Optimize the edge data (filter based on lr_twd > 1)
            edgedp.optimize_edge_data()
            # Retrieve and print the processed edge data # 'RemoteBranch', 'TwoWayDelay', 'LocalCircuit'
            df = pd.DataFrame(edgedp.get_edge_data(), columns = ['Device Point of Presence', 'Precision of Metric', 'Circuit'])
            print(df)
            """ - 20220606 - Egyptionic Data """
            # Create an instance of the class with the data
            processor = DataProcessor(remotebranch, edgedp.get_lr_twdd(), localcircuit)
            # Process the data
            processor.process_data()
            # Optimize and heapify lr_twdd
            processor.optimize_lr_twdd()
            # overloop method
            loop = OverLoop()
            loop.aview(processor.get_heapified_lr_twdd())
            loop.recommandationaview(processor.get_heapified_lr_twdd(), processor.get_resd())
            # 2024.9.19 optimize on overloop
            print("@ Recommandation based by Metric Precision ")
            ## df.to_csv(f'E:\\pyvenv\\Envs\\py3deco\\netlayor\\{self.fetchdevicenameByitem_brief}.csv')


def popitem_carrier(self):
        """ Carrier """
        if ("PY_VAR3" != str(self.fetchdevicenameByitem_brief)):
            self.formal_message("Intercarriers: " + self.fetchdevicenameByitem_brief)
            self.item_event_detail_interfacescarrier_info_()
            print("lDoubleclick: ", self.fetchdevicenameByitem_brief)
            print()
        else:
            tkinter.messagebox.showinfo("Tip", "[Needing Parameter]: Popitem intercarrier")


def popitem_recipelxintf(self):
        """ Recipelx """
        if ("PY_VAR3" != str(self.fetchdevicenameByitem_brief)):
            self.formal_message("Recipelx: " + self.fetchdevicenameByitem_brief)
            self.item_event_detail_recipelxintf_()
            print("lDoubleclick: ", self.fetchdevicenameByitem_brief)
            print()
        else:
            tkinter.messagebox.showinfo("Tip", "[Needing Parameter]: Popitem recipelx")


def popitem_interentries(self):
        """ Interentries """
        if ("PY_VAR3" != str(self.fetchdevicenameByitem_brief)):
            self.formal_message("Interentries: " + self.fetchdevicenameByitem_brief)
            self.item_event_detail_interfacesentry_info_()
            print("lDoubleclick: ", self.fetchdevicenameByitem_brief)
            print()
        else:
            tkinter.messagebox.showinfo("Tip", "[Needing Parameter]: Popitem interentries")


def popitem_interfaces(self):
        """ Interfaces """
        if ("PY_VAR3" != str(self.fetchdevicenameByitem_brief)):
            self.formal_message("Interfaces: " + self.fetchdevicenameByitem_brief)
            self.item_event_detail_interfaces_info_()
            print("lDoubleclick: ", self.fetchdevicenameByitem_brief)
            print()
        else:
            tkinter.messagebox.showinfo("Tip", "[Needing Parameter]: Popitem interfaces")


def popitem_assource(self):
        """ As Source """
        print("lDoubleclick: ", self.fetchdevicenameByitem_brief)
        print()
        if ("PY_VAR3" != str(self.fetchdevicenameByitem_brief)):
            self.formal_message("As Source: " + self.fetchdevicenameByitem_brief)
            self.fetchdevicenameByitem_event = self.fetchdevicenameByitem_brief
            print("rDoubleclick: ", self.fetchdevicenameByitem_event)
            print()
            self.vnilan()
        else:
            tkinter.messagebox.showinfo("Tip", "[Needing Parameter]: Popitem as source")


def popitem_hardware(self):
        """ Hardware """
        from .vtg_appliance_ import VTG_appliance
        # print("lDoubleclick: ", self.fetchdeviceuuidByitem_brief)
        # print()
        if ("PY_VAR7" != str(self.fetchdeviceuuidByitem_brief)):
            self.formal_message("Hardware: " + self.fetchdevicenameByitem_brief)
            appliance = VTG_appliance(deviceorg = self.pulldevicenameByTenant.get())
            _, d = appliance.hardware_(self.fetchdeviceuuidByitem_brief)
            data = json.loads(d)
            print("lDoubleclick: ", self.fetchdevicenameByitem_brief)
            print()
            tkinter.messagebox.showinfo("Hardware Detail ", json.dumps(data, indent = 4))
        else:
            tkinter.messagebox.showinfo("Tip", "[Needing Parameter]: Popitem hardware")


def popitem_event(self):
        """ Event """
        from .vtg_alarms_ import VTG_alarms
        print("lDoubleclick: ", self.fetchdevicenameByitem_brief)
        print()
        if ("PY_VAR3" != str(self.fetchdevicenameByitem_brief)):
            ala = VTG_alarms()
            nes_ = ala.event_of_alarms_(self.fetchdevicenameByitem_brief)
            self.formal_message("Event: " + self.fetchdevicenameByitem_brief)
            # print(json.dumps(nes_, indent = 4))
            tkinter.messagebox.showinfo("Event Detail ", json.dumps(nes_, indent = 4))
        else:
            tkinter.messagebox.showinfo("Tip", "[Needing Parameter]: Popitem event")


def popitem_httpsconft(self):
        """ HTTPs Conf T """
        from .vtg_interface_ import VTG_interface
        print("lDoubleclick: ", self.fetchdevicenameByitem_brief)
        print()
        if ("PY_VAR3" != str(self.fetchdevicenameByitem_brief)):
            _, d = VTG_interface(devicename = self.fetchdevicenameByitem_brief, deviceorg = self.pulldevicenameByTenant.get()).management_
            print("Https.Conf.T_: ", d)
        else:
            tkinter.messagebox.showinfo("Tip", "[Needing Parameter]: Popitem https-conf-t")


def popitem_renewal(self):
        """ Renewal """
        from .vtg_appliance_ import VTG_appliance
        if ("PY_VAR7" != str(self.fetchdeviceuuidByitem_brief)):
            self.formal_message("Branch: " + self.fetchdevicenameByitem_brief)
            appliance = VTG_appliance(deviceorg = self.pulldevicenameByTenant.get())
            _, d = appliance.hardware_(self.fetchdeviceuuidByitem_brief)
            data = json.loads(d)
            print()
            tkinter.messagebox.showinfo("SerialNo", json.dumps(data['versanms.Hardware']['hardWareSerialNo'], indent = 4))
            dSN = data['versanms.Hardware']['hardWareSerialNo']
            # print(dSN)
            self.selectPushFile()
            # print("Renewal Pushing Filename: ", self.pushfilename.get())
            # ReadConfigIni
            cfg = ReadConfigIni(self.pushfilename.get())
            try:
                rSN = cfg.getConfigValue("Basic", "serialnumber")
            except Exception as err:
                print(err)
            else:
                # print("renewalSerialNo: ", rSN)
                print(f'Branch ({self.fetchdevicenameByitem_brief}) to renew {[dSN]} with {[rSN]}.')
                rc, d = appliance.renewal_(dSN, rSN)
                if (500 == rc):
                    data = json.loads(d)
                    self.formal_message("Branch: " + f'- RMA exist and cancel firstly before renewing!')
                    errmessage = data['message']
                    print(f'- RMA exist and cancel firstly before renewing! {errmessage}')
                elif (200 == rc):
                    self.formal_message("Branch: " + f'- Key {rSN} standby is on success.')
                    # print(f'- Key {rSN} standby is on success.')
        else:
            # print("[Needing Parameter]: Popitem hardware")
            tkinter.messagebox.showinfo("Tip", "[Needing Parameter]: Popitem renewal")