from functools import reduce


class Monoiduce:
    __slots__ = ( 'value' )
    def __init__(self, data):
        self.value = data

    def unpack(self):
        ...


class MonoiduceInput(Monoiduce):
    def unpack(self):
        return input()


class MonoiduceOutput(Monoiduce):
    def unpack(self):
        args, kwargs = self.value
        return print(*args, **kwargs)


class MonoiduceBind(Monoiduce):
    def unpack(self):
        return self.value().unpack()


def bind(monoiduce, function):
    return MonoiduceBind(lambda: function(monoiduce.unpack()))


def pure_in():
    return MonoiduceInput(None)


def pure_out(*args, **kwargs):
    return MonoiduceOutput((args, kwargs))


l = [ pure_out("Your input: ", end = " "), lambda _: pure_in(), lambda name: pure_out("Hello", name) ]
reduce(lambda u, v: bind(u, v), l).unpack()