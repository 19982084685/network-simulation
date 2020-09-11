from module.entity import *
from module.modcfg import *
from core.simapi import *


class CEngine(CEntity):
    def __init__(self, parent=None, N=8):
        super().__init__(parent)
        self.name = 'Engine'
        self.mytable = {}
        self.myAddr = int(MAC_MAX_ADR * rand())
        self.N = N
        self.life = 3

    def __repr__(self):
        return "MAC(%s)" % self.myAddr

    def addr(self, mac=None):  # 设置或获取实体的mac地址
        if mac is None:
            return self.myAddr
        else:
            self.myAddr = mac

    def distrib(self, intf, frame):
        """src = self.addr()
        frame.mSrc = src"""
        for ss in self.intf_tab:  # 将该帧拷贝多份，分发到各个站点，入intf除外
            if ss != intf:
                fr = copy.deepcopy(frame)
                self.send(ss, fr)
        del fr

    def handle_rx(self, intf_no, frame, dst=None, src=None):
        dst = frame.mDst
        src = frame.mSrc
        self.deltab()
        t = simtime()
        self.mytable[src] = (intf_no, t)
        #if not (dst == self.myAddr):
        if dst in self.mytable:
            self.send(self.mytable[dst][0], frame)
        else:
            self.distrib(intf_no, frame)
        """else:
            # self.mytable[src]=intf_no
            del frame"""

    def tab(self):
        return self.mytable

    def deltab(self):
        tn = simtime()
        for i in self.mytable:
            t = self.mytable[i][1]
            if tn > t + self.life:
                del self.mytable[i]
