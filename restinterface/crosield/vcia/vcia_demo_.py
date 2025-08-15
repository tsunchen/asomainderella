from functools import reduce
from functools import singledispatch


class Vector:
    __slots__ = ( 'hostname', 'routingInstance', 'count', 'deviceName' )
    def __init__(self, *, hostname = "8.8.8.8", routingInstance = "Transport-VR", count = 4, deviceName = None):
        self.deviceName = deviceName
        self.count = count
        self.routingInstance = routingInstance
        self.hostname = hostname


class Wan(Vector):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


@singledispatch
def ping(vector):
    """ ping a generic vector """
    raise TypeError(f"Can't ping vector {vector!r}")


@ping.register(Wan)
def _(wan):
    data = {"ping": {"hostname": wan.hostname
            , "routing-instance":  wan.routingInstance
            , "count": wan.count
    }}
    d, _ = Restinterface('/api/config/devices/device/{}/config/diagnostics:diagnostics/_operations/ping/'.format(wan.deviceName), json.dumps(data), 'post').action_restinterface_()
    print(attrs(wan))
    return json.loads(d).get('output').get('status')


"""
    Monoiduce VCIA
"""
class Monoiduce:
    __slots__ = ( 'value' )
    def __init__(self, data):
        self.value = data

    def unpack(self):
        ...


class MonoiduceInput(Monoiduce):
    def unpack(self):
        return self.value


class MonoiduceOutput(Monoiduce):
    def unpack(self):
        args, kwargs = self.value
        if () != args:
            return print(*args, **kwargs)
        # else:
        #    return print(*args, **kwargs)


class MonoiduceBind(Monoiduce):
    def unpack(self):
        return self.value().unpack()


def bind(monoiduce, function):
    return MonoiduceBind(lambda: function(monoiduce.unpack()))


def pure_in():
    return MonoiduceInput(None)


def side_in(*args, **kwargs):
    return MonoiduceInput(*args, **kwargs)


def pure_out(*args, **kwargs):
    return MonoiduceOutput((args, kwargs))