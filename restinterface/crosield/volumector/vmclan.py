from .extension import extension
from .volumectorclazz import Volumector

@extension(Volumector)
def LAN(self, *args, **kwargs):
    self.table = {

            "Customer-HAN-XUN": [ "192.168.90.9" ],

            "TEST-BaoYe": [ "10.0.99.46", "10.0.59.101" ],

            "Customer-PuFaJiTuan": [ "10.172.6.1" ],

            "Customer-Yum-China": [ "172.16.7.251", "172.16.1.94" ],

            "Customer-KangHeng": [ "192.168.0.240" ],

            "Customer-HuaQiao": [ "192.168.20.1" ],

            "xinshida": [ "192.168.99.3" ],

            # "TEST-HAN-XUN": ["10.100.6.251"],  # ["192.168.101.9", "10.100.6.251"],
            # "Customer-YanFeng": [ "172.28.34.9", "172.28.34.1" ],

        }

    self.volume = kwargs.get('volume', 'LAN')
    self.super_to_string = self.to_string

    def to_string():
        # print(self.super_to_string())
        return f"This is {self.volume} {self.table}."

    def default_vector(orgName):
        return self.table.get(orgName, [ "16.16.16.16" ])

    self.to_string = to_string
    self.default_vector = default_vector
    return self