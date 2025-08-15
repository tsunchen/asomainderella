#!/usr/bin/python
#coding: UTF-8
from .liyuandirector_ import *

class Casejsonsec:
    """
    2021.9.21 sec case
    2020.1.21 cfue interface case
    """
    def caselection(self, caseface):
        return getattr(self, caseface)()

    def put(self):
        rsp = self.__rsess.put( self.BRANCH_URL_LOCAL, auth = self.auth, verify = False, headers = self.__headers, data = self.__request )
        return rsp.text, rsp.status_code

    def get(self):
        rsp = self.__rsess.get( self.BRANCH_URL_LOCAL, auth = self.auth, verify = False, headers = self.__headers )
        return rsp.text, rsp.status_code

    def pos(self):
        rsp = self.__rsess.post( self.BRANCH_URL_LOCAL, auth = self.auth, verify = False, headers = self.__headers, data = self.__request )
        return rsp.text, rsp.status_code

    __slots__ = ( '__rsess', '__request', '__headers', 'rinttype', 'BRANCH_URL_LOCAL', 'auth', )

    def __init__(self, REQUEST, RINTTYPE):

        """ @setattr(self, "action_restinterface_", action_restinterface_) """

        self.__rsess	        = requests.Session()

        self.__request          = REQUEST

        self.__headers          = {'Accept': 'application/json', 'Content-Type': 'application/json',}

        self.rinttype           = RINTTYPE

        self.BRANCH_URL_LOCAL   = ""

        self.auth               = ""