
from random import expovariate as ernd
from module.entity import *
from core.timer import *
from core.simapi import *

class CAlohaApp(CEntity):
    def __init__(self, appName, parent=None):
        super().__init__(parent)
        self.sCount = 0
        self.rCount = 0
        self.name = appName
        self.timer=CTimer()
        self.T = 0.001
        self.my_t=self.T

    def tx(self,rate=1.0):
        self.msg = "this is the aloha frame"
        self.cnt = 10000
        self.delay = 1.0/rate
        self.d=ernd(1.0/self.delay)
        if self.d <= self.my_t:
            self.timer.start(self.T,self.OnTimer)
        else:
            self.timer.start(self.T,self.retx)
    def OnTimer(self):
        # smprint("[%s sent]%s" % (self.name,self.msg))
        apdu = copy.deepcopy(self.msg)
        self.send(0, apdu)
        self.sCount += 1
        self.cnt -= 1
        self.my_t += self.T
        if self.cnt > 0:
            self.d += ernd(1.0/self.delay)
            if self.d <= self.my_t:
                self.timer.start(self.T, self.OnTimer)
            else:
                self.timer.start(self.T, self.retx)
    def retx(self):
        self.my_t += self.T
        if self.d <= self.my_t:
            self.timer.start(self.T, self.OnTimer)
        else:
            self.timer.start(self.T, self.retx)
    def handle_rx(self, intf_no, apdu, dst=None, src=None):
        self.rCount += 1
        # smprint("[%s rcvd]%s" % (self.name,apdu))
        del apdu

    def stat(self):
        print("%s 统计：发送%d 接收%d" % (self.name,self.sCount,self.rCount))
