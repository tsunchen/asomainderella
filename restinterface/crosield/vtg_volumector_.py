#!/usr/bin/python
#coding: UTF-8

# 2024.12.10 vmcpseudospoke
# 2024.8.22 volumectorclazz, vmclan, vmcgspoke, vmcwan
# 2024.7.16 Cloud Private Network
# 2024.7.15 volumector folder
# 2024.7.9 Volume Vector

from .volumector.extension import extension
from .volumector.volumectorclazz import Volumector
from .volumector.vmclan import LAN
from .volumector.vmcgspoke import GSPOKE
from .volumector.vmcwan import WAN
from .volumector.vmcpseudospoke import PseudoSpoke


@extension(Volumector)
def CPN(self, *args, **kwargs):
    self.table = {

            "Customer-YanFeng": [ "172.28.32.25", "172.28.32.17" ],

        }

    self.volume = kwargs.get('volume', 'CPN')
    self.super_to_string = self.to_string

    def to_string():
        print(self.super_to_string())
        return f"This is {self.volume} {self.table}."

    def default_vector(orgName):
        return self.table.get(orgName, [ "172.28.1.1", "172.28.32.1" ])

    self.to_string = to_string
    self.default_vector = default_vector

    return self


'''
IPVectorWan = WAN(volume = "SD-WAN")
print(IPVectorWan.to_string())
print(IPVectorWan.default_wan_table('Customer-Yum-China'))

IPVectorLan = LAN(volume = "SD-LAN")
print(IPVectorLan.to_string())
print(IPVectorLan.default_lan_table('Customer-YanFeng'))
print(IPVectorLan.default_lan_table('Tenant'))
'''