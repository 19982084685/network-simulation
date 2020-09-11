from channel.link import *
from device.Host1 import *
from device.switch8 import *
from module.shutdown import *

Title = \
    """sw1LAN 仿真"""
N = 8
switch = CSwitch.create("switch8", addr=1111)
for i in range(0, 7):
    h = "h" + str(i)
    CHost1.create(h)
    devh = getdevbyname(h)
    my = switch.__dict__["self.mym" + str(i)]
    li = "l" + str(i)
    locals()["link" + str(i)] = CLink(li,0.1)
    locals()["link" + str(i)].LinkTo(devh.mac)
    locals()["link" + str(i)].LinkTo(my)
for i in range(7, N):
    locals()["sh" + str(i)] = Shut()
    my = switch.__dict__["self.mym" + str(i)]
    my.binding(0, locals()["sh" + str(i)], 0)


def printtab():
    mytab = switch.engine.tab()
    print(mytab)


robot.start()
import code

code.interact(local=locals(), banner=Title)
