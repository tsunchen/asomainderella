from vcia.vcia_demo_ import *


# l = [ pure_out("Your input: ", end = " "), lambda _: pure_in(), lambda name: pure_out("Hello", name) ]
# reduce(lambda u, v: bind(u, v), l).unpack()

vec = [ 
      pure_out(end = ""),
      lambda _: side_in(( 'ping', Wan(deviceName = "dev", hostname = "8.8.8.8", routingInstance = "Internet-Transport-VR", count = 1) )),
      lambda wan: pure_out(wan),
]

reduce(lambda u, v: bind(u, v), vec).unpack()
