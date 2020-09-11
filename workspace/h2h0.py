from channel.link import *
from device.BaseDevice import getdevbyname
from device.Host0 import  *

Title=\
"""Host0 to Host0 实验测试
    仿真命令：h1.app.tx("字符串"）
"""
link = CLink("chn",loss=0.1,delay=0.02)
CHost0.create("h1")
h1=getdevbyname("h1")
h2=CHost0("h2")
link.LinkTo(h1.mac)
link.LinkTo(h2.mac)


robot.start()
import code
code.interact(local=locals(), banner=Title)