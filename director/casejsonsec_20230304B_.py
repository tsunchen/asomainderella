#!/usr/bin/python
#coding: UTF-8
from .liyuandirector_ import *
from .jumendirector_ import *

class Casejsonsec:
    """
    2021.9.21 sec case
    2020.1.21 cfue interface case
    """
    def caselection(self, caseface):
        return getattr(self, caseface)()

    def get(self):
        with self.__rsess as rs:
            rsp = rs.get( self.BRANCH_URL_LOCAL, auth = self.auth, verify = False, headers = self.__headers )
            # print(rsp.json())
            return rsp.text, rsp.status_code

    def got(self):
        with self.__rsess as rs:
            rsp = rs.get( self.BRANCH_URL_LOCAL, auth = self.auth, verify = False, headers = self.__headers )
            return rsp.text, rsp.request.url

    def pos(self):
        with self.__rsess as rs:
            rsp = rs.post( self.BRANCH_URL_LOCAL, auth = self.auth, verify = False, headers = self.__headers, data = self.__request )
            return rsp.text, rsp.status_code

    def put(self):
        with self.__rsess as rs:
            rsp = rs.put( self.BRANCH_URL_LOCAL, auth = self.auth, verify = False, headers = self.__headers, data = self.__request )
            return rsp.text, rsp.status_code

    def fet(self):
        # fetch token
        with self.__rsess as rs:
            rsp = rs.post( self.BRANCH_URL_LOCAL, auth = self.auth, verify = False, headers = self.__headers, data = self.__request )
            return rsp.text, rsp.status_code

    def tok(self):
        # by token
        with self.__rsess as rs:
            headersToken = {'Accept': 'application/json', 'Content-Type': 'application/json',}
            headersToken['Authorization'] = ''.join([ 'Bearer ', self.auth])
            print(headersToken)
            print(self.BRANCH_URL_LOCAL, self.__request)
            rsp = rs.get( self.BRANCH_URL_LOCAL, verify = False, headers = headersToken, data = self.__request )
            return rsp.text, rsp.status_code

    __slots__ = ( '__rsess', '__request', '__headers', 'rinttype', 'BRANCH_URL_LOCAL', 'auth' )

    def __init__(self, REQUEST, RINTTYPE):

        """ @setattr(self, "action_restinterface_", action_restinterface_) """

        self.__rsess	        = requests.Session()

        self.__request          = REQUEST

        self.__headers          = {'Accept': 'application/json', 'Content-Type': 'application/json',}

        self.rinttype           = RINTTYPE

        self.BRANCH_URL_LOCAL   = ""

        self.auth               = ""