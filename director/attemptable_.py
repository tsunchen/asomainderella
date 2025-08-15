#!/usr/bin/python
#coding: UTF-8
from enum import Enum

class Lansnort(Enum):
    # __slots__ = ( "DC", "UR", "RSR", "LMB" )

    LMB    = ('[`]Λ[`]', 'oper = dn', 'admin = up', '#ffbf00', '#ffffff')  # Lambda mode
    RSR    = ('[`]R[`]',  'oper = up', 'admin = up', '#dda0dd', '#ffffff')  # Remote REQUEST SYSTEM REBOOT
    UR     = ('...U...',  'oper = dn', 'admin = dn', '#ff007f', '#ffffff')  # Unreachable
    DC     = ('[`]D[`]',  'oper = up', 'admin = up', '#dda0dd', '#ffffff')  # Discamouflage


class Wansnort(Enum):
    # __slots__ = ( "ETHER", "NPA", "LTEM", "CRITICAL", "MONITOR", "INFO", "ALERT", "PARK", "OVERLTE", "OVER5G" )

    OVER5G   = ('[^.5.^]', 'oper = up', 'admin = up')
    OVERLTE  = ('[^.4.^]', 'oper = up', 'admin = up')
    PARK     = ('[`.P.`]', 'oper = up', 'admin = up', 'ping = disable')
    ALERT    = ('[`]A[`]', 'oper = dn', 'admin = up')
    INFO     = ('[`]I[`]', 'oper = dn', 'admin = up')
    MONITOR  = ('[`]M[`]', 'oper = dn', 'admin = up')
    CRITICAL = ('...U...', 'oper = dn', 'admin = dn')
    LTEM     = ("LTE-Transport-VR ['MONITOR']")
    NPA      = ('N.P.A')
    ETHER    = ('.ETHER.')