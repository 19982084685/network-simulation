from channel.link import *
from device.Host1 import *
from device.switch4 import *
from module.shutdown import *

Title = \
    """swnLAN 仿真"""
N = 4
switch_1 = CSwitch.create("switch_1", addr=1111)
for i in range(0, 3):
    h = "ah" + str(i)
    CHost1.create(h)
    devh = getdevbyname(h)
    my = switch_1.__dict__["self.mym" + str(i)]
    li = "1l" + str(i)
    locals()["1link" + str(i)] = CLink(li, 0.1)
    locals()["1link" + str(i)].LinkTo(devh.mac)
    locals()["1link" + str(i)].LinkTo(my)

switch_2 = CSwitch.create("switch_2", addr=2222)
for i in range(1, 3):
    h = "bh" + str(i)
    CHost1.create(h)
    devh = getdevbyname(h)
    my = switch_2.__dict__["self.mym" + str(i)]
    li = "2l" + str(i)
    locals()["2link" + str(i)] = CLink(li, 0.1)
    locals()["2link" + str(i)].LinkTo(devh.mac)
    locals()["2link" + str(i)].LinkTo(my)

switch_3 = CSwitch.create("switch_3", addr=3333)
for i in range(1, 3):
    h = "ch" + str(i)
    CHost1.create(h)
    devh = getdevbyname(h)
    my = switch_3.__dict__["self.mym" + str(i)]
    li = "3l" + str(i)
    locals()["3link" + str(i)] = CLink(li, 0.1)
    locals()["3link" + str(i)].LinkTo(devh.mac)
    locals()["3link" + str(i)].LinkTo(my)

switch_4 = CSwitch.create("switch_4", addr=4444)
for i in range(1, 4):
    h = "dh" + str(i)
    CHost1.create(h)
    devh = getdevbyname(h)
    my = switch_4.__dict__["self.mym" + str(i)]
    li = "4l" + str(i)
    locals()["4link" + str(i)] = CLink(li, 0.1)
    locals()["4link" + str(i)].LinkTo(devh.mac)
    locals()["4link" + str(i)].LinkTo(my)

for i in range(1, 4):
    my1 = locals()["switch_" + str(i)].__dict__["self.mym3"]
    my2 = locals()["switch_" + str(i + 1)].__dict__["self.mym0"]
    li = "Sl" + str(i)
    locals()["Slink" + str(i)] = CLink(li, 0.1)
    locals()["Slink" + str(i)].LinkTo(my1)
    locals()["Slink" + str(i)].LinkTo(my2)


def printtab(n):
    mytab = globals()["switch_" + str(n)].engine.tab()
    print(mytab)


robot.start()
import code

code.interact(local=locals(), banner=Title)
