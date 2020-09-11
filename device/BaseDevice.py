from core.simapi import *

def getdevbyname(name):
    return sys.modules['__main__'].__dict__[name]

def CreateDevice(_name,_kind,*args,**kw):
    """创建_kind类型的设备，_kind 为Node的派生类，_name为设备名(如h1)，
    其余的参数将传递给新设备的__init__()函数
    返回值=设备对象
    """
    e = _kind(_name,*args,**kw)
    setattr(e,'name',_name)
    sys.modules['__main__'].__dict__[_name]=e
    return e

class CBaseDevice(object):
    """所有节点设备的基类(主机、交换机、路由器等)"""
    @classmethod
    def create(cls,name,*args,**kw):
        """类的批量创建机制，替代普通创建类对象的方法"""
        return CreateDevice(name,cls,*args,**kw)

class CBaseHost(CBaseDevice):
    """所有Host类的都从此类派生"""
    def __init__(self):
        self.type = "Host"
    def __repr__(self):
        return "Host"
    def addr(self):
        pass

class CBaseSwitch(CBaseDevice):
    """所有switch类都从此类派生"""
    def __repr__(self):
        return 'Switch'

class CBaseRouter(CBaseDevice):
    """所有router类都从该类派生"""
    def __repr__(self):
        return 'Router'
