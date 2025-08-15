def failover(self, butt, intf, hostname):
    """Handles failover."""
    setattr(VTG_interface, "intfoperup_", intfoperup_)
    maxnum_tback_ = 0
    try:
        for i in Attemptable_(nStart=maxnum_tback_, butt=butt, deviceName=self.__deviceName, hostName=hostname, ok="success", intf=intf):
            print('- Attempted: {}'.format(maxnum_tback_ - i))
    except Exception as err:
        print("err: ", err)
    else:
        self.park_or_overlte(butt, intf, Wansnort['PARK'].value[0])

def park_or_overlte(self, butt, intf, tag):
    """Handles park or overlte based on conditions."""
    text_intf_brief_ = ''.join([butt['vrf'], ' ', tag])
    if "LTE" == butt['network'].upper() and ("tvi-0/3001.0" == butt['name'] or int(butt['current-rx-bps']) > 4096 or int(butt['current-tx-bps']) > 1024):
        self.vtg_wan_snort_intf_id_.append(self.__deviceName)
        self.vtg_wan_snort_intf_.append(text_intf_brief_.center(30, '.'))

def park(self, butt, intf, tag):
    """Handles parking."""
    self.park_or_overlte(butt, intf, tag)

def overlte(self, butt, intf, tag):
    """Handles overlte."""
    self.park_or_overlte(butt, intf, tag)