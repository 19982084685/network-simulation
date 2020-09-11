from device.BaseDevice import CBaseHost
from module.App1 import *
from module.mac1 import *

mac_sap = 4

class CHost1(CBaseHost):
    def __init__(self, name, addr=None):
        super().__init__()
        self.app = CApp1(name)
        self.mac = CMac1(name)
        CApp1.binding(self.app,0,self.mac,mac_sap)
        if addr != None:
            self.mac.addr(addr)

    def addr(self):
        return self.mac.addr()