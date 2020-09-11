from channel.link import *
from device.Host2 import *
from device.switch4 import *
from device.Router import *
from module.shutdown import *
import code

Title = \
    """ro4WAN 仿真"""
N = 4
Router_1 = CRouter.create("Router_1")

x = ['a', 'b', 'c', 'd']
y = 10100
z = 0
for i in x:
    locals()['switch_' + i] = CSwitch.create(('switch_' + i), y)
    for j in range(0, 3):
        h = i + 'h' + str(j)
        devh = CHost2.create(h)
        ip = y + j + 1
        devh.setip(1, ip)
        devh.hNP.addFIB(0, y + 4, 1)
        my = (locals()['switch_' + i]).__dict__["self.mym" + str(j)]
        li = i + 'l' + str(j)
        locals()[li] = CLink(li, 0.1)
        locals()[li].LinkTo(devh.mac)
        locals()[li].LinkTo(my)
    my1 = Router_1.__dict__["self.mym" + str(z)]
    my2 = locals()["switch_" + i].__dict__["self.mym3"]
    li = "RSl" + str(z)
    locals()[li] = CLink(li, 0.1)
    locals()[li].LinkTo(my1)
    locals()[li].LinkTo(my2)
    z += 1
    y += 100
seq = [10104, 10204, 10304, 10404]
Router_1.setip(seq)


def setFIB():
    subl = [10100, 10200, 10300, 10400]
    n = 0
    for m in subl:
        Router_1.rNP.addFIB(m, m, n)
        n += 1


setFIB()
robot.start()
code.interact(local=locals(), banner=Title)
