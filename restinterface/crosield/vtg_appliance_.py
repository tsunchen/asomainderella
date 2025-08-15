#!/usr/bin/python
#coding: UTF-8
import threading, time
from .vtg_device_ import *
import collections
from graphene import ( 
    ObjectType, 
    String, 
    Schema, 
    JSONString, 
    NonNull, 
    List, 
    Int
)
# from functools import cache
# from functools import cached_property


class VirtualSilicon(ObjectType):
    applianceName = String()
    applianceUuid = String()
    locationId = String()
    latitude = String()
    longitude = String()
    type = String()

class VTG_appliance:
    __slots__ = ( "location", "__ri_appliance_location_urlpath_", "__orgName" )

    """
    2023.3.2   len
    2022.6.17  Exception
    2021.11.26 inner Query , receiverSchema
    2021.11.25 meta
    2021.8.15  f_string
    """
    def __init__(self, **kwargs):
        self.__orgName = kwargs.get('deviceorg')
        self.__ri_appliance_location_urlpath_ = f"/vnms/dashboard/applianceLocation/{self.__orgName}"        
        _, self.location = self.location_


    @property
    def receiverSchema_(self):
        receiver = self
        class Query(ObjectType):
            """
            fetch
            id count 
            """
            fetch = List(VirtualSilicon, id = String(), description = "Detail Fetcher")
            def resolve_fetch(root, info, **kwargs):
                meta_ = list(json.loads(receiver.location).get("List").get('value'))
                response = Conversion(binding = ['applianceName', 'applianceUuid', 'locationId', 'latitude', 'longitude', 'type']).cov(meta_)
                resp = list(response.values())
                return resp
        # schema
        schema = Schema(query = Query)
        return schema


    @property
    def longitudes_(self):
        try:
            longitudes_ = [ list(meta.values()) for meta in self.receiverSchema_.execute('{ fetch(id: "id") { longitude } }').data['fetch'] ]
        except (TypeError, UnboundLocalError) as e:
            print(f" - Please wait unitl branch appliance and uuid created successfully. {e}")
        else:
            return longitudes_


    @property
    def latitudes_(self):
        try:
            latitudes_ = [ list(meta.values()) for meta in self.receiverSchema_.execute('{ fetch(id: "id") { latitude } }').data['fetch'] ]
        except (TypeError, UnboundLocalError) as e:
            print(f" - Please wait unitl branch appliance and uuid created successfully. {e}")
        else:
            return latitudes_


    @property
    def locationids_(self):
        try:
            locationids_ = [ list(meta.values()) for meta in self.receiverSchema_.execute('{ fetch(id: "id") { locationId } }').data['fetch'] ]
        except (TypeError, UnboundLocalError) as e:
            print(f" - Please wait unitl branch appliance and uuid created successfully. {e}")
        else:
            return locationids_


    @property
    def uuids_(self):
        try:
            uuids_ = [ list(meta.values()) for meta in self.receiverSchema_.execute('{ fetch(id: "id") { applianceUuid } }').data['fetch'] ]
        except (TypeError, UnboundLocalError) as e:
            print(f" - Please wait unitl branch appliance and uuid created successfully. {e}")
        else:
            print(f" ({uuids_.__len__()}) @ Data families of {self.__orgName} are loading onto the SF-Viewer.  ")
            return uuids_


    @property
    def names_(self):
        try:
            names = [ list(meta.values()) for meta in self.receiverSchema_.execute('{ fetch(id: "id") { applianceName } }').data['fetch'] ]
        except (TypeError, UnboundLocalError) as e:
            print(f" - Please wait unitl branch appliance and uuid created successfully. {e}")
        else:
            return names


    @property
    def types_(self):
        try:
            types_ = [ list(meta.values()) for meta in self.receiverSchema_.execute('{ fetch(id: "id") { type } }').data['fetch'] ]
        except (TypeError, UnboundLocalError) as e:
            print(f" - Please wait unitl branch appliance and uuid created successfully. {e}")
        else:
            return types_


    def status_(self, applianceStatus):
        applianceStatus, rc = Restinterface(f"/vnms/dashboard/applianceStatus/{applianceStatus}/brief", 0, 'get').action_restinterface_()
        # print("applianceStatus_: ", rc)
        # print("applianceStatus_: ", d)
        return rc, applianceStatus


    def renewal_(self, dSN, rSN):
        # /vnms/assets/asset/{destinationSerialNo}/replace/{renewalSerialNo}
        # print(f'/vnms/assets/asset/{[dSN]}/replace/{[rSN]}')
        applianceRenewal, rc = Restinterface(f"/vnms/assets/asset/{dSN}/replace/{rSN}", 0, 'put').action_restinterface_()
        print("applianceRenewal_: ", rc)
        # print("applianceRenewal_: ", applianceRenewal)
        return rc, applianceRenewal


    def hardware_(self, fetchdeviceuuidByitem_brief):
        # /vnms/dashboard/appliance/{applianceUuid}
        # /vnms/dashboard/applianceByUuid/{applianceUuid}
        applianceHardware, rc = Restinterface(f"/vnms/dashboard/appliance/{fetchdeviceuuidByitem_brief}/hardware", 0, 'get').action_restinterface_()
        # print("applianceHardware_: ", rc)
        # print("applianceHardware_: ", applianceHardware)
        return rc, applianceHardware


    @property
    def location_(self):
        location_, rc = Restinterface(self.__ri_appliance_location_urlpath_, 0, 'get').action_restinterface_()
        # print("applianceLocation_: ", rc)
        # print("applianceLocation_", d)
        return rc, location_


class Conversion:
    """Json data to GraphQL data"""
    def __init__(self, *args, **kwargs):
        self.__bond = kwargs['binding']

    def cov(self, data):
        """
        data: json
        """
        Conversioner = collections.namedtuple("Conversioner", self.__bond)
        outdict = {}
        for dt in data:
            resp = collections.OrderedDict()
            for tp in self.__bond:
                resp[tp] = dt[tp]
            outdict[data.index(dt)] = Conversioner(*resp.values())
        return outdict