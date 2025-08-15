#!/usr/bin/python
#coding: UTF-8

import threading, time

from .vtg_device_ import *

#
class VTG_vrouter:
    def __init__(self, *args, **kwargs):
        self.__orgName = kwargs['deviceorg']
        self.__deviceName = kwargs['devicename']
        self.__vrsrjson_data = "vrsrjson_data"
        self.__instanceId = "instanceId"
        self.__routeId = "routeId"
        self.__subRouteId = "subRouteId"


    def fetch_bgp_neighbor_lan_(self):
        deviceRoutinginstance = self.__orgName + "-LAN-VR"
        ri_device_fetch_bgpNeighborLan_urlpath = '/api/operational/devices/device/' + self.__deviceName + '/live-status/bgp/neighbors/detail/' + deviceRoutinginstance + '/neighbor-ip/'
        ri_device_fetch_bgpNeighborLan_ = Restinterface(ri_device_fetch_bgpNeighborLan_urlpath, 0, 'get')
        d, d2 = ri_device_fetch_bgpNeighborLan_.action_restinterface_()
        #print("fetch_bgpNeighborLan_: ", d2)
        #print("fetch_bgpNeighborLan_:", d)
        return d2, d


    def fetch_vrf_export_target_(self):
        deviceRoutinginstance = self.__orgName + "-LAN-VR-Export"
        ri_device_fetch_vrfExportTarget_urlpath = '/api/config/devices/device/' + self.__deviceName + '/config/routing-instances/routing-instance/' + deviceRoutinginstance + '/vrf-export-target'
        ri_device_fetch_vrfExportTarget_ = Restinterface(ri_device_fetch_vrfExportTarget_urlpath, 0, 'get')
        d, d2 = ri_device_fetch_vrfExportTarget_.action_restinterface_()
        data = json.loads(d)
        #print("fetch_vrfExportTarget_: ", d2)
        #print("fetch_vrfExportTarget_:", data['vrf-export-target'])
        return d2, data['vrf-export-target']


    def fetch_routeId_(self):
        deviceRoutinginstance = self.__orgName + "-Control-VR"
        ri_device_fetch_routeId_urlpath = '/api/config/devices/device/' + self.__deviceName + '/config/routing-instances/routing-instance/' + deviceRoutinginstance + '/protocols/bgp/rti-bgp'
        ri_device_fetch_routeId_ = Restinterface(ri_device_fetch_routeId_urlpath, 0, 'get')
        d, d2 = ri_device_fetch_routeId_.action_restinterface_()
        data = json.loads(d)
        print("fetch_routeId_: ", d2)
        print("fetch_routeId_:", data['rti-bgp'][0]['router-id'])
        self.__routeId = data['rti-bgp'][0]['router-id']
        print("self.__routeId: ", self.__routeId)
        self.__subRouteId = self.__routeId.split('.')[-1]
        print("self.__subRouteId: ", self.__subRouteId)
        return d2, d


    def fetch_instanceId_(self):
        deviceRoutinginstance = self.__orgName + "-Control-VR"
        ri_device_fetch_instanceId_urlpath = '/api/config/devices/device/' + self.__deviceName + '/config/routing-instances/routing-instance/' + deviceRoutinginstance + '/protocols/bgp/rti-bgp'
        ri_device_fetch_instanceId_ = Restinterface(ri_device_fetch_instanceId_urlpath, 0, 'get')
        d, d2 = ri_device_fetch_instanceId_.action_restinterface_()
        data = json.loads(d)
        print("fetch_instanceId_: ", d2)
        print("fetch_instanceId_:", data['rti-bgp'][0]['instance-id'])
        self.__instanceId = data['rti-bgp'][0]['instance-id']
        print("self.__instanceId: ", self.__instanceId)
        return d2, d


    def update_hub_lanslot_TO_SDWAN_(self):
        wildcard_match_community = "(^|,)8001:" + self.__subRouteId + "($|,)"
        vrsrconfig = {
          "routing-peer-policy": [
            {
              "name": "TO_SDWAN",
              "term": [
              {
                "term-name": "VersaPvt-Wildcard",
                "match": {
                  "family": "versa-private"
                },
                "action": {
                  "filter": "accept"
                }
              },
              {
                "term-name": "Wildcard",
                "match": {
                  "community": wildcard_match_community # "(^|,)8001:108($|,)"
                },
                "action": {
                  "filter": "accept"
                }
              },
              {
                "term-name": "Mark-Other-Region-Routes",
                "action": {
                  "filter": "accept",
                  "community": "8010:65535",
                  "community-action": "set-specific"
                }
              }
              ]
            }
          ]
        }
        self.__vrsrjson_data = vrsrconfig
        print("self.__vrsrjson_data: ", self.__vrsrjson_data)
        deviceRoutinginstance = self.__orgName + "-Control-VR"
        instanceId = self.__instanceId
        ri_vr_rinst_controlroute_update_objects_urlpath = '/api/config/devices/device/' + self.__deviceName + '/config/routing-instances/routing-instance/'  + deviceRoutinginstance + '/protocols/bgp/rti-bgp/' + str(self.__instanceId) + '/routing-peer-policy/TO_SDWAN'
        ri_vr_rinst_controlroute_update_objects_ = Restinterface(ri_vr_rinst_controlroute_update_objects_urlpath, json.dumps(self.__vrsrjson_data), 'put')
        d, d2 = ri_vr_rinst_controlroute_update_objects_.action_restinterface_()
        print("update_hub_lanslot_TO_SDWAN_: ", d2)
        print("update_hub_lanslot_TO_SDWAN_: ", d)
        return d2, d


    # update hub control vr
    # /api/config/devices/device/TYY-POP-SH-001/config/routing-instances/routing-instance/Customer-JZY-Control-VR/protocols/bgp/rti-bgp/7/routing-peer-policy/Import-From-SDWAN-Policy
    def update_hub_lanslot_ImportFromSDWANPolicy_(self):
        allowAll_match_extendedCommunity = "target:" + str(self.__instanceId) + "L:9999"
        lpFromSpokes_match_community = "8010:" + self.__subRouteId
        lpFromSpokes_match_extendedCommunity = "target:" + str(self.__instanceId) + "L:" + str(self.__instanceId)
        lowerLPFromSpokes_match_extendedCommunity = "target:" + str(self.__instanceId) + "L:" + str(self.__instanceId)
        vrsrconfig = {
          "routing-peer-policy": [
            {
              "name": "Import-From-SDWAN-Policy",
              "term": [
              {
                "term-name": "Allow-All",
                "match": {
                  "extended-community": allowAll_match_extendedCommunity # "target:7L:9999"
                },
                "action": {
                  "filter": "accept",
                  "community": "8009:8009",
                  "community-action": "set-specific"
                }
              },
              {
                "term-name": "Allow-VersaPvt-All",
                "match": {
                  "family": "versa-private"
                },
                "action": {
                  "filter": "accept"
                }
              },
              {
                "term-name": "Reject-Dup-Routes",
                "match": {
                  "community": "(^|,)8010:65535($|,)"
                },
                "action": {
                  "filter": "reject"
                }
              },
              {
                "term-name": "LP-From-Spokes",
                "match": {
                  "community": lpFromSpokes_match_community, # "8010:108",
                  "extended-community": lpFromSpokes_match_extendedCommunity # "target:7L:7"
                },
                "action": {
                  "filter": "accept",
                  "set-local-preference": 101
                }
              },
              {
                "term-name": "Lower-LP-From-Spokes",
                "match": {
                  "extended-community": lowerLPFromSpokes_match_extendedCommunity # "target:7L:7"
                },
                "action": {
                  "filter": "accept",
                  "set-local-preference": 90
                }
              },
              {
                "term-name": "Allow-Other-Region-Routes",
                "action": {
                  "filter": "accept"
                }
              }
              ]
            }
          ]
        }
        self.__vrsrjson_data = vrsrconfig
        deviceRoutinginstance = self.__orgName + "-Control-VR"
        print("self.__vrsrjson_data: ", self.__vrsrjson_data)
        instanceId = self.__instanceId
        ri_vr_rinst_controlroute_update_objects_urlpath = '/api/config/devices/device/' + self.__deviceName + '/config/routing-instances/routing-instance/'  + deviceRoutinginstance + '/protocols/bgp/rti-bgp/' + str(self.__instanceId) + '/routing-peer-policy/Import-From-SDWAN-Policy'
        ri_vr_rinst_controlroute_update_objects_ = Restinterface(ri_vr_rinst_controlroute_update_objects_urlpath, json.dumps(self.__vrsrjson_data), 'put')
        d, d2 = ri_vr_rinst_controlroute_update_objects_.action_restinterface_()
        print("update_hub_lanslot_ImportFromSDWANPolicy_: ", d2)
        print("update_hub_lanslot_ImportFromSDWANPolicy_: ", d)
        return d2, d


    def create_staticroute_(self, vrsrconfig):
        self.__vrsrjson_data = vrsrconfig
        deviceRoutinginstance = self.__orgName + "-LAN-VR"
        ri_vr_rinst_staticroute_create_objects_urlpath = '/api/config/devices/device/' + self.__deviceName + '/config/routing-instances/routing-instance/' + deviceRoutinginstance + '/routing-options/static/route/'
        ri_vr_rinst_staticroute_create_objects_ = Restinterface(ri_vr_rinst_staticroute_create_objects_urlpath, json.dumps(self.__vrsrjson_data), 'post')
        d, d2 = ri_vr_rinst_staticroute_create_objects_.action_restinterface_()
        print("create_staticroute_: ", d2)
        print("create_staticroute_: ", d)
        return d2, d


    def create_termstatic_(self):
        termStatic = {  "term": {    "term-name": "T99-Static",    "match": {      "protocol": "static"    },    "action": {      "filter": "accept",      "set-origin": "igp"    }  }}
        ri_vr_redistributionPolicy_term_create_objects_urlpath = '/api/config/devices/device/' + self.__deviceName + '/config/routing-instances/routing-instance/' + deviceRoutinginstance + '/policy-options/redistribution-policy/' + 'Default-Policy-To-BGP' + '/'
        ri_vr_redistributionPolicy_term_create_objects_ = Restinterface(ri_vr_redistributionPolicy_term_create_objects_urlpath, json.dumps(termStatic), 'post')
        d, d2 = ri_vr_redistributionPolicy_term_create_objects_.action_restinterface_()
        print("create_termstatic_:", d2)
        print("create_termstatic_:", d)
        return d2, d


    def create_staticroute_template_(self, vrsrconfig):
        self.__vrsrjson_data = vrsrconfig
        deviceRoutinginstance = self.__orgName + "-LAN-VR"
        ri_vr_rinst_staticroute_create_objects_urlpath = '/api/config/template/device/' + self.__deviceName + '/config/routing-instances/routing-instance/' + deviceRoutinginstance + '/routing-options/static/route/'
        ri_vr_rinst_staticroute_create_objects_ = Restinterface(ri_vr_rinst_staticroute_create_objects_urlpath, json.dumps(self.__vrsrjson_data), 'post')
        d, d2 = ri_vr_rinst_staticroute_create_objects_.action_restinterface_()
        print("create_staticroute_template_: ", d2)
        print("create_staticroute_template_: ", d)
        return d2, d


    def create_termstatic_bytemplate_(self):
        termStatic = {  "term": {    "term-name": "T77-Static",    "match": {      "protocol": "static"    },    "action": {      "filter": "accept",      "set-origin": "igp"    }  }}
        ri_vr_redistributionPolicy_term_create_objects_urlpath = '/api/config/devices/template/' + self.__deviceName + '/config/routing-instances/routing-instance/' + deviceRoutinginstance + '/policy-options/redistribution-policy/' + 'Default-Policy-To-BGP' + '/'
        ri_vr_redistributionPolicy_term_create_objects_ = Restinterface(ri_vr_redistributionPolicy_term_create_objects_urlpath, json.dumps(termStatic), 'post')
        d, d2 = ri_vr_redistributionPolicy_term_create_objects_.action_restinterface_()
        print("create_termstatic_bytemplate_:", d2)
        print("create_termstatic_bytemplate_:", d)
        return d2, d


    def append_staticroute_bytemplate_(self, vrsrconfig):
        self.__vrsrjson_data = vrsrconfig
        deviceRoutinginstance = self.__orgName + "-LAN-VR"
        ri_vr_rinst_staticroute_create_objects_urlpath = '/api/config/devices/template/' + self.__deviceName + '/config/routing-instances/routing-instance/' + deviceRoutinginstance + '/routing-options/static/route/'
        ri_vr_rinst_staticroute_create_objects_ = Restinterface(ri_vr_rinst_staticroute_create_objects_urlpath, json.dumps(self.__vrsrjson_data), 'post')
        d, d2 = ri_vr_rinst_staticroute_create_objects_.action_restinterface_()
        print("insert_staticroute_bytemplate_: ", d2)
        print("insert_staticroute_bytemplate_: ", d)
        return d2, d


    '''
    def erase_(self):
        ri_devicegroup_erase_urlpath = '/nextgen/deviceGroup/' + self.__dgName
        ri_devicegroup_erase_ = Restinterface(ri_devicegroup_erase_urlpath, 0, 'delete')
        d, d2 = ri_devicegroup_erase_.action_restinterface_()
        print("erase_: ", d2)
        #print("erase_: ", d)
        return d2, d
    '''

