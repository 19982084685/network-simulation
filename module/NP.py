from module.entity import *
from module.modcfg import *
from module.pdu import CPacket


class CNP(CEntity):
    def __init__(self, parent=None, hr=0):
        super().__init__(parent)
        self.name = 'NP'
        self.enable = hr
        self.FIBtable = {}
        self.iptable = {}
        # self.muti = []

    def handle_req(self, sap_no, tra, dst=None, src=None):
        packet = CPacket()
        packet.setData(tra)
        packet.nProt = sap_no
        packet.nDst = dst
        if dst is None:
            packet.nDst = IP_BRD_ADR
        act = self.lookup(dst)
        packet.nSrc = self.iptable[act[1]]
        self.send(act[1], packet, self.ip2mac(act[0]), self.ip2mac(self.iptable[act[1]]))

    def handle_rx(self, intf_no, packet, dst=None, src=None):
        dst = packet.nDst
        if self.enable and (dst < IP_BRD_ADR):  # and (dst % 100 != 99):
            self.route(intf_no, packet, dst)
            return
        '''if (dst < IP_MAX_ADR) and (dst != self.iptable[intf_no]):
            del packet  # 滤掉dst是单播且不是自己的分组
            return'''
        '''if IP_MAX_ADR <= dst < IP_BRD_ADR:  # and (dst not in self.muti):
            del packet
            return'''
        tra = packet.getData()
        src = packet.nSrc
        sap = packet.nProt
        if sap in self.sap_tab:  # sap 有绑定才递交
            self.deliver(sap, tra, dst, src)
        else:
            print("Error NP : 未绑定sap %d" % sap)
            del packet

    def route(self, intf_no, packet, dst):
        act = self.lookup(dst)
        if act[1] == intf_no:
            print("出现回路，已删除报文")
            del packet
            return
        else:
            if not act[0]:
                packet.nDst = 65535
        self.send(act[1], packet, self.ip2mac(act[0]), self.ip2mac(self.iptable[act[1]]))

    def lookup(self, dst):
        if dst < IP_MAX_ADR:
            nip = dst % 100
            sub = dst - nip
            if self.FIBtable.get(sub) is None:
                try:
                    return self.FIBtable[0]
                except KeyError:
                    print("默认网关未设置或路由失败，将删除分组")
                    return (-1), 1
            else:
                x = self.FIBtable[sub]
                if x[0] % 100 == 0:
                    if nip == 99:
                        return None, x[1]
                    else:
                        return dst, x[1]
                else:
                    return x
        else:
            return dst, 1

    def addFIB(self, dstsub, nextstep, intf):
        self.FIBtable[dstsub] = (nextstep, intf)

    def delFIB(self, dstsub):
        if self.FIBtable.get(dstsub):
            del self.FIBtable[dstsub]
            return True
        else:
            return False

    def addip(self, intf, val):
        self.iptable[intf] = val

    @staticmethod
    def ip2mac(ip):
        # 将IP地址转换为MAC地址的算法
        mac = ip
        return mac

    """def addmuti(self, group):
        group = int(group)
        if group not in self.muti:
            self.muti.append(group)
            return True
        else:
            return False

    def delmuti(self, group):
        group = int(group)
        if group in self.muti:
            self.muti.remove(group)
            return True
        else:
            return False"""
