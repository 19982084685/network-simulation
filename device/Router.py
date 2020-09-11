from device.BaseDevice import *
from module.mac1 import *
from module.NP import *

N = 4
mac_sap = 5


class CRouter(CBaseDevice):
    def __init__(self, name):
        super().__init__()
        self.rNP = CNP(name, 1)
        for i in range(0, N):
            self.__dict__["self.mym" + str(i)] = CMac1()
            self.rNP.binding(i, self.__dict__["self.mym" + str(i)], mac_sap)

    def setip(self, seq):
        # 以列表的形式按顺序读入每个端口的IP地址
        i = 0
        for j in seq:
            self.rNP.addip(i, j)
            (self.__dict__["self.mym" + str(i)]).addr(j)
            i += 1
        return
