#!/usr/bin/python
#coding: UTF-8
from enum import Enum


class Vector:
    __slots__ = ( 'hostname', 'routingInstance', 'count', 'deviceName' )
    def __init__(self, *, hostname = "8.8.8.8", routingInstance = "Transport-VR", count = 4, deviceName = None):
        self.deviceName = deviceName
        self.count = count
        self.routingInstance = routingInstance
        self.hostname = hostname


@property
def default_wantable_(self):
    return self.wantable.get(self.orgName, [ "202.96.209.133", "180.101.50.188" ])
    # 202.96.199.132 202.96.199.133 202.96.209.5 202.96.209.133, "116.228.111.118"


class Wan(Vector):
    __slots__ = ( 'wantable' )
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.wantable = {

            ## "Customer-YanFeng": [ "61.169.29.218", "61.169.29.210" ],
            "Customer-Yum-China": [ "61.169.31.253" ],
            "Customer-JZY": [ "218.78.62.95" ],
            "Customer-KangHeng": [ "58.34.73.155" ],
            "Customer-HuaQiao": [ "222.71.59.122" ],
            "Customer-YG": [ "180.101.50.188" ],
            "xinshida": [ "180.101.50.188" ],
        }


@property
def default_lantables_(self):
    return self.lantables.get(self.orgName, [ "14.13.12.11" ])


class Lan(Vector):
    __slots__ = ( 'lantables' )
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.lantables = {
            "TEST": [ "192.168.1.1" ],
            # "TEST": [ "192.168.77.1", "192.168.66.1", "192.168.55.1" ],
            "Customer-YanFeng": [ "172.28.34.9", "172.28.34.1" ],
            "xinshida": [ "192.168.99.3" ],
            "Customer-PuFaJiTuan": [ "10.172.6.1" ],
            "Customer-Yum-China": [ "172.16.1.94" ],
            "Customer-YG": [ "192.168.91.10" ],
            "Customer-KangHeng": [ "192.168.0.240" ],
            "Customer-JZY": [ "172.16.202.2" ],
            "Customer-HuaQiao": [ "192.168.20.1" ],
        }


@property
def default_cpntable_(self):
    return self.cpntable.get(self.orgName, [ "172.28.32.1" ])


class Cpn(Vector):
    __slots__ = ( 'cpntable' )
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cpntable = {
            "Customer-YanFeng": [ "172.28.32.17", "172.28.32.25" ],
        }


class Group:
    __slots__ = ( 'vectors' )
    def __init__(self, vectors):
        self.vectors = vectors
