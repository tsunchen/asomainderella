
def hud(obj):
    obj.pORTk = "9183"
    obj.pORT  = "9182"
    # obj.uPASS = ('yaxin', 'YAxin@123')
    obj.uPASS = ('Administrator', 'Versa#123')
    obj.uRL   = ("172.17.21.1", "61.151.158.121")
    return obj


def wan(cls):
    """ The decorator is for class vtg_interface. """
    def __wantable():
        return {
            "Customer-Yum-China": [ "222.73.137.150" ],
            "Customer-JZY": [ "218.78.62.95" ],
            "Customer-KangHeng": [ "58.34.73.155", "8.8.8.8" ],
        }
    cls.__wan = __wan
    return cls
