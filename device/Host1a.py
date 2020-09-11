from device.BaseDevice import CBaseHost
from module.App1 import *
from module.mac1 import *

mac_sap1 = 4;mac_sap2=6

class CHost1a(CBaseHost):
    def __init__(self, name, addr=None):
        super().__init__()
        self.app1 = CApp1(name)
        self.app2 = CApp1(name)
        self.mac = CMac1(name)
        CApp1.binding(self.app1,0,self.mac,mac_sap1)
        CApp1.binding(self.app2, 0, self.mac, mac_sap2)
        if addr != None:
            self.mac.addr(addr)

    def addr(self):
        return self.mac.addr()