from module.entity import *
from core.simapi import *
class CLink(CEntity):
    """点对点信道，可设置延迟、丢包率  """
    def __init__(self, name, delay=0, loss=0.0):
        super().__init__()
        self.name = name
        self.latency = delay
        self.lossrate = loss
        self.sap_indx = 0
        self.rcvcnt = 0
        self.lostcnt = 0
        self.sentcnt = 0
    def __repr__(self):
        return self.name

    def LinkTo(self, dev, intf1=0):
        if self.sap_indx < 2:
            dev.binding(intf1,self, self.sap_indx)
            self.sap_indx += 1
        else:
            print("连接已满，无法再连接")

    def handle_req(self, sap_no, packet, dst = None, src = None):
        self.rcvcnt += 1
        if self.lossrate > rand():
            del packet
            print('lossy')
            self.lostcnt += 1
        else:
            for ss in self.sap_tab:
                if ss != sap_no:
                    Dispatch(self.latency, self.deliver,(ss, packet))
                    self.sentcnt += 1

    def delay(self, dt=0):
        if dt == 0:
            return self.latency
        else:
            self.latency = dt

    def loss(self,p=0):
        if p == 0:
            return self.lossrate
        else:
            self.lossrate = p
    def stat(self):
        print("%s 收发统计：收%d 发%d 丢失%d" % (self.name,self.rcvcnt,self.sentcnt,self.lostcnt))