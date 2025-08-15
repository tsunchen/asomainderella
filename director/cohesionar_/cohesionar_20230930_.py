#!/usr/bin/python
#coding: UTF-8
import requests
from requests.adapters import HTTPAdapter
from collections import Counter
import datetime
from urllib.parse import urljoin
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import os, pickle
import json, time
import tkinter
from .refractor_ import VTGThread_refractor
# from ...director.attemptable_ import Wansnort, Lansnort
from .attemptable_ import Lansnort


# class attr : model
# cfue : condition
def INTENT_RESTZ(*decoargs, **decokwargs):
    """
    INTENT_RESTZ
    """
    def wrapper(model):
        def inner_wrapper(self, *args, **kwargs):
            try:
                status_, rc = Restinterface(decokwargs['model'], 0, decokwargs['condition']).action_restinterface_()
                data = json.loads(status_)
            except json.decoder.JSONDecodeError:
                print("-- Error: json.decoder.JSONDecodeError, check Username and Password ")
                exit(0)
            else:
                print(f"-- LICENSE_{decokwargs['djson']}: {rc}")
                if decokwargs['djson'] == 'status':
                    a, b, c = data['output'][f"{decokwargs['djson']}"].split("\n")
                    print(a.strip(), c.strip())
                    import re
                    remain = re.compile(r'[(](.*?)[)]')
                    print('{} Day Countdown.'.format(re.findall(remain, b)[0].split(':')[1].strip()))
                else:
                    print(data) # version 21.2.x
                    # print(data[f"{decokwargs['djson']}"]) # version 16.x.x
            ## print(decokwargs['condition'])
            ## print(decokwargs['model'])
        return inner_wrapper
    return wrapper


seco_string_ = "parameter: secotime"

def step_str(*dargs, **dkwargs):
    """
    Count the function in number
    """
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            func(*args, **kwargs)
            outstep_ = str(f" The {inc()()} Done ! ")
            print(" -- -- -- -- -- ")
            print(f' {(outstep_)} ')
        return inner_wrapper
    return wrapper


def inc():
    def counter():
        count = 0
        while True:
            count += 1
            response = yield count
            if response is not None:
                count = response
    c = counter()
    return lambda x = False: c.send(0) if x else next(c)


