#!/usr/bin/python
#coding: UTF-8
from .vtg_devices_ import *


""" Mergeable Functions """
# 2021.5.5 keydefval_setter
def keydefval_(self, root, key, value):
    if ( root.get(key, None) is None):
        root.setdefault(key, value)
        # print('To associate [ {} <- {} ] '.format(key, value))
    return root[key]


# 2021.5.7 intfoperup_
def intfoperup_(self, operateinterfacename, devicename):
    """ (self, operateinterfacename, devicename) """
    data = { "oper-up": { "name": operateinterfacename } }
    ri_device_operup_urlpath = '/api/config/devices/device/{}/config/interfaces/_operations/oper-up'.format(devicename)
    operup_, rc = Restinterface(ri_device_operup_urlpath, json.dumps(data), 'post').action_restinterface_()
    print("operup_: ", rc)
    # print(operateinterfacename, devicename)
    # print("operup_: ", operup_)
    return rc, operup_


# 2021.9.28 intfopernoup_
# Force-Recipelx: noup_ -> up_
def intfopernoup_(self, operateinterfacename, seconds = 40):
    data = {  "oper-down": { "name": operateinterfacename, "seconds": seconds } }
    ri_device_operNoup_urlpath = '/api/config/devices/device/{}/config/interfaces/_operations/oper-down'.format(self.__deviceName)
    opernoup_, rc = Restinterface(ri_device_operNoup_urlpath, json.dumps(data), 'post').action_restinterface_()
    print("operNoup_: ", rc)
    # print("operNoup_: ", opernoup_) #400:transport closed
    return rc, opernoup_


class VTG_interfaces:
    __slots__ = ( '__deviceName' )
    # __slots__ = ( '__deviceName', '__orgName' )

    def __init__(self, *args, **kwargs):    
        # self.__orgName = kwargs['deviceorg']
        self.__deviceName = kwargs['devicename']
        # setattr(self, "intfoperup_", intfoperup_)


    def intfoperup_(self, operateinterfacename, devicename):
        """ (self, operateinterfacename, devicename) """
        data = { "oper-up": { "name": operateinterfacename } }
        ri_device_operup_urlpath = '/api/config/devices/device/{}/config/interfaces/_operations/oper-up'.format(devicename)
        operup_, rc = Restinterface(ri_device_operup_urlpath, json.dumps(data), 'post').action_restinterface_()
        print("operup_: ", rc)
        # print(operateinterfacename, devicename)
        # print("operup_: ", operup_)
        return rc, operup_