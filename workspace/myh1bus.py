from channel.bus import *
from device.Host1 import  *
Title=\
"""BUS和host1的局域网仿真环境"""
N=8
def go():
    link=CBus("chn",delay=0.001)
    a=0;b=N
    while a < b:
        a+=1
        s="h"+str(a)
        CHost1.create(s)
        dev = getdevbyname(s)
        link.LinkTo(dev.mac)



robot.start()
import code
code.interact(local=locals(), banner=Title)
