#!/usr/bin/python
#coding: UTF-8
from .cfue_shct_ import *


""" 
Mergeable Functions
"""
# 2021.5.7 pings_wan_
def devpings_wan_(self, devicename, hostname = "8.8.8.8", routingInstance = "Internet-Transport-VR", count = 4):
    """ (self, devicename, hostname = "8.8.8.8", routingInstance = "Internet-Transport-VR", count = 4) """
    data = { "ping": {"hostname": hostname, "routing-instance":  routingInstance, "count": count } }
    # print("dumps: ", data)
    # print(self.__deviceName)
    # /api/config/devices/device/<APPLIANCE-NAME>/config/diagnostics:diagnostics/_operations/ping
    ri_device_pings_urlpath = '/api/config/devices/device/{}/config/diagnostics:diagnostics/_operations/ping'.format(devicename)
    d, rc = Restinterface(ri_device_pings_urlpath, json.dumps(data), 'post').action_restinterface_()
    data = json.loads(d)
    print(data)
    print("pings_wan_: ", rc)
    d = data['output']['result']
    print("pings_wan_: ", d)
    d = data['output']['status']
    print("pings_wan_: ", d)
    return rc, data['output']['status']