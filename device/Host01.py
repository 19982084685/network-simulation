from device.BaseDevice import CBaseHost
from module.App01 import *
from module.mac0 import *

class CHost01(CBaseHost):
    def __init__(self, name):
        super().__init__()
        self.app = CApp01(name)
        self.mac = CMac0(name)
        CApp01.binding(self.app,0,self.mac,0)
