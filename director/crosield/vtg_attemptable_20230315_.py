#!/usr/bin/python
#coding: UTF-8
#from .vtg_interface_ import *
#from .vtg_interfaces_ import *
from enum import Enum


def Attemptable(intf, butt, deviceName, hostName, nStart, ok = "success"):
    """ (nStart, butt, deviceName, hostName, ok) """
    while nStart > 0:
        _, rc_try_ = intf.intfoperup_(operateinterfacename = butt['name'], devicename = deviceName)
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


class Lansnort(Enum):
    __slots__ = ( "ALERT", "RSR" )
    ALERT = ('[`]A[`]', 'oper = dn', 'admin = up', '#dda0dd', '#ffffff')
    RSR   = ('[`]R[`]', 'oper = up', 'admin = up', '#dda0dd', '#ffffff') # REQUEST SYSTEM REBOOT


class Wansnort(Enum):
    __slots__ = ( "ETHER", "NPA", "LTEM", "CRITICAL", "MONITOR", "INFO", "ALERT", "PARK", "OVERLTE", "OVER5G" )

    OVER5G   = ('[^.5.^]', 'oper = up', 'admin = up')
    OVERLTE  = ('[^.4.^]', 'oper = up', 'admin = up')
    PARK     = ('[`.P.`]', 'oper = up', 'admin = up', 'ping = disable')
    ALERT    = ('[`]A[`]', 'oper = dn', 'admin = up')
    INFO     = ('[`]I[`]', 'oper = dn', 'admin = up')
    MONITOR  = ('[`]M[`]', 'oper = dn', 'admin = up')
    CRITICAL = ('...U...', 'oper = dn', 'admin = dn')
    LTEM     = ("LTE-Transport-VR ['MONITOR']")
    NPA      = ('N.P.A')
    ETHER    = ('.ETHER.')