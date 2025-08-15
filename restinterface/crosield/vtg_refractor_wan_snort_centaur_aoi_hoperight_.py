def hoperight(self, tag):
    # 2024.3.2 painleft
    # Wansnort['CRITICAL'].value[0].center(30, '.')
    print(f'- ! Off Line: {self.__deviceName} {self.__deviceOrg}')
    self.vtg_wan_snort_intf_id_.append(self.__deviceName)
    self.vtg_wan_snort_intf_.append(tag)