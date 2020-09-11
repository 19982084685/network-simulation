from module.entity import *

class CApp0(CEntity):
    def __init__(self, appName, parent=None):
        super().__init__(parent)
        self.sCount = 0
        self.rCount = 0
        self.name = appName

    def tx(self,string):
        self.sCount += 1
        self.send(0,string)

    def handle_rx(self, intf_no, string, dst=None, src=None):
        self.rCount += 1
        smprint("[%s收到]%s" % (self.name,string))

    def stat(self):
        print("%s 统计：发送%d 接收%d" % (self.name,self.sCount,self.rCount))