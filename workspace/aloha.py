from channel.bus import *
from module.myalohaApp import *
from device.Host1 import  *
Title=\
"""Aloha  信道访问实验
"""
class CAlohaHost(CBaseHost):
    def __init__(self, name):
        super().__init__()
        self.mac = CAlohaApp(name)
    def start(self,rate):
        self.mac.tx(rate)

G = 1
R=1000.0
N=10

def go():
    link = CBus("chn", delay=1.0 / R)
    a = 0; b = N
    while a < b:
        a += 1
        s = "h" + str(a)
        CAlohaHost.create(s)
        dev = getdevbyname(s)
        link.LinkTo(dev.mac)
    r = G*R/N
    print("信道速率R=%d帧 站点数N=%d 输入流量G=%0.2f" % (R,N,G))
    a = 0;b = N
    while a < b:
        a += 1
        s = "h"+str(a)
        dev = getdevbyname(s)
        dev.start(r)
def stat():
    a=0;b=N
    while a < b:
        a += 1
        s = "h"+str(a)
        dev = getdevbyname(s)
        dev.mac.stat()
robot.start()
robot.RealTime(0)
import code
code.interact(local=locals(), banner=Title)