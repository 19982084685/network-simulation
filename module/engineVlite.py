from module.entity import *
from module.modcfg import *
from core.simapi import *


class CEngine(CEntity):
    def __init__(self, parent=None, N=4):
        super().__init__(parent)
        self.name = 'Engine'
        self.mytable = {}
        self.life = 3
        self.myAddr = int(MAC_MAX_ADR * rand())
        self.N = N
        self.VLAN = {}

    def __repr__(self):
        return "MAC(%s)" % self.myAddr

    def addr(self, mac=None):  # 设置或获取实体的mac地址
        if mac is None:
            return self.myAddr
        else:
            self.myAddr = mac

    def distrib(self, intf, frame, v=None):
        """src = self.addr()
        frame.mSrc = src"""
        for ss in v[1]:
            if ss != intf:
                fr = copy.deepcopy(frame)
                self.send(ss, fr)
        # del fr

    def handle_rx(self, intf_no, frame, dst=None, src=None):
        dst = frame.mDst
        src = frame.mSrc
        v = self.revlan(intf_no)
        self.deltab()
        if v == -1:
            vid = str(frame.vid)
            v = (vid, self.VLAN[vid])
        elif v is None:
            del frame
            return "端口未分配"
        else:
            frame.vid = int(v[0])

        t = simtime()
        self.mytable[src] = (intf_no, t)

        # if not (dst == self.myAddr):
        if dst in self.mytable:
            if self.mytable[dst][0] in v[1]:
                self.send(self.mytable[dst][0], frame)
            else:
                del frame
        else:
            self.distrib(intf_no, frame, v)
        """else:
            # self.mytable[src]=intf_no
            del frame"""

    def tab(self):
        return self.mytable

    def revlan(self, intf):
        x = 0
        myz = None
        for i in self.VLAN:
            if intf in self.VLAN[i]:
                x += 1
                myz = (i, self.VLAN[i])
        if x == 0:
            return None
        elif x == 1:
            return myz
        else:
            return -1

    def deltab(self):
        tn = simtime()
        for i in self.mytable:
            t = self.mytable[i][1]
            if tn > t + self.life:
                del self.mytable[i]
