from .extension import extension
from .volumectorclazz import Volumector

@extension(Volumector)
def PseudoSpoke(self, *args, **kwargs):
    self.table = {

        "Customer-HAN-XUN" : [ "HanXun-CPE-ShangHai-001" ],

        "Customer-HuaQiao" : [ "Customer-HuaQiao-CPE-ShangHai-001-SD1000068013" ],

        "Customer-KangHeng" : [ "KangHeng-ShangHai-CPE-001" ],

        "Customer-PuFaJiTuan" : [ "PuFaJiTuan-000000-01-S", "PuFaJiTuan-000000-01-M" ],

        "Customer-Yum-China" : [ "Yum-China-SH-CPE-IDC-001" ],

        "xinshida" : [ "XSD-SH-CPE-001" ],

        "TEST-BaoYe" : [ "TEST-BaoYe-CPE-ShangHai-001" ],

    }

    self.volume = kwargs.get('volume', 'PseudoSpoke')
    self.super_to_string = self.to_string

    def to_string():
        print(self.super_to_string())
        return f"This is {self.volume} {self.table}."

    def default_vector(orgName):
        return self.table.get(orgName, [ "controller01", "controller02" ])

    self.to_string = to_string
    self.default_vector = default_vector

    return self