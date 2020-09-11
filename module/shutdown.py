from module.entity import *

class Shut(CEntity):
    def __init__(self, parent=None):
        CEntity.__init__(self, parent)
        self.name = 'SHUT'
        self.rec=0
    def __repr__(self):
        return "Shutdown"
    def handle_req(self, sap, pkt, dst=None, src=None):
        self.rec+=1
        pass
    def handle_rx(self, intf_no, frame, dst=None, src=None):
        pass
    def stat(self):
        print("阻挡了%d个报文" % self.rec)