
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

    def tx(self,rate=1.0):
        self.msg = "this is the aloha frame"
        self.cnt = 10000
        self.delay = 1.0/rate
        self.timer.start(ernd(1.0/self.delay),self.OnTimer)

    def OnTimer(self):
        # smprint("[%s sent]%s" % (self.name,self.msg))
        apdu = copy.deepcopy(self.msg)
        self.send(0, apdu)
        self.sCount += 1
        self.cnt -= 1
        if self.cnt > 0:
            self.timer.start(ernd(1.0/self.delay),self.OnTimer)

    def handle_rx(self, intf_no, apdu, dst=None, src=None):
        self.rCount += 1
        # smprint("[%s rcvd]%s" % (self.name,apdu))
        del apdu

    def stat(self):
        print("%s 统计：发送%d 接收%d" % (self.name,self.sCount,self.rCount))
