from core.robot import *

def smprint(arg=()):
    print("%0.3f:" % vTime.get(), arg)

def Dispatch(delay,func,args=()):
    robot.doLater(delay,func,*args)

def realtime(v):
    robot.RealTime(v)

def simtime():
    return vTime.get()


def simulator(title):
    robot.start()
    import code
    code.interact(local=locals(), banner=title)