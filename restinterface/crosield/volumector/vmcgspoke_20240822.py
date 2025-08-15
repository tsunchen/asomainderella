from .extension import extension
from .volumectorclazz import Volumector

@extension(Volumector)
def GSPOKE(self, *args, **kwargs):
    self.table = {

            "Customer-HuaQiao" : [ "Customer-HuaQiao-CPE-ShangHai-001-SD1000068013" ],
            "Customer-KangHeng" : [ "KangHeng-ShangHai-CPE-001" ],

        }

    self.volume = kwargs.get('volume', 'GSPOKE')
    self.super_to_string = self.to_string

    def to_string():
        print(self.super_to_string())
        return f"This is {self.volume} {self.table}."

    def default_vector(orgName):
        return self.table.get(orgName, [ "controller01", "controller02" ])

    self.to_string = to_string
    self.default_vector = default_vector

    return self