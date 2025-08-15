#!/usr/bin/python
#coding: UTF-8
from .vtg_interface_ import *
from .vtg_interfaces_ import *


def Attemptable_(intf, butt, deviceName, hostName, nStart, ok = "success"):
    """ (nStart, butt, deviceName, hostName, ok) """
    while nStart > 0:
        _, rc_try_ = intf.intfoperup_(operateinterfacename = butt['name'], devicename = deviceName)
        # print("try: ", rc_try_, butt['name'], deviceName)
        rc_back_ = VTG_device(devicename = deviceName).pingw_(hostname = hostName, routingInstance = butt['vrf'], count = 1)
        print('- On {} attempted by {} of {}, then result is {}.'.format(hostName, deviceName, butt['vrf'], rc_back_))
        # "success"  rc_back_:
        nStart -= 1
        if ok == rc_back_:
            raise Exception("- Iteration is aborted by interface being self-cured ahead of time. ", rc_back_)
        else:
            yield nStart


def Attemptable(butt, deviceName, hostName, nStart, ok = "success"):
    """ (nStart, butt, deviceName, hostName, ok) """
    while nStart > 0:
        _, rc_try_ = VTG_interfaces(devicename = deviceName).intfoperup_(operateinterfacename = butt['name'], devicename = deviceName)
        # print("try: ", rc_try_, butt['name'], deviceName)
        rc_back_ = VTG_device(devicename = deviceName).pingw_(hostname = hostName, routingInstance = butt['vrf'], count = 1)
        print('- On {} attempted by {} of {}, then result is {}.'.format(hostName, deviceName, butt['vrf'], rc_back_))
        # "success"  rc_back_:
        nStart -= 1
        if ok == rc_back_:
            # 2021.7.20 tsunc exception replace the stopiteration
            raise Exception("- Iteration is aborted by interface being self-cured ahead of time. ", rc_back_)
        else:
            yield nStart