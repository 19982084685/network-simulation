from module.App1 import *
from module.NP import *
from module.mac1 import *

mac_sap = 5


class CHost2(CBaseHost):
    def __init__(self, name):
        super().__init__()
        self.app1 = CApp1(name)
        self.hNP = CNP(name, 0)
        self.mac = CMac1(name)
        self.app1.binding(0, self.hNP, 1)
        self.hNP.binding(1, self.mac, mac_sap)

    def addr(self):
        return self.mac.addr()

    def setip(self, intf=1, ip=None):
        self.hNP.addip(intf, ip)
        self.mac.addr(ip)
