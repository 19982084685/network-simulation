from channel.link import *
from device.Host1 import *
from device.switch8V import *
from module.shutdown import *

Title = \
    """sw1VLAN 仿真"""
N = 8
switch1 = CSwitch.create("switch8", addr=1111)
switch1.convlan(seq=['1', '2', '3'], val=[[0, 1, 2, 7], [3, 4, 5, 7], [6, 7]])
for i in range(0, 7):
    h = "ah" + str(i)
    CHost1.create(h)
    devh = getdevbyname(h)
    my = switch1.__dict__["self.mym" + str(i)]
    li = "1l" + str(i)
    locals()["1link" + str(i)] = CLink(li, 0.1)
    locals()["1link" + str(i)].LinkTo(devh.mac)
    locals()["1link" + str(i)].LinkTo(my)

switch2 = CSwitch.create("switch8", addr=2222)
switch2.convlan(seq=['1', '2', '3'], val=[[0, 1, 2, 7], [3, 4, 5, 7], [6, 7]])
for i in range(0, 7):
    h = "bh" + str(i)
    CHost1.create(h)
    devh = getdevbyname(h)
    my = switch2.__dict__["self.mym" + str(i)]
    li = "2l" + str(i)
    locals()["2link" + str(i)] = CLink(li, 0.1)
    locals()["2link" + str(i)].LinkTo(devh.mac)
    locals()["2link" + str(i)].LinkTo(my)

my1 = switch1.__dict__["self.mym" + str(7)]
my2 = switch2.__dict__["self.mym" + str(7)]
mytr = CLink("tr", 0.1)
mytr.LinkTo(my1)
mytr.LinkTo(my2)


def printtab(n=1):
    mytab = globals()["switch" + str(n)].engine.tab()
    print(mytab)


robot.start()
import code

code.interact(local=locals(), banner=Title)
