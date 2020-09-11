from channel.link import *
from device.Host2 import *
from device.switch4 import *
from device.Router import *
import code

Title = \
    """rodWAN 仿真"""
N = 4
x = ['A', 'D']
y = [10100, 10400]
for m in range(0, 2):
    i = x[m]
    j = y[m]
    locals()['switch_' + i] = CSwitch.create(('switch_' + i), y)
    for k in range(1, 3):
        h = i + 'h' + str(k)
        devh = CHost2.create(h)
        devh.setip(1, j + k + 1)
        devh.hNP.addFIB(0, y[m] + 1, 1)
        my = (locals()['switch_' + i]).__dict__["self.mym" + str(k)]
        li = i + 'l' + str(k)
        locals()[li] = CLink(li, 0.1)
        locals()[li].LinkTo(devh.mac)
        locals()[li].LinkTo(my)
    my0 = (locals()['switch_' + i]).__dict__["self.mym0"]
    my3 = (locals()['switch_' + i]).__dict__["self.mym3"]
    li0 = i + 'Rl0'
    li3 = i + 'Rl3'
    locals()[li0] = CLink(li0, 0.1)
    locals()[li0].LinkTo(my0)
    locals()[li3] = CLink(li3, 0.1)
    locals()[li3].LinkTo(my3)
x = ['B', 'C']
y = [10200, 10300]
for m in range(0, 2):
    i = x[m]
    j = y[m]
    for n in range(1, 3):
        locals()['switch_' + i + str(n)] = CSwitch.create(('switch_' + i + str(n)), y)
        for k in range(1, 3):
            h = i + str(n) + 'h' + str(k)
            if h == 'C1h2':
                my = (locals()['switch_' + i + str(n)]).__dict__["self.mym" + str(k)]
                li = i + str(n) + 'l' + str(k)
                locals()[li] = CLink(li, 0.1)
                locals()[li].LinkTo(my)
                continue
            devh = CHost2.create(h)
            if n == 1:
                devh.setip(1, j + k + 1)
            else:
                devh.setip(1, j + k + 4)
            devh.hNP.addFIB(0, y[m] + 1, 1)
            my = (locals()['switch_' + i + str(n)]).__dict__["self.mym" + str(k)]
            li = i + str(n) + 'l' + str(k)
            locals()[li] = CLink(li, 0.1)
            locals()[li].LinkTo(devh.mac)
            locals()[li].LinkTo(my)
    my0 = (locals()['switch_' + i + '1']).__dict__["self.mym0"]
    my3 = (locals()['switch_' + i + '2']).__dict__["self.mym3"]
    li0 = i + 'Rl0'
    li3 = i + 'Rl3'
    locals()[li0] = CLink(li0, 0.1)
    locals()[li0].LinkTo(my0)
    locals()[li3] = CLink(li3, 0.1)
    locals()[li3].LinkTo(my3)
    mys1 = (locals()['switch_' + i + '1']).__dict__["self.mym3"]
    mys2 = (locals()['switch_' + i + '2']).__dict__["self.mym0"]
    lis = i + 'Rls'
    locals()[lis] = CLink(lis, 0.1)
    locals()[lis].LinkTo(mys1)
    locals()[lis].LinkTo(mys2)

Router_A = CRouter.create("Router_A")
my = Router_A.__dict__["self.mym0"]
locals()['ARl0'].LinkTo(my)
my=Router_A.__dict__["self.mym1"]
locals()['BRl0'].LinkTo(my)
seq = [10101, 10201, 0, 0]
Router_A.setip(seq)

Router_B = CRouter.create("Router_B")
my=Router_B.__dict__["self.mym0"]
locals()['BRl3'].LinkTo(my)
my=Router_B.__dict__["self.mym1"]
locals()['C1l2'].LinkTo(my)
my=Router_B.__dict__["self.mym2"]
locals()['DRl0'].LinkTo(my)
seq = [10204, 10303, 10401, 0]
Router_B.setip(seq)

Router_C = CRouter.create("Router_C")
my=Router_C.__dict__["self.mym0"]
locals()['ARl3'].LinkTo(my)
my=Router_C.__dict__["self.mym1"]
locals()['CRl0'].LinkTo(my)
seq = [10104, 10301, 0, 0]
Router_C.setip(seq)

Router_D = CRouter.create("Router_D")
my=Router_D.__dict__["self.mym0"]
locals()['CRl3'].LinkTo(my)
my=Router_D.__dict__["self.mym1"]
locals()['DRl3'].LinkTo(my)


robot.start()
code.interact(local=locals(), banner=Title)