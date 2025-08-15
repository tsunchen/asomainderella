def failover(self, butt, intf, hostname):
    """ ('pageJson_pings_wans handler...') """
    setattr(VTG_interface, "intfoperup_", intfoperup_)
    maxnum_tback_ = 0
    try:
        for i in Attemptable_(nStart = maxnum_tback_, butt = butt, deviceName = self.__deviceName, hostName = hostname, ok = "success", intf = intf):
            print('- Attempted: {}'.format(maxnum_tback_ - i))
    except Exception as err:
        print("err: ", err)
    else:
        # ("handler.park")
        self.park(butt, intf, Wansnort['PARK'].value[0])
    finally:
        # ("handler.overlte")
        self.overlte(butt, intf, Wansnort['OVERLTE'].value[0])


def park(self, butt, intf, tag):
    # PARK, Suspended Pause Parking [NHP]
    text_intf_brief_ = ''.join([ butt['vrf'], ' ', tag ])
    self.vtg_wan_snort_intf_id_.append(self.__deviceName)
    self.vtg_wan_snort_intf_.append(text_intf_brief_.center(30, '.'))


def overlte(self, butt, intf, tag):
    if "tvi-0/3001.0" == butt['name']:
        intf.keydefval_(butt, 'network', Wansnort['ETHER'].value[0])
    if "LTE" == butt['network'].upper(): # Over the LTE
        if int(butt['current-rx-bps']) > 4096 or int(butt['current-tx-bps']) > 1024:
            text_intf_brief_ = ''.join([ butt['vrf'], ' ', tag ])
            self.vtg_wan_snort_intf_id_.append(self.__deviceName)
            self.vtg_wan_snort_intf_.append(text_intf_brief_.center(30, '.'))
