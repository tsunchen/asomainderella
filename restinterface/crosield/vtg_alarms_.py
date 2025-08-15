#!/usr/bin/python
#coding: UTF-8

#import yagmail
import threading, time

from .vtg_device_ import *


#
class VTG_alarms:
    def __init__(self, *args, **kwargs):
        pass
        ##self.__orgName = kwargs['deviceorg']
        ##self.__deviceName = kwargs['devicename']


    '''
    def mail_print_(self, contents):
        yagclient = yagmail.SMTP("rpc_tvm@163.com", host = "smtp.163.com")
        contents = contents
        yagclient.send(to = "chen.xinfeng@21viacloud.com",
            cc = ["chen.chaoqun.ext@99cloud.net"],
            subject = "This is mail print from VTG_alarms_ ...",
            contents = contents)
    '''


    def event_of_alarms_(self, site):
        ri_alarms_event_urlpath = '/api/operational/alarms/alarm-list/alarm'
        ri_alarms_event_ = Restinterface(ri_alarms_event_urlpath, 0, 'get')
        d, rn = ri_alarms_event_.action_restinterface_()
        data = json.loads(d)
        Alarm_ = [ alarm for alarm in data["alarm"] ]
        NodeEventSite_ = [ (a['device'], a['type'], a['status-change']) for a in Alarm_ if site == a['device'] ]
        return NodeEventSite_


    def number_of_alarms_(self):
        #/api/operational/alarms/alarm-list/number-of-alarms
        ri_alarms_number_urlpath = '/api/operational/alarms/alarm-list/number-of-alarms'
        ri_alarms_number_ = Restinterface(ri_alarms_number_urlpath, 0, 'get')
        d, rn = ri_alarms_number_.action_restinterface_()
        data = json.loads(d)
        NoA = data["number-of-alarms"]
        return NoA


    def detail_of_alarms_(self):
        ri_alarms_detail_urlpath = '/api/operational/alarms/alarm-list/alarm'
        ri_alarms_detail_ = Restinterface(ri_alarms_detail_urlpath, 0, 'get')
        d, rn = ri_alarms_detail_.action_restinterface_()
        data = json.loads(d)
        devicesAlarm_ = [ alarm['device'] for alarm in data["alarm"] ]
        return devicesAlarm_


