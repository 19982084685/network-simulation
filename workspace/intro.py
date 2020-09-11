from channel.link import *
from module.App0 import *

Title="""入门仿真：信道验证演示小程序"""
link = CLink("chn",loss=0.1,delay=0.01)  #链路实例
s1 = CApp0("s1")         #生成站点实例
s2 = CApp0("s2")         #生成站点实例
link.LinkTo(s1)            #链路link连接到站点st1
link.LinkTo(s2)            #链路link连接到站点st2

robot.start()
import code
code.interact(local=locals(), banner=Title)
