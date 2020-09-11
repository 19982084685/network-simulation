from module.entity import *
from core.timer import *
from core.simapi import *

class CApp01(CEntity):
    def __init__(self, appName, parent=None):
        super().__init__(parent)
        self.sCount = 0
        self.rCount = 0
        self.name = appName
        self.timer=CTimer()

    def tx(self, string: object, cnt: object = None, delay: object = None) -> object:
        if cnt == None:
            self.send(0,string)
            return
        self.msg = string
        self.cnt = cnt
        self.delay = 1.0
        if delay != None:
            self.delay = delay
        if self.cnt > 0:
            self.timer.start(self.delay,self.OnTimer)

    def OnTimer(self):
        self.send(0, self.msg)
        self.sCount += 1
        self.cnt -= 1
        if self.cnt > 0:
            self.timer.restart()

    def handle_rx(self, intf_no, string, dst=None, src=None):
        self.rCount += 1
        smprint("[%s rcvd]%s" % (self.name,string))

    def stat(self):
        print("%s 统计：发送%d 接收%d" % (self.name,self.sCount,self.rCount))