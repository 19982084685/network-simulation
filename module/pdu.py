"""
    PDU

    定义各种PDU格式：    Packet格式、    Frame格式
"""
class Cpdu(object):
    def __init__(self):
        self.dLen = 0       #数据长度
        self.hLen = 0       #头部长度
        self.Data = None
    def setData(self, data):
        self.Data = data
        if isinstance(data,Cpdu):
            self.dLen = data.Length()
        else:
            self.dLen = len(data)

    def getData(self):
        return self.Data
    def Length(self):
        return self.dLen+self.hLen

class CFrame(Cpdu):
    """帧首部  CFrame=[mSrc,vid,mDst,mType,mLen,mData]"""
    def __init__(self):
        super().__init__()
        self.mSrc = 0  # 源MAC地址
        self.vid = 0  #VLAN标志
        self.mDst = 0  # 目的MAC地址
        self.mType = 0  # 帧类型
        self.hLen = 6   #帧头部长度
        self.trace = 0  # 跟踪标志

    def __repr__(self):
        return "Frame[%s-->%s,type=%s]" % (self.mSrc, self.mDst,self.mType)
    def strdata(self):
        return str(self.Data)

class CPacket(Cpdu):
    """分组结构[sAddr,dAddr,prot,ttl,data]"""
    def __init__(self):
        super().__init__()
        self.nSrc = 0       # 网络源地址
        self.nDst = 0       # 网络目的地址
        self.nProt = 0      # 载荷协议类型
        self.hLen = 8       # 分组头部长度
        self.trace = 0      # 跟踪标志

    def __repr__(self):
        return "pkt[%s-->%s prot=%s]" % (self.nSrc,self.nDst,self.nProt)
    def strdata(self):
        return str(self.Data)

class Cudp(Cpdu):
    """传输层报文结构"""
    def __init__(self):
        super().__init__()
        self.pSrc = 0       # 报文源端口
        self.pDst = 0       # 报文目的端口
        self.hLen = 4       # 报文首部长度
        self.trace = 0      # 跟踪标志
    def __repr__(self):
        return "udp[%s-->%s]" % (self.pSrc, self.pDst)
    def strdata(self):
        return str(self.Data)

class Ctcp(Cpdu):
    """传输层报文结构"""
    def __init__(self):
        super().__init__()
        self.pSrc = 0       # 报文源端口
        self.pDst = 0       # 报文目的端口
        self.ssn = 0        # 发送序号
        self.rsn = 0        # 接收序号
        self.flag = 0       # 报文类型
        self.hLen = 4       # 报文首部长度
        self.trace = 0      # 跟踪标志
    def __repr__(self):
        return "tcp[%s-->%s] sn=%d rn=%d" % (self.pSrc, self.pDst,self.ssn,self.rsn)
    def strdata(self):
        return str(self.Data)

class CAppPdu(Cpdu):
    def __init__(self,stringdata):
        super().__init__()
        self.hLen = 0
        self.Data = stringdata
        self.dLen = len(stringdata)
    def __repr__(self):
        return "%s" % self.Data
    def strdata(self):
        return str(self.Data)
    def getData(self):
        return None

class CEcho(object):
    def __init__(self):
        self.echo = 1
        self.data = "this is a ping message" 
