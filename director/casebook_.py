#!/usr/bin/python
#coding: UTF-8

from .liyuandirector_ import *

class Casebook:

    def __init__(self, REQUEST, RINTTYPE):
        """ @setattr(self, "action_restinterface_", action_restinterface_) """

        self.__request          = REQUEST
        self.__headers          = {'Accept': 'application/json', 'Content-Type': 'application/json',}

        self.rinttype = RINTTYPE
        self.selector = {
            'delete': self.erase_caseface_,
            'post'  : self.create_caseface_,
            'put'   : self.update_caseface_,
        }
        self.BRANCH_URL_LOCAL = ""
        self.auth             = ""

        self.__rS = requests.Session()

    # 2021.1.1 cfue interface case
    def erase_caseface_(self):
        rsp =  self.__rS.delete(self.BRANCH_URL_LOCAL, auth = self.auth, verify = False, headers = self.__headers )
        return rsp.text, rsp.status_code

    def update_caseface_(self):
        rsp =  self.__rS.put(self.BRANCH_URL_LOCAL, auth = self.auth, verify = False, headers = self.__headers, data = self.__request)
        return rsp.text, rsp.status_code

    def fetch_caseface_(self):
        rsp =  self.__rS.get(self.BRANCH_URL_LOCAL, auth = self.auth, verify = False, headers = self.__headers )
        return rsp.text, rsp.status_code

    def create_caseface_(self):
        rsp = self.__rS.post(self.BRANCH_URL_LOCAL, auth = self.auth, verify = False, headers = self.__headers, data = self.__request )
        return rsp.text, rsp.status_code
