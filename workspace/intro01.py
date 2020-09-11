from channel.link import *
from module.App01 import *

Title="""入门仿真：信道验证演示小程序"""
link = CLink("chn",loss=0.1,delay=0.01)  #链路实例
s1 = CApp01("app1")         #生成站点实例
s2 = CApp01("app2")         #生成站点实例
link.LinkTo(s1)            #链路link连接到站点st1
link.LinkTo(s2)            #链路link连接到站点st2

def go():
    s1.tx("站点%s发送出来的信息" % s1,15,1.2)
    s2.tx("我是s2,明晚出来哈皮，行吗？",16,0.9)

robot.start()
import code
code.interact(local=locals(), banner=Title)
