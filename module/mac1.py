from module.entity import *
from module.modcfg import *
from module.pdu import CFrame


class CMac1(CEntity):
    """  MAC 帧协议实体，实现mac帧的封装、解封装、过滤
        作为主机mac或路由器mac
        服务访问点号码 1~65535，sap0保留未用
    """

    def __init__(self, parent=None):
        CEntity.__init__(self, parent)
        self.name = 'MAC'
        self.myAddr = int(MAC_MAX_ADR * rand())  # 实体的MAC地址=随机值
        self.intf = 0  # 只有一个接口，号码为0
        self.muti = []
        # self.switchmac=[1111,2222,3333,4444]

    def __repr__(self):
        return "MAC(%s)" % self.myAddr

    def addr(self, mac=None):  # 设置或获取实体的mac地址
        if mac is None:
            return self.myAddr
        else:
            self.myAddr = mac

    def handle_req(self, sap, pkt, dst=None, src=None):
        """ 发送pkt,用帧封装后发送
            目的地址=dst，或广播地址，若dst=None
            源地址=自身地址，忽略参数
            type = sap
        """
        frame = CFrame()  # 生成帧
        frame.setData(pkt)  # 装载pkt
        frame.mType = sap
        frame.mDst = dst
        if dst is None:
            frame.mDst = MAC_BRD_ADR
        frame.mSrc = self.myAddr
        self.send(self.intf, frame)

    def handle_rx(self, intf_no, frame, dst=None, src=None):
        """
        信道帧到达：帧过滤，解封装、从sap=type向上递交
        """
        dst = frame.mDst
        #print(dst,src)
        if (dst < MAC_MAX_ADR) and (dst != self.myAddr):
            del frame  # 滤掉dst是单播且不是自己的帧
            return
        if (MAC_MAX_ADR <= dst < MAC_BRD_ADR) and (dst not in self.muti):
            del frame
            return
        pkt = frame.getData()  # 解封装
        src = frame.mSrc
        """if(src in self.switchmac):
            self.reply(src)"""
        sap = frame.mType
        if sap in self.sap_tab:  # sap 有绑定才递交
            self.deliver(sap, pkt, dst, src)
        else:
            print("Error MAC %d: 未绑定sap %d" % (self.myAddr, sap))
            del frame

    def addmuti(self, group):
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
            return False

    """def reply(self,dst=None):
        frame = CFrame()  # 生成帧
        frame.setData("reply")
        frame.mDst = dst
        if dst == None:
            frame.mDst = MAC_BRD_ADR
        frame.mSrc = self.myAddr
        self.send(self.intf, frame)
    def addswitch(self,mac):
        self.switchmac.append(mac)"""
