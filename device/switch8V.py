from device.BaseDevice import *
from module.mac0 import *
from module.engineVlite import *

N = 8


class CSwitch(CBaseDevice):
    def __init__(self, name, addr=None):
        super().__init__()
        self.engine = CEngine(name, N)
        for i in range(0, N):
            self.__dict__["self.mym" + str(i)] = CMac0()
            self.engine.binding(i, self.__dict__["self.mym" + str(i)], 0)
        if addr is not None:
            self.engine.addr(addr)

    def addr(self):
        return self.engine.addr()

    def convlan(self, seq="1", val=None):
        if val is None:
            val = [[0, 1, 2, 3, 4, 5, 6, 7]]
        self.engine.VLAN = dict(zip(seq, val))
