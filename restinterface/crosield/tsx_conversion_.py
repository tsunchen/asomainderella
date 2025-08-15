#!/usr/bin/python
#coding: UTF-8

class Conversion():
    """Json data to GraphQL data"""
    def __init__(self):
        self.bond = ['applianceName', 'applianceUuid', 'locationId', 'latitude', 'longitude', 'type']

    def cov(self, data):
        """
        data: json
        """
        Conversioner = collections.namedtuple("Conversioner", self.bond)
        outdict = {}
        for dt in data:
            resp = collections.OrderedDict()
            for tp in self.bond:
                resp[tp] = dt[tp]
            outdict[data.index(dt)] = Conversioner(*resp.values())
        return outdict
