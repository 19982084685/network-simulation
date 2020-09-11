from module.entity import *
from module.pdu import *
from core.simapi import *
from device.BaseDevice import *

class CApp1(CEntity):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.sCount = 0
        self.rCount = 0
        self.name = "App1"

    def tx(self,dst,string):        # 目的地址，或目的对象
        apkt = CAppPdu(string)      # 用appPdu封装 app 数据
        self.sCount += 1
        d=dst
        if isinstance(dst,CBaseHost):   #目的对象？
            d=dst.addr()
        self.send(0,apkt,d)

    def handle_rx(self, intf_no, apkt, dst=None, src=None):
        self.rCount += 1
        smprint("%s[%d<--%d] %s" % (self.parent(),dst,src,str(apkt)))

    def stat(self):
        print("%s 统计：发送%d 接收%d" % (self.name,self.sCount,self.rCount))