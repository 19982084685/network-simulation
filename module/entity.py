import copy
from random import random as rand
from core.robot import *
from core.simapi import *

class CEntity(object):
    """通信模块实体的基类，用于生成协议实体、交换实体等。
    Entity类对上提供了SAP服务接口，分别是handle_req和deliver
        handle_req(sap号x，pdu,目的，源)，由上层启动，接收上层送到x号sap的pdu,继承类须重载该函数
        deliver(sap号y，pdu,目的，源), 自己发起，从s号sap向上层递交pdu，继承实体可直接使用
    Entity类对下提供了驱动接口，分别时send和handle_rx
        send(接口号k，pdu，目的，源)，自己发起，从自己的第k号接口向下传递pdu
        handle_rx(接口号k，pdu，目的，源），由下层启动，从接口k接收进来的pdu
    Entity 提供binding绑定服务，用于将自己的对下接口k，与下层实体E的x号SAP绑定，send和hanle_rx通过接口k实现与实体E的x号SAP上的pdu收发
        binding(接口号，下层实体，sap号）
    """
    def __init__(self,dad=None):
        self.dev = dad
        self.sap_tab = {}      # 字典结构，SAP绑定参数，saps={sap号:(上层Entity，接口号)}
        self.intf_tab = {}     #字典结构，intf接口参数，intf={接口号：(下层Entity，sap号）}

    def __repr__(self):
        return self.name
    
    def parent(self,dad=None):
        if dad == None:
            return self.dev
        else:
            self.dev = dad

    def send(self, intf_no, packet, dst=None,src=None):
        """从intf_no向dst发出分组"""
        if intf_no in self.intf_tab:
            peer=self.intf_tab[intf_no][0]
            sap=self.intf_tab[intf_no][1]
            Dispatch(0.0, peer.handle_req, (sap, packet,dst,src))
        else:
            print("send(%s,..." % intf_no)
            del packet
            raise RuntimeError("错误：接口未绑定")

    def deliver(self, sap_no, packet, dst=None,src=None):
        if sap_no in self.sap_tab:
            peer = self.sap_tab[sap_no][0]
            intf = self.sap_tab[sap_no][1]
            Dispatch(0.0, peer.handle_rx, (intf, packet,dst,src))
        else:
            del packet
            raise RuntimeError("错误：服务未绑定")
        
    def handle_rx(self, intf_no, packet,dst=None,src=None ):
        """来自intf_no的分组，继承实体应重载该函数"""
        pass

    def handle_req(self, sap_no, packet, dst=None, src=None):
        """来自上层实体的发送请求,若src为None，则用实体的地址替代"""
        pass

    def binding(self,intf,entity,sap):
        """用自己的intf与下层实体的sap绑定
           在自己的intf表中注册下层实体的sap，在下层实体中sap号上注册自己的intf"""
        self.intf_tab[intf]=(entity,sap)
        entity.register(sap,self,intf)

    def register(self, sap, entity, intf):
        self.sap_tab[sap] = (entity, intf)
