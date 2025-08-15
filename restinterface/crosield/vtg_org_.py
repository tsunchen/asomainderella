#!/usr/bin/python
#coding: UTF-8
from .vtg_device_ import *


class VTG_org:

    __slots__ = ( '__ri_orgs_orgservice_pathmetrics_urlpath_',
                  '__ri_orgs_org_sdwanslamonitor_stats_urlpath_',
                  '__ri_organization_fetchall_urlpath',
                  '__ri_organization_org_urlpath',
                  '__deviceName',
                  '__orgName'
    )

    """ 2021.5.6 VTG_org """
    '''
    2022.5.2  pathmetric
    2021.8.16 f_string
    '''
    def __init__(self, *args, **kwargs):
        self.__orgName = kwargs['deviceorg']
        self.__deviceName = kwargs['devicename']
        self.__ri_organization_org_urlpath                     = f"/vnms/sdwan/workflow/orgs/org/{self.__orgName}" # " information for organization workflow "
        self.__ri_organization_fetchall_urlpath                = f"/vnms/dashboard/tenant/{self.__orgName}/allchildren"
        self.__ri_orgs_org_sdwanslamonitor_stats_urlpath_      = f"/api/operational/devices/device/{self.__deviceName}/live-status/orgs/org/{self.__orgName}/sd-wan/sla-monitor/status"
        self.__ri_orgs_orgservice_pathmetrics_urlpath_         = f"/api/operational/devices/device/{self.__deviceName}/live-status/orgs/org-services/{self.__orgName}/sd-wan/path"


    def path_pathmetrics_remote_deep_(self, remote):
        """
        self.__ri_orgs_orgservice_pathmetrics_urlpath_ + /path-metrics?deep=true
        """
        ...


    def path_pathmetrics_deep_(self):
        """
        self.__ri_orgs_orgservice_pathmetrics_urlpath_ + /path-metrics/${remote}?deep=true
        """
        ...


    def path_pathmetric_remote_(self, remote):
        """
        /api/operational/devices/device/${device}/live-status/orgs/org-services/${tenant}/sd-wan/path/path-metrics/${remote}/path-list
        """
        ri_path_pathmetric_remote_ = f'/api/operational/devices/device/{self.__deviceName}/live-status/orgs/org-services/{self.__orgName}/sd-wan/path/path-metrics/{remote}/path-list'
        path_pathmetric_remote_, rc = Restinterface(ri_path_pathmetric_remote_, 0, 'get').action_restinterface_()
        # print("pathpathmetricremote_: ", rc)
        # print("pathpathmetricremote_: ", path_pathmetric_remote_)
        return rc, path_pathmetric_remote_


    @property
    def path_pathmetrics_(self):
        # deprecated: self.__ri_orgs_orgservice_pathmetrics_urlpath_    = f"/api/operational/devices/device/{self.__deviceName}/live-status/orgs/org-services/{self.__orgName}/sd-wan/path/path-metrics"
        # using: self.__ri_orgs_orgservice_pathmetrics_urlpath_         = f"/api/operational/devices/device/{self.__deviceName}/live-status/orgs/org-services/{self.__orgName}/sd-wan/path"
        path_pathmetrics_, rc = Restinterface(self.__ri_orgs_orgservice_pathmetrics_urlpath_, 0, 'get').action_restinterface_()
        data = json.loads(path_pathmetrics_)
        # print("pathpathmetrics: ", rc)
        # print("pathpathmetrics: ", path_pathmetrics_)
        return rc, data['path']['path-metrics']


    def sdwan_slamonitor_stats_path_(self, target):
        """
        /api/operational/devices/device/KangHeng-Taizhou-CPE-001-SD1000066066//live-status/orgs/org/Customer-KangHeng/sd-wan/sla-monitor/status/KangHeng-Shanghai-CPE-001-SD1000064072/path-status
        /api/operational/devices/device/<appliance-name>/live-status/orgs/org/<org-name>/sd-wan/sla-monitor/status/<target>/path-status
        """
        ri_orgs_org_sdwanslamonitor_stats_path_urlpath_ = f"/api/operational/devices/device/{self.__deviceName}/live-status/orgs/org/{self.__orgName}/sd-wan/sla-monitor/status/{target}/path-status"
        orgsdwanslamonitorstatspath_, rc = Restinterface(ri_orgs_org_sdwanslamonitor_stats_path_urlpath_, 0, 'get').action_restinterface_()
        print("orgsdwanslamonitorstatspath_: ", rc)
        # print("orgsdwanslamonitorstatspath_: ", d)
        return rc, orgsdwanslamonitorstatspath_


    @property
    def sdwan_slamonitor_stats_(self):
        """
        /api/operational/devices/device/KangHeng-Taizhou-CPE-001-SD1000066066/live-status/orgs/org/Customer-KangHeng/sd-wan/sla-monitor/status
        /api/operational/devices/device/<appliance-name>/live-status/orgs/org/<org-name>/sd-wan/sla-monitor/status
        """
        orgsdwanslamonitorstats_, rc = Restinterface(self.__ri_orgs_org_sdwanslamonitor_stats_urlpath_, 0, 'get').action_restinterface_()
        print("orgsdwanslamonitorstats_: ", rc)
        # print("orgsdwanslamonitorstats_: ", d)
        return rc, orgsdwanslamonitorstats_


    @property
    def tenantallchildren_(self):
        """ TENANT """
        _uPASS = (os.getenv("VUADM"), os.getenv("VUPAS"))
        print("Prajan-Paramita-Sutra".center(64))
        # print("la vie & l'amour, the winner is".center(64))
        tenantallchildren_, rc = Infresta(self.__ri_organization_fetchall_urlpath, 0, 'get', _uPASS).action_restinterface_()
        print("tenantallchildren_: ", rc)
        # print("tenantallchildren_: ", d)
        return rc, tenantallchildren_


    def tenantallchildren(self, token):
        """ TENANT by Token """
        tenantallchildren, rc = Infresta(self.__ri_organization_fetchall_urlpath, 0, 'tok', token).action_restif_oauth_(token)
        print("tenantallchildren: ", rc)
        print("tenantallchildren: ", tenantallchildren)
        return rc, tenantallchildren


    @property
    def org_(self):
        """ ORG """ # "versanms.sdwan-org-workflow"
        org_, rc = Restinterface(self.__ri_organization_org_urlpath, 0, 'get').action_restinterface_()
        print("orginfo_: ", rc)
        # print("orginfo_: ", d)
        return rc, org_


    @property
    def org_Id_(self):
        """ ORG """ # "versanms.sdwan-org-workflow" ""globalId""
        _, org_ = self.org_
        data = json.loads(org_)
        # print(data["versanms.sdwan-org-workflow"])
        # print(data["versanms.sdwan-org-workflow"]["globalId"])
        return data["versanms.sdwan-org-workflow"]["globalId"]