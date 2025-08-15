#!/usr/bin/python
#coding: UTF-8

from .liyuandirector_ import *

class Casejsonoauth:

    # 2021.10.21 oauth
    # 2021.9.21 sec case
    # 2020.1.21 cfue interface case
    def update_caseface_(self):
        rsp =  self.__rses.put(self.BRANCH_URL_LOCAL, verify = False, headers = self.__headers, data = self.__request )
        return rsp.text, rsp.status_code

    def fetch_caseface_(self):
        rsp =  self.__rses.get(self.BRANCH_URL_LOCAL, verify = False, headers = self.__headers )
        return rsp.text, rsp.status_code

    def create_caseface_(self):
        rsp = self.__rses.post(self.BRANCH_URL_LOCAL, verify = False, headers = self.__headers, data = self.__request )
        return rsp.text, rsp.status_code

    def __init__(self, REQUEST, RINTTYPE):

        """ @setattr(self, "action_restinterface_", action_restinterface_) """

        self.__rses	        = requests.Session()

        self.__request          = REQUEST

        self.__headers          = {'Accept': 'application/json', 'Content-Type': 'application/json',}

        self.rinttype           = RINTTYPE

        self.selector           = {
            'pos' : self.create_caseface_,
            'put' : self.update_caseface_,
        }

        self.BRANCH_URL_LOCAL   = ""

        self.auth               = ""

        self.token              = ""

