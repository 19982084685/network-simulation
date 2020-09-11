from channel.link import *
from device.Host1a import  *
Title=\
"""Host1a to Host1a 传输实验测试
   发送数据：h1.app1/2.tx(对方主机名 or 主机地址，字符串）
"""
link = CLink("chn",loss=0.1,delay=0.02)
CHost1a.create("h1",addr=1111)
h1=getdevbyname("h1")
h2 = CHost1a("h2",addr=2222)
link.LinkTo(h1.mac)
link.LinkTo(h2.mac)

print("h1=%d" % h1.mac.addr())
print("h2=%d" % h2.mac.addr())

robot.start()
import code
code.interact(local=locals(), banner=Title)