'''
Appliance_Networking___Routing_Management - Delete Static route
https://<vd-ip>:<port>/api/config/devices/device/<appliance-name>/config/routing-instances/routing-instance/<NAME-OF-THE-ROUTING-INSTANCE>/routing-options/static/route/rti-static-route-list/<DESTINATION>/<NEXT-HOP(S)-TO-DESTINATION-OR-NAME-OF-NEXT-ROUTING-INSTANCE>/<INTERFACE-TO-BE-USED-TO-REACH-NEXTHOP>


Appliance_Networking___Routing_Management - Create Static route
https://<vd-ip>:<port>/api/config/devices/device/<appliance-name>/config/routing-instances/routing-instance/<NAME-OF-THE-ROUTING-INSTANCE>/routing-options/static/route


Appliance_Networking___Routing_Management - Edit Static route
https://<vd-ip>:<port>/api/config/devices/device/<appliance-name>/config/routing-instances/routing-instance/<NAME-OF-THE-ROUTING-INSTANCE>/routing-options/static/route/rti-static-route-list/<DESTINATION>/<NEXT-HOP(S)-TO-DESTINATION-OR-NAME-OF-NEXT-ROUTING-INSTANCE>/<INTERFACE-TO-BE-USED-TO-REACH-NEXTHOP>


Appliance_Networking___Routing_Management - Get Static route
https://<vd-ip>:<port>/api/config/devices/device/<appliance-name>/config/routing-instances/routing-instance/<NAME-OF-THE-ROUTING-INSTANCE>/routing-options/static/route/rti-static-route-list
'''
