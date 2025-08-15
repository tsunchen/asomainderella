#!/usr/bin/python
#coding: UTF-8
from .cfue_shct_ import *


@property
def default_pseudosg_(self):
    return self.pseudosg.get(self.orgName, [ "controller01", "controller02" ])


class VTG_spokegroup:

    """
    2024.2.1 pseudosg
    2021.5.15 - 18 hub spoke spokegroup hub priority
    2021.5.17 orgspokegroups_
    2020.10.30 found orgspokegroup not complete spoke
    2020.10 dev template spoke spokegroup hub priority
    """

    __slots__ = ( "pseudosg", "__orgSpokeGroups", "__devspokegroupshub_priority", "__devspokegroup_infos_hubs", "__devspokegroup_infos",
                  "__hubspokegroupdev_priority", "__hubspokegroup_info_hubs", "__hubspokegroup_info", "__hubSpokeGroup",
                  "__devspokegrouphub_priority", "__devspokegrouphub_prime", "__devspokegroup_info_hubs", "__devspokegroup_info",
                  "__devSpokeGroup", "__orgSpokeGroup", "orgName" )

    def __init__(self, *args, **kwargs):
        self.orgName = kwargs['deviceorg']
        self.__orgSpokeGroup = []
        self.__devSpokeGroup = ""
        self.__devspokegroup_info = {}
        self.__devspokegroup_info_hubs = []
        self.__devspokegrouphub_prime = []
        self.__devspokegrouphub_priority = [] # dev -> hub
        #
        self.__hubSpokeGroup = ""
        self.__hubspokegroup_info = {}
        self.__hubspokegroup_info_hubs = []
        self.__hubspokegroupdev_priority = [] # hub -> dev
        #
        self.__devspokegroup_infos = [] # infos = n * info
        self.__devspokegroup_infos_hubs = [] # infos_hubs = n * infos
        self.__devspokegroupshub_priority = [] # hub -> hub
        self.__orgSpokeGroups = []
        #
        self.pseudosg = {
            "Customer-HuaQiao" : [ "Customer-HuaQiao-CPE-ShangHai-001-SD1000068013" ],
            "Customer-KangHeng" : [ "KangHeng-ShangHai-CPE-001" ], # 2024.4.2
            # "Customer-KangHeng" : [ "KangHeng-Shanghai-CPE-001-SD1000064072" ],
            "Customer-YG" : [ "YG-SH-CPE-001" ],
        }


    """
    hub spoke spokegroup hub priority  2021.5.15 - 18
    """
    def devspokegroups_hub_hub_(self, hub):
        """
        item['Name']
        item['Priority']
        item['Hub']
        """
        for item in self.__devspokegroup_infos_hubs:
            if (1 == item['Priority'] and hub == item['Name']):
                self.__devspokegroupshub_priority.append(item['Hub'])
                # self.__devspokegroupshub_priority.append(item['Hub'] + ',' + item['Name'])
        return self.__devspokegroupshub_priority


    def devspokegroups_hubs_priority_(self):
        self.__devspokegroup_infos_hubs = [ { "Name": itemHub["name"], "Priority": itemHub["priority"], "Hub": devspokegroup_info['name'] } for devspokegroup_info in self.__devspokegroup_infos for itemVrf in devspokegroup_info["vrfs"] for itemHub in itemVrf["hubs"] ]
        return self


    def devspokegroups_(self):
        for spoke in self.__orgSpokeGroups:
            _, data = self.devspokegroup_(spoke)
            self.__devspokegroup_infos.append(data)
        return self


    def orgspokegroups_(self):
        """ ?org= 2021.5.17 """
        ri_spokegroup_fetchall_urlpath = '/nextgen/spokegroup/' + '?org=' + self.orgName
        ri_spokegroup_fetchall_ = Restinterface(ri_spokegroup_fetchall_urlpath, 0, 'get')
        d, rc = ri_spokegroup_fetchall_.action_restinterface_()
        data = json.loads(d)
        print("orgspokegroups_: ", rc)
        # print("orgspokegroups_: ", d)
        self.__orgSpokeGroups = [ item['name'] for item in data if item['org'] == self.orgName ]
        return self


    """
    dev template spoke spokegroup hub priority  2020.10
    """
    def devspokegroup_hub_priority_(self):
        devspokegrouphubs = self.devspokegroup_hubs_priority_()
        # print(devspokegrouphubs)
        for item in devspokegrouphubs:
            # print(item['Priority'])
            # print(item['Name'])
            # 2020.10.26 Priority = First
            if (1 == item['Priority']):
                self.__devspokegrouphub_priority.append(item['Name'])
        return self.__devspokegrouphub_priority


    def devspokegroup_hub_prime_(self):
        devspokegrouphubs = self.devspokegroup_hubs_()
        self.__devspokegrouphub_prime.append(devspokegrouphubs[0])
        return self.__devspokegrouphub_prime


    def devspokegroup_hubs_priority_(self):
        data = self.__devspokegroup_info
        # print(f"devspokegroup_hubs_priority_: {data}")
        if (data is not None):
            data.pop('createDate')
            data.pop('modifyDate')
            data.pop('lastUpdatedBy')
            data.pop('status')
            # 2020.10.29 Add the Hub
            self.__devspokegroup_info_hubs = [ {"Name": item["name"], "Priority": item["priority"], "Hub": data["name"]} for item in data["vrfs"] for item in item["hubs"] ]
            # print(self.__devspokegroup_info_hubs)
        return self.__devspokegroup_info_hubs


    def devspokegroup_hubs_(self):
        data = self.__devspokegroup_info
        # print(f"devspokegroup_hubs_: {data}")
        if (data is not None):
            data.pop('createDate')
            data.pop('modifyDate')
            data.pop('lastUpdatedBy')
            data.pop('status')
            self.__devspokegroup_info_hubs = [ item["name"] for item in data["vrfs"] for item in item["hubs"] ]
        return self.__devspokegroup_info_hubs


    def devspokegroupi_(self, spoke):
        self.__devSpokeGroup = spoke
        ri_spokegroup_fetch_urlpath = '/nextgen/spokegroup/' + self.__devSpokeGroup
        ri_spokegroup_fetch_ = Restinterface(ri_spokegroup_fetch_urlpath, 0, 'get')
        d, rc = ri_spokegroup_fetch_.action_restinterface_()
        data = json.loads(d)
        # print(json.dumps(data, indent = 4))
        self.__devspokegroup_info = data
        return rc, data


    def devspokegroup_(self, spoke):
        self.__devSpokeGroup = spoke
        # 2020.11.30
        if (self.__devSpokeGroup is None):
            print("Spoke Unavailable")
            self.__devspokegroup_info = None
            return None, None
        else:
            ri_spokegroup_fetch_urlpath = '/nextgen/spokegroup/' + self.__devSpokeGroup
            ri_spokegroup_fetch_ = Restinterface(ri_spokegroup_fetch_urlpath, 0, 'get')
            d, rc = ri_spokegroup_fetch_.action_restinterface_()
            data = json.loads(d)
            # print(json.dumps(data, indent = 4))
            self.__devspokegroup_info = data
            return rc, data


    def orgspokegroup_hubs_(self):
        for item in self.__orgSpokeGroup:
            # print(item)
            ri_spokegrouphubs_fetchall_urlpath = '/nextgen/spokegroup/' + item
            ri_spokegrouphubs_fetchall_ = Restinterface(ri_spokegrouphubs_fetchall_urlpath, 0, 'get')
            d, rc = ri_spokegrouphubs_fetchall_.action_restinterface_()
            data = json.loads(d)
            data.pop('createDate')
            data.pop('modifyDate')
            data.pop('lastUpdatedBy')
            data.pop('status')
            # print("orgspokegrouphubs_: ", rc)
            # print("orgspokegrouphubs_: ", data['vrfs']['hubs'])
            # print(json.dumps(data, indent = 4))


    def orgspokegroup_(self):
        # 2020.10.30 found orgspokegroup not complete spoke
        #/api/config/nms/sdwan/workflows/workflow/spoke-group
        #/nextgen/spokegroup/
        ri_spokegroup_fetchall_urlpath = '/nextgen/spokegroup/'
        ri_spokegroup_fetchall_ = Restinterface(ri_spokegroup_fetchall_urlpath, 0, 'get')
        d, rc = ri_spokegroup_fetchall_.action_restinterface_()
        data = json.loads(d)
        print("orgspokegroup_: ", rc)
        # print("orgspokegroup_: ", d)
        self.__orgSpokeGroup = [ item['name'] for item in data if item['org'] == self.orgName ]
        # print(self.__orgSpokeGroup)
        # return rn, self.__orgSpokeGroup