from channel.link import *
from device.BaseDevice import getdevbyname
from device.Host01 import  *

Title=\
"""Host01 to Host01 实验测试
    仿真命令：h1.app.tx("字符串"）
"""
link = CLink("chn",loss=0.1,delay=0.02)
CHost01.create("h1")
h1=getdevbyname("h1")
h2=CHost01("h2")
link.LinkTo(h1.mac)
link.LinkTo(h2.mac)


def go():
    h1.app.tx("站点%s发送出来的信息" % h1,15,1.2)
    h2.app.tx("我是h2,明晚出来哈皮，行吗？",16,0.9)

robot.start()
import code
code.interact(local=locals(), banner=Title)