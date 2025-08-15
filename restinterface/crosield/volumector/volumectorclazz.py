from .extension import extension

@extension()
def Volumector(self, *args, **kwargs):
    self.deviceName = kwargs.get('deviceName', 'default-device')
    self.count = kwargs.get('count', 4)
    self.routingInstance = kwargs.get('routingInstance', 'Transport-VR')
    self.hostname = '8.8.8.8'
    self.histories = {
            "Customer-JZY": [ "218.78.62.95" ],
            "Customer-YG": [ "180.101.50.188" ],
            "Customer-YanFeng": [ "172.28.34.9", "172.28.34.1" ],
        }

    def to_string():
        return f'This is {self.deviceName} {self.count} {self.routingInstance} {self.hostname} {self.histories}.'

    self.to_string = to_string
    return self