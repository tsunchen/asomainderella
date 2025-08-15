#!/usr/bin/python
#coding: UTF-8
from .vtg_device_ import *
from .asyncinventories.async_iterator_ import AsyncIteratorWrapper

@property
def default_lan_tables_(self):
    return self.lantables.get(self.orgName, [ "14.13.12.11" ])


@property
def default_wan_table_(self):
    return self.wantable.get(self.orgName, [ "202.96.209.133", "180.101.50.188" ])
    # 202.96.199.132 202.96.199.133 202.96.209.5 202.96.209.133, "116.228.111.118"


@property
def default_cpn_table_(self):
    return self.cpntable.get(self.orgName, [ "172.28.32.1" ])


class VTG_interface:

    __slots__ = ( 'cpntable', 'lantables', 'wantable', '__ri_interface_vni_objects_arpentry_urlpath', '__ri_interface_vni_objects_unit_urlpath', '__deviceName', 'orgName' )

    """
    2024.3.4    fusable
    2023.5.4    orgintfcloudnet_
    2023.4.24  orgintfcloudnet
    2023.3.30  orgintfnocloudnet
    2023.2.28  orgintfinside network update
    2023.2.21  orgintfinside update
    2022.12.28 orgintfinside
    2022.9.1   orgintfnompls_
    2022.8.10  wantable, orgName instance
    2022.7.27  __wantable upgrade
    2022.7.12  enter, exit
    2021.10.22 deviceUuid
    2021.9.29  exception
    2021.9.28  jmp.urlinconnecting_
    2021.8.16  f_string
    """
    def __init__(self, *args, **kwargs):
        self.orgName = kwargs['deviceorg']
        self.__deviceName = kwargs['devicename']
        self.__ri_interface_vni_objects_unit_urlpath = f"/api/operational/devices/device/{self.__deviceName}/live-status/interfaces/info/{self.orgName}/org_intf"
        self.__ri_interface_vni_objects_arpentry_urlpath = f"/vnms/dashboard/appliance/{self.__deviceName}/live?command=arp/interface"

        self.cpntable = {

            ## "Customer-YanFeng": [ "172.28.32.17", "172.28.32.25" ],
            "Customer-YanFeng": [ "172.28.32.25" ],
        }

        self.wantable = {

            "Customer-PuFaJiTuan": [ "61.151.158.122" ], # ["58.34.42.194" , "58.34.42.196"]
            ## "Customer-YanFeng": [ "61.169.29.218", "61.169.29.210" ],
            "Customer-Yum-China": [ "61.169.31.253" ],
            "Customer-JZY": [ "218.78.62.95" ],
            "Customer-KangHeng": [ "140.206.185.50" ], # CU
            ## "Customer-KangHeng": [ "58.34.73.155" ], # CT
            "Customer-HuaQiao": [ "222.71.59.122" ],
            "Customer-YG": [ "180.101.50.188" ],
            "xinshida": [ "180.101.50.188" ],
        }

        self.lantables = {

            "TEST": [ "192.168.1.1" ],
            # "TEST": [ "192.168.77.1", "192.168.66.1", "192.168.55.1" ],
            "Customer-YanFeng": [ "172.28.34.9", "172.28.34.1" ],
            "xinshida": [ "192.168.99.3" ],
            "Customer-PuFaJiTuan": [ "10.172.6.1" ],
            "Customer-Yum-China": [ "172.16.1.94"],
            # "Customer-Yum-China":  [ "172.31.200.5" ],
            "Customer-YG": [ "192.168.91.10" ],
            "Customer-KangHeng": [ "192.168.0.240" ],
            "Customer-JZY": [ "172.16.202.2" ],
            "Customer-HuaQiao": [ "192.168.20.1" ],
        }


    def __enter__(self):
        # return self
        """
        unit of the interface object 
        """
        rc, uio = self.unit_
        if (200 == rc):
            return uio, self
        else:
            # Unreachablility of UIO
            return "...U...", self


    def __exit__(self, type, value, trace):
        ...


    def keydefval_(self, root, key, value):
        if ( None == root.get(key, None)):
            root.setdefault(key, value)
            print("To associate ( " + key + " <- " + value + " )")
        return root[key]


    def detailStatisticsAlarms_IpsecTunnel_(self, devUuid):
        """ _statistics_objects_alarms_urlpath """
        # ipsec-tunnel-down
        # "/versa/ncs-services/vnms/dashboard/appliance/{self.__deviceName}/live?uuid={devUuid}&command=alarms/statistics/detail/ipsec-tunnel-down"
        desals_, rc = Restinterface(f"/vnms/dashboard/appliance/{self.__deviceName}/live?uuid={devUuid}&command=alarms/statistics/detail/ipsec-tunnel-down", 0, 'get').action_restinterface_()
        # print("desals_: ", rc)
        # print("desals_", desals_)
        return rc, desals_


    def detailStatisticsAlarms_Interface_(self, devUuid):
        # "/versa/ncs-services/vnms/dashboard/appliance/{self.__deviceName}/live?uuid={devUuid}&command=alarms/statistics/detail/interface-down"
        desals_, rc = Restinterface(f"/vnms/dashboard/appliance/{self.__deviceName}/live?uuid={devUuid}&command=alarms/statistics/detail/interface-down", 0, 'get').action_restinterface_()
        # print("desals_: ", rc)
        # print("desals_", desals_)
        return rc, desals_


    def detailStatisticsAlarms_(self, devUuid):
        # "/versa/ncs-services/vnms/dashboard/appliance/{self.__deviceName}/live?uuid={devUuid}&command=alarms/statistics/detail"
        desals_, rc = Restinterface(f"/vnms/dashboard/appliance/{self.__deviceName}/live?uuid={devUuid}&command=alarms/statistics/detail", 0, 'get').action_restinterface_()
        # print("desals_: ", rc)
        # print("desals_", desals_)
        return rc, desals_


    def briefStatisticsAlarms_(self, devUuid):
        # "/versa/ncs-services/vnms/dashboard/appliance/{self.__deviceName}/live?uuid={devUuid}&command=alarms/statistics/brief"
        brsals_, rc = Restinterface(f"/vnms/dashboard/appliance/{self.__deviceName}/live?uuid={devUuid}&command=alarms/statistics/brief", 0, 'get').action_restinterface_()
        # print("brsals_: ", rc)
        # print("brsals_", brsals_)
        return rc, brsals_


    # self.__ri_interface_vni_objects_management_urlpath
    # /versa/vnms/console/?target=wu2oozerc7h/10.0.0.8&key=wu2oozerc7h&mode=shell
    # https-conf-t
    @property
    def management_(self): # Mgmt_Address
        try:
            jmp = Restinterface(None, 0, 'get')
            jmp.action_restinterface_()
            from .vtg_org_ import VTG_org
            gId = VTG_org(devicename = self.__deviceName, deviceorg = self.orgName).org_Id_
            eId = str(int(gId) * 2 + 1)
            __management_mgmtAddr_ = f"/api/operational/devices/device/{self.__deviceName}/live-status/interfaces/ip/detail/\"tvi-0/{eId}.0\"/ipv4"
            mgmtAddr_, rc = Restinterface(__management_mgmtAddr_, 0, 'get').action_restinterface_()
            data = json.loads(mgmtAddr_)
            mgmtAddr_ = data['ipv4'][0].split("/")[0]
        except KeyError as e:
            print(f"- Fail to connect, this {self.__deviceName} could not be reachable ! ")
        else:
            __management_httpsconft = f"{jmp.urlinconnecting_}/versa/vnms/console/?target={self.__deviceName}/{mgmtAddr_}&mode=shell"
            # print(__management_httpsconft)
            import webbrowser as web
            chromepath = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
            web.register('chrome', None, web.BackgroundBrowser(chromepath))
            web.get('chrome').open_new_tab(__management_httpsconft)
        finally:
            return rc, mgmtAddr_


    def carrier_(self, devUuid):
        # "/versa/ncs-services/vnms/dashboard/appliance/{self.__deviceName}/live?uuid={devUuid}&command=interfaces/wwan/status/carrier-brief?deep"
        __ri_interface_vni_objects_carrier_urlpath = f"/vnms/dashboard/appliance/{self.__deviceName}/live?uuid={devUuid}&command=interfaces/wwan/status/carrier-brief?deep"
        carrier_, rc = Restinterface(__ri_interface_vni_objects_carrier_urlpath, 0, 'get').action_restinterface_()
        # print("interfacecarrier_: ", rc)
        # print("interfacecarrier_", carrier_)
        return rc, carrier_


    @property
    def entry_(self):
        entry_, rc = Restinterface(self.__ri_interface_vni_objects_arpentry_urlpath, 0, 'get').action_restinterface_()
        # print("interfaceentry_: ", rc)
        # print("interfaceentry_", entry_)
        return rc, entry_


    @property
    def unit_(self):
        unit_, rc = Restinterface(self.__ri_interface_vni_objects_unit_urlpath, 0, 'get').action_restinterface_()
        # print("interfaceunit_: ", rc)
        # print("interfaceunit_", unit_)
        return rc, json.loads(unit_)


    '''
    async def uNit_wan_ver21_1_(self):
        #/api/operational/devices/device/<appliance-name>/live-status/interfaces/info
        ri_interface_vni_objects_unit_urlpath = '/api/operational/devices/device/' + self.__deviceName + '/live-status/interfaces/info/' + self.__orgName + '/org_intf/'
        ri_interface_vni_objects_unit_ = Restinterface(ri_interface_vni_objects_unit_urlpath, 0, 'get')
        uNit_, rc = await ri_interface_vni_objects_unit_.action_restinterface_()
        #print(uNit_['org_intf'])
        if uNit_ != None:
            uNit_wan_ = [ butt async for butt in AsyncIteratorWrapper(uNit_['org_intf']) if ("wan" == butt['type'] and "MPLS" not in butt['vrf'].upper()) ]
        else:
            uNit_wan_ = []
        #print("interfaceunit_wan_: ", rc)
        #print("interfaceunit_wan_", uNit_)
        return rc, uNit_wan_

    async def orgIntfnocloudnet_(self, data):
        # [ butt async for butt in AsyncIteratorWrapper(uNit_['org_intf']) if ("wan" == butt['type'] and "MPLS" not in butt['vrf'].upper()) ]
        ## return [ butt async for butt in AsyncIteratorWrapper(data['org_intf']) if "wan" == butt['type'] and "CPN" not in butt['vrf'].upper() and "MPLS" not in butt['vrf'] ]
        ## return [ butt for butt in data['org_intf'] if "wan" == butt['type'] and "CPN" not in butt['vrf'].upper() and "MPLS" not in butt['vrf'] ]
    '''

    def orgintfnocloudnet_(self, data):
        return [ butt for butt in data['org_intf'] if "wan" == butt['type'] and "CPN" not in butt['vrf'].upper() and "MPLS" not in butt['vrf'] ]


    def orgintfinside_(self, data):
        return [ butt for butt in data['org_intf'] if "lan" == butt['type'] and "FAILOVER" not in butt['network'].upper() ]
        # return [ butt for butt in data['org_intf'] if "lan" == butt['type'] and "FAILOVER" not in butt['network'].upper() and "LAN-VR-WAN" not in butt['network'].upper() ] # and "LAN2" not in butt['network'].upper() ]


    def orgintfcloudnet_(self, data):
        # return [ butt for butt in data['org_intf'] if "wan" == butt['type'] and "CPN" in butt['vrf'].upper() ]
        # '''
        for butt in data['org_intf']:
            butt.setdefault('network', "CPN")
            if butt.get('network') is not None:
                # print(butt['name'])
                break
        else:
            print(" - Key network error - ")
            return []
        return [ butt for butt in data['org_intf'] if "wan" == butt['type'] and "CPN" in butt['network'].upper() ]
        # '''