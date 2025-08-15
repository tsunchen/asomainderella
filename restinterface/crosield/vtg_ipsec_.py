#!/usr/bin/python
#coding: UTF-8
from .vtg_device_ import *


class VTG_ipsec:
    """
    2021.4.29
    """
    def __init__(self, *args, **kwargs):
        self.__orgName = kwargs['deviceorg']
        self.__deviceName = kwargs['devicename']
        self.__wantable = {}
        # self.__vpnpname = kwargs['vpnpname'] # IPSEC-VPN-PROFILE-NAME


    def vpn_stats_(self):
        """
        # /api/operational/devices/device/<appliance-name>/live-status/orgs/org-services/<ORG-NAME>/ipsec/statistics/ipsec-stats
        """
        ri_ipsec_objects_stats_urlpath_ = '/api/operational/devices/device/' + self.__deviceName + '/live-status/orgs/org-services/' + self.__orgName + '/ipsec/statistics/ipsec-stats'
        ri_ipsec_objects_stats_ = Restinterface(ri_ipsec_objects_stats_urlpath_, 0, 'get')
        d, rc = ri_ipsec_objects_stats_.action_restinterface_()
        print("ipsecstats_: ", rc)
        print("ipsecstats_", d)
        return rc, d


    def vpn_securityassociations_(self):
        """
        # /api/operational/devices/device/<appliance-name>/live-status/orgs/org-services/<ORG-NAME>/ipsec/vpn-profile/<IPSEC-VPN-PROFILE-NAME>/vpn-show/ike/security-associations
        """
        ...


    def vpn_profile_(self):
        """
        # /api/operational/devices/device/<appliance-name>/live-status/orgs/org-services/<ORG-NAME>/ipsec/vpn-profile
        """
        ri_ipsec_objects_profile_urlpath = '/api/operational/devices/device/' + self.__deviceName + '/live-status/orgs/org-services/' + self.__orgName + '/ipsec/vpn-profile'
        ri_ipsec_objects_profile_ = Restinterface(ri_ipsec_objects_profile_urlpath_, 0, 'get')
        d, rc = ri_ipsec_objects_profile_.action_restinterface_()
        print("ipsecprofile_: ", rc)
        print("ipsecprofile_", d)
        return rc, d


    def vpn_history_(self): # /api/operational/devices/device/KangHeng-Shanghai-CPE-001-SD1000064072/live-status/orgs/org-services/Customer-KangHeng/ipsec/vpn-profile/controller01-Profile/vpn-show/ike/history
        """
        # /api/operational/devices/device/<appliance-name>/live-status/orgs/org-services/<ORG-NAME>/ipsec/vpn-profile/<IPSEC-VPN-PROFILE-NAME>/vpn-show/ike/history
        """
        ri_ipsec_objects_history_urlpath_ = '/api/operational/devices/device/' + self.__deviceName + '/live-status/orgs/org-services/' + self.__orgName + '/ipsec/vpn-profile/' + self.__vpnpname + '/vpn-show/ike/history'
        ri_ipsec_objects_history_ = Restinterface(ri_ipsec_objects_history_urlpath_, 0, 'get')
        d, rc = ri_ipsec_objects_history_.action_restinterface_()
        print("ipsechistory_: ", rc)
        print("ipsechistory_", d)
        return rc, d