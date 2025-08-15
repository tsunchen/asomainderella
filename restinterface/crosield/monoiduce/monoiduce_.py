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
        if ('ping') == args:
            return ping(*args)
        if () == args:
            return print(*args, **kwargs)


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
