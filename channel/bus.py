from module.entity import *
from random import random as rand
from core.simapi import *


class CBus(CEntity):
    """总线信道，可设置信道长度,用延迟表示
       设置延迟  inst.delay(delay）
    """
    def __init__(self, name, delay=1):
        super().__init__()
        self.name = name
        self.gcnt = 0
        self.scnt = 0
        self.simt = 0
        self.sap_indx = 0
        self.latency = delay
        self.count=0        # 当前信道上的并发数量
        self.gauge=0        # 当前信道的并发水平(单增，count为0时也清零)
        self.sta_tab={}     # 站点字典表，格式为{sap:(STA,intf)}

    def __repr__(self):
        return self.name

    def handle_req(self, sap_no, packet, dst = None, src = None):
        """开始发送帧"""
        self.gcnt += 1      # 发送帧统计
        self.count += 1     # 增加信道帧活动计数
        self.gauge += 1     # 增加信道帧活动度量
        t = simtime()
        if t > self.simt+10.0:
            self.simt=t
            self.stat()
        Dispatch(self.latency,self.distrib,(sap_no,packet))

    def distrib(self,sap,pkt,dst=None,src = None):
        """帧发送完成"""
        self.count -= 1                     # 信道帧活动计数减少
        if self.count == 0:                 # 如果计数为0，信道变空闲
            if self.gauge == 1:              # 如果gauge 为1，表明信道一直只有一个帧，成功！
                self.scnt += 1              # 成功帧统计
                for ss in self.sap_tab:     # 未遭冲突，将该帧拷贝多份，分发到各个站点，入sap除外
                    if ss != sap:
                        pk = copy.deepcopy(pkt)
                        self.deliver(ss,pk)
            self.gauge = 0                  # 当前信道空闲
        del pkt

    def LinkTo(self, dev,):
        dev.binding(0,self, self.sap_indx)
        self.sap_indx += 1

    def delay(self, dt=0):
        if dt == 0:
            return self.latency
        else:
            self.latency = dt

    def stat(self):
        t=simtime()/self.latency
        smprint('g=%d(%0.4f)  s=%d(%0.4f)' %(self.gcnt,self.gcnt/t,self.scnt,self.scnt/t))