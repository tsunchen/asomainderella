#!/usr/bin/python
#coding: UTF-8
from .cfue_shct_ import *
from .aoicfu_ import *

class VTG_device:

    __slots__ = ( "__vtg_device", "__network", "__ping", "__pingw", "__scp", "__bw", "__deviceName" )

    VTG_device = '/vnms/sdwan/workflow/devices/device/'

    def __init__(self, *args, **kwargs):
        self.__deviceName = kwargs['devicename']
        self.__bw = '/api/config/devices/device/{}/config/system/bw-measurement/_operations/client/'.format(self.__deviceName)
        self.__scp = '/api/config/devices/device/{}/config/diagnostics:diagnostics/_operations/scp/'.format(self.__deviceName)
        self.__pingw = '/api/config/devices/device/{}/config/diagnostics:diagnostics/_operations/ping/'.format(self.__deviceName)
        self.__ping = '/api/config/devices/device/{}/_operations/ping'.format(self.__deviceName)
        self.__network = '/api/config/devices/device/{}/config/networks/network'.format(self.__deviceName)
        self.__vtg_device = ''.join([ self.__class__.VTG_device, self.__deviceName ])


    def availableId(self):
        # /vnms/sdwan/global/Branch/availableId/withSerialNumber # {"AvailableIDResponseModel":{"branchId":"123","serialNumbmer":"0b3eff73-66c4-4c8d-a00c-eba77d911010"}}
        d, rc = Restinterface('/vnms/sdwan/global/Branch/availableId/withSerialNumber', 0, 'get').action_restinterface_()
        data = json.loads(d)
        deviceAvailableId = data["AvailableIDResponseModel"]["branchId"]
        # print("availableId_: ", rc)
        # print("availableId_: ", deviceAvailableId)
        return rc, deviceAvailableId


    @property
    def bindData(self):
        d, rc = Restinterface(self.__vtg_device, 0, 'get').action_restinterface_()
        deviceTemplateVariableAttrs = json.loads(d)["versanms.sdwan-device-workflow"]['postStagingTemplateInfo']['templateData']['device-template-variable']['variable-binding']['attrs']
        return deviceTemplateVariableAttrs


    def bindData_(self):
        d, rc = Restinterface(self.__vtg_device, 0, 'get').action_restinterface_()
        data = json.loads(d)
        deviceTemplateVariableAttrs = data["versanms.sdwan-device-workflow"]['postStagingTemplateInfo']['templateData']['device-template-variable']['variable-binding']['attrs']
        # print("bindData_: ", rc)
        # print("bindData_: ", d)
        return rc, deviceTemplateVariableAttrs


    def specificServiceTemplate_(self):
        d, rc = Restinterface(self.__vtg_device, 0, 'get').action_restinterface_()
        data = json.loads(d)
        try:
            specificServiceTemplate_ = data['versanms.sdwan-device-workflow']['deviceSpecificServiceTemplates'][0]['name']
        except (KeyError, IndexError):
            specificServiceTemplate_ = "No Specific" # None
            # print("specificServiceTemplate_: ", rc)
            # print("specificServiceTemplate_: ", d)
        return rc, specificServiceTemplate_


    def serialNumber_(self):
        d, rc = Restinterface(self.__vtg_device, 0, 'get').action_restinterface_()
        data = json.loads(d)
        serialNumber_ = data['versanms.sdwan-device-workflow']['serialNumber']
        # print("serialNumber_: ", rc)
        # print("serialNumber_: ", d)
        return rc, serialNumber_


    def workflowStatus_(self):
        d, rc = Restinterface(self.__vtg_device, 0, 'get').action_restinterface_()
        data = json.loads(d)
        workflowStatus_ = data['versanms.sdwan-device-workflow']['workflowStatus']
        # print("workflowStatus_: ", rc)
        # print("workflowStatus_: ", d)
        return rc, workflowStatus_


    def deviceOrgName_(self):
        d, rc = Restinterface(self.__vtg_device, 0, 'get').action_restinterface_()
        data = json.loads(d)
        orgName = data['versanms.sdwan-device-workflow']['orgName']
        # print("deviceOrgName_: ", rc)
        # print("deviceOrgName_: ", d)
        return rc, orgName


    def templateName_(self):
        # 2020.08.30
        #/vnms/sdwan/workflow/devices/device/<appliance-name>
        d, rc = Restinterface('/vnms/sdwan/workflow/devices/device/{}'.format(self.__deviceName), 0, 'get').action_restinterface_()
        data = json.loads(d)
        templateName_ = data["versanms.sdwan-device-workflow"]["postStagingTemplateInfo"]["templateName"]
        # print("templateName_: ", rc)
        # print("templateName_: ", templateName)
        return rc, templateName_


    def alarm_(self):
        #/api/operational/alarms/alarm-list/alarm
        #/api/operational/devices/device/<appliance-name>/live-status/alarms/statistics/org
        #/api/config/devices/device/<appliance-name>/config/alarms/alarm
        #ri_misc_alarm_urlpath = '/api/config/devices/device/' + self.__deviceName + '/config/alarms/alarm'
        alarm_, rc = Restinterface('/api/operational/alarms/alarm-list/alarm', 0, 'get').action_restinterface_()
        print("alarm_: ", rc)
        # print("alarm_: ", alarm_)
        return rc, alarm_


    def sync_(self):
        #/api/config/devices/device/Yum-China-SH-CPE-01/_operations/check-sync
        sync_, rc = Restinterface('/api/config/devices/device/{}/_operations/check-sync/'.format(self.__deviceName), 0, 'post').action_restinterface_()
        print("sync_: ", rc)
        print("sync_: ", sync_)
        return rc, sync_


    def yangModules_(self):
        #/api/config/devices/device/Yum-China-SH-CPE-01/_operations/check-yang-modules
        yangModules_, rc = Restinterface('/api/config/devices/device/{}/_operations/check-yang-modules'.format(self.__deviceName), 0, 'post').action_restinterface_()
        print(rc)
        print(yangModules_)
        return rc, yangModules_


    @property
    def connect_(self):
        #/api/config/devices/device/Yum-China-SH-CPE-01/_operations/connect
        d, rc = Restinterface('/api/config/devices/device/{}/_operations/connect'.format(self.__deviceName), 0, 'post').action_restinterface_()
        print("connect_: ", rc)
        return rc, json.loads(d).get('output').get('result')


    def decommission_(self):
        decommission_, rc = Restinterface('/vnms/sdwan/workflow/devices/device/{}'.format(self.__deviceName), 0, 'delete').action_restinterface_()
        print(rc)
        print(decommission_)
        return rc, decommission_


    def deploy_(self):
        deploy_, rc = Restinterface('/vnms/sdwan/workflow/devices/device/deploy/{}'.format(self.__deviceName), 0, 'post').action_restinterface_()
        print(rc)
        print(deploy_)
        return rc, deploy_


    def fetch_(self):
        fetch_, rc = Restinterface('/vnms/sdwan/workflow/devices/device/{}'.format(self.__deviceName), 0, 'get').action_restinterface_()
        # print(rc)
        # print(fetch_)
        return rc, fetch_


    def fetchall_(self):
        #/vnms/sdwan/workflow/devices
        fetchall_, rc = Restinterface('/vnms/sdwan/workflow/devices', 0, 'get').action_restinterface_()
        # print(rc)
        # print(fetchall_)
        return rc, fetchall_


    @property
    def networks_(self):
        networks_, rc = Restinterface(self.__network, 0, 'get').action_restinterface_()
        print(rc)
        print(networks_)
        return rc, networks_


    def ping_(self):
        rc, d = self.connect_()
        if (True == d):
            d, rc = Restinterface(self.__ping, 0, 'post').action_restinterface_()
            print("ping_: ", rc)
            return rc, json.loads(d).get('output').get('result')
        else:
            print(self.__deviceName + " connect time out")
            return "500", "100% packet loss, try to ping again after connecting"


    def push_(self, data):
        ri_device_pushconfig_urlpath = '/vnms/sdwan/workflow/devices/device'
        ri_device_pushconfig_ = Restinterface(ri_device_pushconfig_urlpath, json.dumps(data), 'post')
        d, rc = ri_device_pushconfig_.action_restinterface_()
        print(rc)
        return rc, d


    def pull_(self):
        ri_device_fetch_urlpath = '/vnms/sdwan/workflow/devices/device/' + self.__deviceName
        ri_device_fetch_ = Restinterface(ri_device_fetch_urlpath, 0, 'get')
        d, rc = ri_device_fetch_.action_restinterface_()
        # print("pull_: ", rc)
        # print("pull_: "d)
        return rc, d


    def restart_(self):
        ri_device_restart_urlpath = '/api/config/devices/device/' + self.__deviceName + '/config/system/_operations/restart/'
        ri_device_restart_ = Restinterface(ri_device_restart_urlpath, 0, 'post')
        d, rc = ri_device_restart_.action_restinterface_()
        print(rc)
        print(d)
        return rc, d


    def traceroute_(self, hostname = "8.8.8.8" ,routingInstance = "Internet-Transport-VR", source = "192.168.1.1"):
        data = {"traceroute": {"hostname": hostname
            ,"routing-instance": routingInstance 
            , "source": source
        }}
        #/api/config/devices/device/<APPLIANCE-NAME>/config/diagnostics:diagnostics/_operations/traceroute
        ri_device_traceroute_urlpath = '/api/config/devices/device/' + self.__deviceName + '/config/diagnostics:diagnostics/_operations/traceroute/'
        ri_device_traceroute_ = Restinterface(ri_device_traceroute_urlpath, json.dumps(data), 'post')
        d, rc = ri_device_traceroute_.action_restinterface_()
        data = json.loads(d)
        d = data['output']['result']
        print(rc)
        print(d)
        return rc, d


    async def aoipingstre_(self, hostname = "6.6.6.6", routingInstance = "LAN-Transport-VR", count = 4):
        data = {"ping": {"hostname": hostname
            , "routing-instance":  routingInstance
            , "count": count
        }}
        sessicfuepost = Aoicfu(self.__pingw, json.dumps(data), 'creates')
        d, _ = await sessicfuepost.action_restinterface_()
        return d.get('output').get('status'), d.get('output').get('result')


    def pingstre_(self, hostname = "6.6.6.6", routingInstance = "LAN-Transport-VR", count = 4):
        data = {"ping": {"hostname": hostname
            , "routing-instance":  routingInstance
            , "count": count
        }}
        d, _ = Restinterface(self.__pingw, json.dumps(data), 'post').action_restinterface_()
        return json.loads(d).get('output').get('status'), json.loads(d).get('output').get('result')


    def pings_(self, source, hostname = "8.8.8.8", routingInstance = "Internet-Transport-VR", count = 4):
        data = {"ping": {"hostname": hostname
            , "routing-instance":  routingInstance
            , "source": source
            , "count": count
        }}
        print("dumps: ", data)
        print(self.__deviceName)
        #/api/config/devices/device/<APPLIANCE-NAME>/config/diagnostics:diagnostics/_operations/ping
        d, rc = Restinterface(self.__pingw, json.dumps(data), 'post').action_restinterface_()
        print("pings_: ", rc)
        return rc, json.loads(d).get('output').get('result')


    async def aoipingw_(self, hostname = "8.8.8.8", routingInstance = "Internet-Transport-VR", count = 4):
        # 2023.5.13
        data = {"ping": {"hostname": hostname
            , "routing-instance":  routingInstance
            , "count": count
        }}
        sessicfuepost = Aoicfu(self.__pingw, json.dumps(data), 'creates')
        d, _ = await sessicfuepost.action_restinterface_()
        return d.get('output').get('status')


    def pingw_(self, hostname = "8.8.8.8", routingInstance = "Internet-Transport-VR", count = 4):
        data = {"ping": {"hostname": hostname
            , "routing-instance":  routingInstance
            , "count": count
        }}
        d, _ = Restinterface(self.__pingw, json.dumps(data), 'post').action_restinterface_()
        return json.loads(d).get('output').get('status')


    def pingx_(self, hostname = "8.8.8.8", routingInstance = "Internet-Transport-VR", count = 8, packetSize = 65507):
        """
        2025.6 Ping with maximum packet size rapidly to figure out for the more potential result
        """
        data = {"ping": {"hostname": hostname
            , "routing-instance":  routingInstance
            , "count": count
            , "packet-size": packetSize
            # , "rapid": "enable"
        }}
        d, _ = Restinterface(self.__pingw, json.dumps(data), 'post').action_restinterface_()
        return json.loads(d).get('output')


    def pingi_(self, source, deviceName, hostname = "8.8.8.8", routingInstance = "Internet-Transport-VR", count = 4):
        # pingi = '/api/operational/devices/device/{}/live-status/diagnostics:diagnostics/_operations/ping?rapid=enable'
        pingi = '/api/operational/devices/device/{}/live-status/diagnostics:diagnostics/_operations/ping'
        data = {"ping": {"hostname": hostname
            , "routing-instance":  routingInstance
            , "source": source
            , "count": count
            # , "packet-size": 45454
        }}
        # print(json.dumps(data))
        # 21.1 #/api/operational/devices/device/JinQiaoZhen-CPE-Shanghai-001/live-status/diagnostics:diagnostics/_operations/ping
        #                          /api/operational/devices/device/JinQiaoZhen-CPE-Shanghai-001/live-status/diagnostics:diagnostics/_operations/ping
        # 16.1 #/api/config/devices/device/<APPLIANCE-NAME>/config/diagnostics:diagnostics/_operations/ping
        # ri_device_pings_urlpath = '/api/config/devices/device/' + deviceName + '/config/diagnostics:diagnostics/_operations/ping'
        # print(json.dumps(data, indent = 4))
        # print(ri_device_pings_urlpath)
        # 2025.6 pingi
        d, rc = Restinterface(pingi.format(deviceName), json.dumps(data), 'post').action_restinterface_()
        print(rc)
        return rc, json.loads(d).get('output').get('result')


    def scp_(self, username, password):
        data = {"scp": {"server": hostname
            , "routing-instance":  routingInstance
            , "username": username
            , "password": password
        }}
        #/api/config/devices/device/Yum-China-SH-CPE-01/config/diagnostics:diagnostics/_operations/scp
        d, rc = Restinterface(self.__scp, json.dumps(data), 'post').action_restinterface_()
        data = json.loads(d)
        scp_ = data['output']['result']
        print(rc)
        print(scp_)
        return rc, scp_


    def bw_(self):
        bw_, rc = Restinterface(self.__bw, 0, 'get').action_restinterface_()
        # data = json.loads(d)
        # d = data['output']['result']
        print(rc)
        print(bw_)
        return rc, bw_