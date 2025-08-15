#!/usr/bin/python
#coding: UTF-8
from .vtg_attemptable_ import *
from .vtg_aso_ import *


""" routines """
# 2021.2.12 taster_routine
def taster_(self):
    while True:
        delicaciesRecv = yield


def attendant(self, taste):
    """
    2022.8.11 Wansnort.X.value[0]
    2022.5.27 Function Attemptable, INFO interface
    2022.5.26 Class Attempting Countdown
    2021.7.21 recipelx exception
    2021.7.15 pointmerge
    2021.5.5 to take care of delicacies
    2021.2.12 routine
    """
    ordering = None
    taste.send(ordering)
    ordering = self.text_intf_brief_

    taste.send(ordering)
    # print("attendant %s" % ordering)


# 2021.2.12 attendant_routine
def attendant_(self, taste):
    """
    2022.8.11 Wansnort.X.value[0]
    2022.5.27 Function Attemptable, INFO interface
    2022.5.26 Class Attempting Countdown
    2021.7.21 recipelx exception
    2021.7.15 pointmerge
    2021.5.5 to take care of delicacies
    2021.2.12 routine
    """
    ordering = None
    taste.send(ordering)

    ordering = self.arrange_  # ordering = self.__text_intf_brief_
    taste.send(ordering)
    # print("attendant %s" % ordering)


@property
def arrange_(self):
    """
    2022.6.2 Arrange method
    """
    if "up" == self.__butt['if-oper-status']:
        pageJson_pings_wan_ = self.__dev.pingw_(hostname = self.__hostName, routingInstance = self.__butt['vrf'])
        if "success" != pageJson_pings_wan_:
            maxnum_tback_ = 3
            try:
                # for i in Attemptable(nStart = maxnum_tback_, butt = self.__butt, deviceName = self.__deviceName, hostName = self.__hostName, ok = "success", tryfoo_ = intfoperup_, backfoo_ = devpings_wan_):
                # for i in Attemptable( intf = self, nStart = maxnum_tback_, butt = self.__butt, deviceName = self.__deviceName, hostName = self.__hostName, ok = "success" ):
                for i in Attemptable( nStart = maxnum_tback_, butt = self.__butt, deviceName = self.__deviceName, hostName = self.__hostName, ok = "success" ):
                    print('- Attempted: {}'.format(maxnum_tback_ - i))
            except Exception as err:
                # 2021.7.20 tsunx exception replace the stopiteration
                print("Tryback_recipelx_: {}".format(err))
                # recipelx alarm-printing
                self.alarmprint_content_recipelx_()
            else:
                print('- Tryback Anything Else_: maxinum trial times of {}\n'.format(maxnum_tback_))
                ## self.__text_intf_brief_ = '{} {}'.format(self.__butt['vrf'], self.__butt['service-provider']) # v16.x.x
                ## self.__text_intf_brief_ = '{} {}'.format(self.__butt['vrf'], self.__butt['network']) # v21.2.1
                ## self.__text_intf_brief_ = '{} .P.'.format(self.__butt['vrf']) # v21.2.2 Suspended Pause Parking
                self.__text_intf_brief_ = ''.join([ self.__butt['vrf'], ' ', Wansnort.PARK.value[0] ]) # 2022.8.10
                #.=> "subject = Alarming"
    else:
        # 2020.10.14
        self.keydefval_(self.__butt, 'if-proto-down', Wansnort.INFO.value[0])
        self.keydefval_(self.__butt, 'network', Wansnort.ETHER.value[0])
        if ( (self.__butt['network']).upper() in ("LTE", "WAN2", "INTERNET2") ):
            self.__text_intf_brief_ = ''.join([ self.__butt['vrf'], ' ', str(self.__butt['if-proto-down']) ])
        else:
            # ALERT, INFO, MONITOR
            self.__text_intf_brief_ = ''.join([ self.__butt['vrf'], ' ', Wansnort.ALERT.value[0] ]) if "MONITOR" not in self.__butt['if-proto-down'] else ''.join([ self.__butt['vrf'], ' ', str(self.__butt['if-proto-down']) ])
        #.=> "subject = Pending"

    # Alarm Filter
    if ( "" == self.__text_intf_brief_ ):
        ... # print(self.__deviceName)
    elif ("['MONITOR']" in self.__text_intf_brief_):
        print('- {} of the MONITOR {} interface.'.format(self.__deviceName, self.__text_intf_brief_))
    elif (Wansnort.INFO.value[0] in self.__text_intf_brief_ ):
        # INFO interface to be inserted
        print('- {} of the INFO {} interface to be plugged in.'.format(self.__deviceName, self.__text_intf_brief_))
    elif (Wansnort.PARK.value[0] in self.__text_intf_brief_ ):
        print('- {} of the Parking {} interface to be woke up.'.format(self.__deviceName, self.__text_intf_brief_))
    elif (Wansnort.ALERT.value[0] in self.__text_intf_brief_):
        # alert alarm-printing
        self.alarmprint_content_alert_()
    else:
        # warn alarm-printing
        self.alarmprint_content_warn_()

    return self.__text_intf_brief_, self.__deviceName