class Softcohesion:

    @staticmethod
    def formal_message(msg):
        """
        - somaticohesion - 2023.3.3
        """
        result = tkinter.messagebox.askokcancel(title = 'message', message = msg)
        return result


    @staticmethod
    def pointmerge(targetobject = "VTGThread_refractor", point = "run", merger = "merger"):
        """
        Pointance of merge func 
        """
        def wrapper(func):
            def inner_wrapper(*args, **kwargs):
                setattr(targetobject, point, merger)
                func(*args, **kwargs)
            return inner_wrapper
        return wrapper

    @staticmethod
    def secit():
        """
        Count the function in seconds
        """
        def wrapper(func):
            def inner_wrapper(*args, **kwargs):
                sT = datetime.datetime.now() #start = time.clock()
                func(*args, **kwargs)
                eT = datetime.datetime.now() # print('{} sec'.format((eT - sT)))
                print(f" {(eT - sT)} sec ") #end = time.clock() #print('used: {}'.format(end - start))
            return inner_wrapper
        return wrapper

    @staticmethod
    def seco_str(*dargs, **dkwargs):
        """
        Count the function in seconds
        """
        def wrapper(func):
            def inner_wrapper(*args, **kwargs):
                sT = datetime.datetime.now()
                func(*args, **kwargs)
                eT = datetime.datetime.now()
                # print(dargs) # print(dkwargs) # print(f" {(eT - sT)} sec ")
                outseco_ = str(f" {(eT - sT)} ") # secotime_ = str(f" {(eT - sT).seconds} ")
                # print(" -- -- -- -- -- ")
                print(f'  Done with {(outseco_)}.  '.center(40, '-'))
            return inner_wrapper
        return wrapper

    # model = "Model"
    @staticmethod
    def Intention_IFELSE(*dargs, **dkwargs):
        """
        Intention_IFELSE
        """
        def wrapper(model):
            def inner_wrapper(self, *args, **kwargs):
                orgName = self.pulldevicenameByTenant.get()
                if ( orgName != "..." and orgName != "" ):
                    dkwargs['model'](orgName, *args, **kwargs)
                else:
                    self.formal_message(" Please select the organization about tenant firstly. ")
                ## print(dkwargs['condition'])
                ## print(dkwargs['model'])
            return inner_wrapper
        return wrapper


    # model = "Model"
    # condition = "Condition"
    # filter_message = "FilterMessage"
    @staticmethod
    def INTENT_IFELSE(*decoargs, **decokwargs):
        """
        INTENT_IFELSE
        """
        def wrapper(model):
            def inner_wrapper(self, *args, **kwargs):
                orgName = self.pulldevicenameByTenant.get()
                if ( orgName not in decokwargs['condition'] ):
                    decokwargs['model'](orgName, *args, **kwargs)

                    if "laninspectorModel" == decokwargs['model'].__name__:
                        for item in self.treeview.get_children():
                           self.treeview.tag_configure(self.treeview.item(item, "tags"), background = "#ffffff", foreground = "darkblue")

                        for chi in self.treeview.get_children():
                            if self.treeview.item(chi, "values")[1] in VTGThread_refractor.vtg_lan_snort_intf_id_:
                                # print(self.treeview.item(chi, "values"), chi)
                                # print(VTGThread_refractor.vtg_lan_snort_intf_id_.index(self.treeview.item(chi, "values")[1]))
                                lansnortintf_idx = VTGThread_refractor.vtg_lan_snort_intf_id_.index(self.treeview.item(chi, "values")[1])
                                # print(self.treeview.item(chi, "values")[1], VTGThread_refractor.vtg_lan_snort_intf_[lansnortintf_idx])
                                if Lansnort['LMB'].value[0] in VTGThread_refractor.vtg_lan_snort_intf_[lansnortintf_idx]:
                                    self.treeview.tag_configure(self.treeview.item(chi, "tags"), background = Lansnort['LMB'].value[3], foreground = Lansnort['LMB'].value[4])
                                if Lansnort['RSR'].value[0] in VTGThread_refractor.vtg_lan_snort_intf_[lansnortintf_idx]:
                                    self.treeview.tag_configure(self.treeview.item(chi, "tags"), background = Lansnort['RSR'].value[3], foreground = Lansnort['RSR'].value[4])
                                if Lansnort['UR'].value[0] in VTGThread_refractor.vtg_lan_snort_intf_[lansnortintf_idx]:
                                    self.treeview.tag_configure(self.treeview.item(chi, "tags"), background = Lansnort['UR'].value[3], foreground = Lansnort['UR'].value[4])

                        # flash treeview component
                        self.style = tkinter.ttk.Style()
                        self.style.map("Treeview", foreground = self.fixed_map("foreground"), background = self.fixed_map("background"))

                else:
                    self.formal_message(decokwargs['filter_message'])
                ## print(decokwargs['condition'])
                ## print(decokwargs['model'])
            return inner_wrapper
        return wrapper


    # model = "Model"
    @staticmethod
    def Intention_IF(*dargs, **dkwargs):
        """
        Intention_IF
        """
        def wrapper(model):
            def inner_wrapper(self, *args, **kwargs):
                devName = self.fetchdevicenameByitem_event
                orgName = self.pulldevicenameByTenant.get()
                if ( orgName != "..." and orgName != "" ):
                    dkwargs['model'](devName, orgName, *args, **kwargs)
                else:
                    self.file_message(" Please select the organization about tenant firstly. ")
                ## print(dkwargs['condition'])
                ## print(dkwargs['model'])
            return inner_wrapper
        return wrapper