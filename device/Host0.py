from device.BaseDevice import CBaseHost
from module.App0 import *
from module.mac0 import *

class CHost0(CBaseHost):
    def __init__(self, name):
        super().__init__()
        self.app = CApp0(name)
        self.mac = CMac0(name)
        CApp0.binding(self.app,0,self.mac,0)
