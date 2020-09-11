from module.pdu import *

appd = CAppData("this is a application data")

udp = Cudp()
udp.pDst = 80
udp.pSrc = 1020
udp.setData(appd)       # appd封装进udp

pkt = CPacket()
pkt.nDst = 8020
pkt.nSrc = 2080
pkt.nProt = 17
pkt.setData(udp)        # udp封装进pkt

fm = CFrame()
fm.mDst = 1122
fm.mSrc = 3344
fm.mType = 56
fm.setData(pkt)         # pkt 封装进frame

            # 分别打印各个报文
print(str(fm))
print(str(pkt))
print(str(udp))
print(str(appd))

pk = fm
print("从封装中取出报文再打印")
while pk != None:
    print(str(pk))
    pk = pk.getData()

