from channel.link import *
from device.Host1 import *
from device.switch4V import *
from module.shutdown import *
import code

Title = \
    """sw6VLAN 仿真"""
N = 4
x = ['l', 'r']
y = ['a', 'c']
for i in x:
    for j in y:
        locals()['switch' + i + j] = CSwitch.create('switch' + i + j)
        for m in range(0, 2):
            h = i + j + str(m)
            devh1 = CHost1.create(h)
            my = (locals()['switch' + i + j]).__dict__["self.mym" + str(m)]
            li = i + j + 'l' + str(m)
            locals()[li] = CLink(li, 0.1)
            locals()[li].LinkTo(devh1.mac)
            locals()[li].LinkTo(my)
        sh = i + j + 'sh'
        locals()[sh] = Shut()
        my = (locals()['switch' + i + j]).__dict__["self.mym" + str(3)]
        my.binding(0, locals()[sh], 0)
    (locals()['switch' + i + 'a']).convlan(seq=['1', '2', '3'], val=[[0, 1, 2, 3], [2], [2]])
    (locals()['switch' + i + 'c']).convlan(seq=['1', '2', '3'], val=[[2], [2], [0, 1, 2, 3]])

    locals()['switch' + i + 'b'] = CSwitch.create('switch' + i + 'b')
    (locals()['switch' + i + 'b']).convlan(seq=['1', '2', '3'], val=[[0, 1, 3], [0, 1, 2, 3], [0, 1, 3]])
    h = i + 'b' + '2'
    devh2 = CHost1.create(h)
    my = (locals()['switch' + i + 'b']).__dict__['self.mym' + '2']
    li = i + 'bl' + '2'
    locals()[li] = CLink(li, 0.1)
    locals()[li].LinkTo(devh2.mac)
    locals()[li].LinkTo(my)
    for k in range(0, 2):
        my1 = (locals()['switch' + i + 'b']).__dict__["self.mym" + str(k)]
        my2 = (locals()['switch' + i + y[k]]).__dict__["self.mym" + '2']
        tr = i + 'tr' + str(k)
        locals()[tr] = CLink(tr, 0.1)
        (locals()[tr]).LinkTo(my1)
        (locals()[tr]).LinkTo(my2)

mytr = CLink('mytr', 0.1)
my1 = (locals()['switch' + 'lb']).__dict__["self.mym" + '3']
my2 = (locals()['switch' + 'rb']).__dict__["self.mym" + '3']
mytr.LinkTo(my1)
mytr.LinkTo(my2)

robot.start()
code.interact(local=locals(), banner=Title)
