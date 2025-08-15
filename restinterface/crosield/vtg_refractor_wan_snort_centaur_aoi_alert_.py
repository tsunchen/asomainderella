def alert(self, butt, intf, tag):
    # 2021.1.15 # intf.keydefval_(butt, 'if-proto-down', "['INFO']")
    # 2022.1.14 interface unit to insert
    intf.keydefval_(butt, 'if-proto-down', Wansnort['INFO'].value[0])
    intf.keydefval_(butt, 'network', Wansnort['ETHER'].value[0])
    # 2021.4.13 unknown network
    if (butt['network']).upper() in ["WAN2", "LTE"]:
        text_intf_brief_ = ''.join([ butt['vrf'], ' ', str(butt['if-proto-down']) ])
    else:
        # ALERT, INFO, MONITOR
        text_intf_brief_ = ''.join([ butt['vrf'], ' ', tag ]) if "MONITOR" not in butt['if-proto-down'] else ''.join([ butt['vrf'], ' ', str(butt['if-proto-down']) ])
    self.vtg_wan_snort_intf_id_.append(self.__deviceName)
    self.vtg_wan_snort_intf_.append(text_intf_brief_.center(30, '-'))