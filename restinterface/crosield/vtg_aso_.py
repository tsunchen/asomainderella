#!/usr/bin/python
#coding: UTF-8

""" Arrange.Step.Once """
class ASO:
    __slots__ = ( "_done", "_eres", "coro" )

    def __init__(self, coro):
        self.coro = coro
        self._eres = None
        self._done = False

    def run(self):
        print('-' * 8)
        if not self._done:
            try:
                c = self.coro.send(None)
            except StopIteration as e:
                self._eres = e.value
                self._done = True
            else:
                delicacies, rival = c.value
                print("- .ASO. (%s) %s" % (delicacies, rival))
        else:
            print('- .ASO. has been done.')
        print('-' * 8)


async def once_(self):
    print(f'- Once begin -')
    result = await self.step_()
    print(f'- Once end -')


async def step_(self):
    stepRes = self.arrange_
    await Arrangable(stepRes)
    return stepRes


class Arrangable:
    __slots__ = ( 'value' )

    def __init__(self, obj):
        self.value = obj

    def __await__(self):
        yield self