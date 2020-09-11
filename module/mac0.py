from module.entity import *

class CMac0(CEntity):
    """ 交换机mac，SAP(0）与intf（0）直通，或作为直通模块使用 """
    def __init__(self, parent=None):
        CEntity.__init__(self, parent)
        self.name = 'MAC'
        self.rec=0
        self.sen=0
    def __repr__(self):
        return "Pure MAC"

    def handle_req(self, sap, pkt, dst=None, src=None):
        """MAC发送请求：直通处理，pkt直接从默认intf发送出去 """
        self.send(0, pkt)
        self.sen+=1
    def handle_rx(self, intf_no, frame, dst=None, src=None):
        """MAC接收通知: 直通处理，直接从默认sap递交上去 """
        self.deliver(0, frame)
        self.rec+=1
    def stat(self):
        print("收%d 发%d" % (self.rec,self.sen))
