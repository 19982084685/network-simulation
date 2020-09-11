from channel.link import *
from device.Host1 import *
from device.switch4 import *

Title = \
    """swcir 仿真"""
N = 4
x = ['a', 'b', 'c', 'd']
for j in x:
    locals()['switch_' + j] = CSwitch.create("switch_" + j)
    for i in range(1, 3):
        h = j + "h" + str(i)
        devh = CHost1.create(h)
        my = (locals()['switch_' + j]).__dict__["self.mym" + str(i)]
        li = j + "l" + str(i)
        locals()[li] = CLink(li, 0.1)
        locals()[li].LinkTo(devh.mac)
        locals()[li].LinkTo(my)
for m in range(0, 4):
    n = (m + 1) % 4
    my1 = locals()["switch_" + x[m]].__dict__["self.mym3"]
    my2 = locals()["switch_" + x[n]].__dict__["self.mym0"]
    li = 'Sl' + str(m)
    locals()[li] = CLink(li, 0.1)
    locals()[li].LinkTo(my1)
    locals()[li].LinkTo(my2)

robot.start()
import code

code.interact(local=locals(), banner=Title)
