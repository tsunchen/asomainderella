#!/usr/bin/python
#coding: UTF-8
from dataclasses import dataclass, InitVar
from .cohesionar_ import *

# 2022.7.25 dataclasses, urlroute, auth, port
# 2022.5.5  timeout(32)
# 2021.9.26 return url in connecting
# 2021.8.31 casebook
# 2021.8.5  seco_str
# 2021.7.20 secit, pointmerge
# 2021.6.22 Multi-URL with weight update
# 2021.6.21 session update into director
# 2021.4.2  Hyper Bound Query Director
# 2021.1.20 session retries(4), timeout(8)
# 2020.2.1  Origin

@dataclass
class LIYUANDirector:
    PORT: InitVar[str]
    AUTH: InitVar[str]
    URL:  InitVar[str]

    def __call__(self, func):
        def inner_wrapper(*args, **kwargs):
            maxRetries, timeOut = 25, 4
            sess = requests.Session()
            sess.mount('https://', HTTPAdapter(max_retries = maxRetries))
            try:
                sess.get(url = f"https://{self.__urlroute.most_common(1)[0][0]}:{self.__port}", timeout = timeOut, verify = False)
            except requests.exceptions.ConnectionError as e:
                print(f"- Fail to connect, this {(self.__urlroute.most_common(1)[0][0])} might have been blocked or delay! ")
                self.__urlroute.subtract([self.__urlroute.most_common(1)[0][0]])
            kwargs['port'], kwargs['auth'], kwargs['url'] = self.__port, self.__auth, f"https://{(self.__urlroute.most_common(1)[0][0])}"
            print(f"- With {(kwargs['url'])} as connectable object")
            return func(*args, **kwargs)
        return inner_wrapper

    __slots__ = ( "__urlroute", "__auth", "__port", )

    def __init__(self, URL, AUTH, PORT):
        self.__urlroute = Counter(URL)
        self.__auth = AUTH
        self.__port = PORT