#!/usr/bin/python
#coding: UTF-8
from .vtg_device_ import *

class VTG_oauth(object):
    """
    2023.3.3   update
    2021.11.21 set
    """
    __uPASS = (os.getenv("VUADM"), os.getenv("VUPAS"))

    def __init__(self, *args, **kwargs):
        self.__ri_oauth_creation_urlpath_ = "/auth/token"

    @property
    def oauth_bearer_(self):
        """ /auth/token """
        oauth_bearerd = { "client_id": "voae_rest", "client_secret": "asrevnet_123", "grant_type": "password", "username": VTG_oauth.__uPASS[0], "password": VTG_oauth.__uPASS[1] }
        print(oauth_bearerd)
        oauth_bearer_, rc = Restinterface(self.__ri_oauth_creation_urlpath_, json.dumps(oauth_bearerd), 'fet').action_restinterface_()
        # print("oauth_bearer_: ", rc)

        '''
        # oauth_bearer_, rc = Restinterface(self.__ri_oauth_creation_urlpath_, json.dumps(oauth_bearerd), 'fet').action_restinterface_()
        # print("oauth_bearer_: ", rc)
        # print("oauth_bearer_: ", oauth_bearer_)
        # data = json.loads(oauth_bearer_)
        # print(json.dumps(data, indent = 4))
        '''
        return rc, oauth_bearer_

