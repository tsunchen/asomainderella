#!/usr/bin/python
#coding: UTF-8
import aiohttp
from ...director.liyuandirector_ import *


class Aoicfu:

    _pORT  = os.getenv("VAPIPORT")
    _uPASS = (os.getenv("VUADM"), os.getenv("VUPAS"))
    _uRL   = (os.getenv("VURL"), os.getenv("VURLW"))

    @LIYUANDirector(_uRL, _uPASS, _pORT)
    async def action_restinterface_(self, url, auth, port):
        # print("urlpath %s, request %s, url %s, auth %s, port %s " % (self.__urlpath, self.__request, url, auth, port))
        # BASE_URL = url + ":" + port
        BASE_URL = '{}:{}'.format(url, port)
        self.__BRANCH_URL_LOCAL = urljoin(BASE_URL, self.__urlpath)
        self.__auth = auth
        return await self.caSelection(self.__rinttype)


    # 2021.6.4 create_sessor_
    # 2021.1.1 cfue interface case
    async def creates(self):
        async with aiohttp.ClientSession(connector = aiohttp.TCPConnector(limit = 64, verify_ssl = False)) as session:
            async with session.post(self.__BRANCH_URL_LOCAL,
                                          data = self.__request,
                                          auth = aiohttp.BasicAuth(login = self.__auth[0], password = self.__auth[1]),
                                          headers = self.__headers) as resp:
                body = await resp.text()
                # handle the error
                if resp.status >= 400:
                    print('.error: %s' % body)
                pageJson = await resp.json()
                return pageJson, resp.status


    # 2021.6.3 fetch_sessor_
    async def fetches(self):
        async with aiohttp.ClientSession(connector = aiohttp.TCPConnector(limit = 64, verify_ssl = False)) as session:
            # login = self.__auth[0], password = self.__auth[1]
            async with session.get(self.__BRANCH_URL_LOCAL,
                                         auth = aiohttp.BasicAuth(login = self.__auth[0], password = self.__auth[1]),
                                         headers = self.__headers) as resp:
                body = await resp.text()
                # handle the error
                # if resp.status >= 400:
                #     print('.error: %s' % body)
                if 200 == resp.status:
                    pageJson = await resp.json()
                else:
                    pageJson = None
                return pageJson, resp.status


    # 2021.6.9 update_sessor_
    async def updates(self):
        async with aiohttp.ClientSession(connector = aiohttp.TCPConnector(limit = 64, verify_ssl = False)) as session:
            async with session.put(self.__BRANCH_URL_LOCAL,
                                         data = self.__request,
                                         auth = aiohttp.BasicAuth(login = self.__auth[0], password = self.__auth[1]),
                                         headers = self.__headers) as resp:
                body = await resp.text()
                # handle the error
                if resp.status >= 400:
                    print('.error: %s' % body)
                pageJson = await resp.json()
                return pageJson, resp.status


    # 2022.3.27
    def syncget(self):
        rsp =  requests.get(self.__BRANCH_URL_LOCAL, auth = self.__auth, verify = False, headers = self.__headers )
        return rsp.json(), rsp.status_code


    async def caSelection(self, caseface):
        return await getattr(self, caseface)()


    __slots__ = ( '__headers', '__auth', '__BRANCH_URL_LOCAL', '__rinttype', '__request', '__urlpath' )

    def __init__(self, URLPATH, REQUEST, RINTTYPE):
        self.__urlpath          = URLPATH
        self.__request          = REQUEST
        self.__rinttype         = RINTTYPE
        self.__BRANCH_URL_LOCAL = ""
        self.__auth             = ""
        self.__headers          = {'Accept': 'application/json', 'Content-Type': 'application/json',}