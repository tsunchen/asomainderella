from .extension import extension
from .volumectorclazz import Volumector

@extension(Volumector)
def WAN(self, *args, **kwargs):
    self.table = {
            "Customer-Yum-China": [ "61.169.31.253" ],
            "Customer-KangHeng": [ "58.34.73.155" ],
            "Customer-HuaQiao": [ "222.71.59.122" ],
            "xinshida": [ "180.101.50.188" ],
        }

    self.volume = kwargs.get('volume', 'WAN')
    self.super_to_string = self.to_string

    def to_string():
        print(self.super_to_string())
        return f"This is {self.volume} {self.table}."

    def default_vector(orgName):
        return self.table.get(orgName, [ "202.96.209.133", "180.101.50.188" ])

    self.to_string = to_string
    self.default_vector = default_vector

    return self