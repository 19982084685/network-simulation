import sys
import queue
import threading
from core.robot import *
from core.simapi import *

class CTimer (object):
    """ It's a timer.
    You should just create this with api.create_timer()."""
    def __init__ (self):
        self.go = False
        pass
    def start(self, delay, tmfunc, args=(), kw=None):
        if kw is None:
            kw = {}
        self.go = True
        self.delay = delay
        self.func = tmfunc
        self.stopped = False
        self.args = list(args)
        self.kw = dict(kw)
        Dispatch(delay, self.ontime)

    def restart(self):
        if not self.go:
            raise RuntimeError("Timer not started")
        if not self.stopped:
            Dispatch(self.delay, self.ontime)
    def cancel (self):
        self.stopped = True

    def ontime (self):
        if self.stopped: return
        if self.func:
            self.func(*self.args,**self.kw)

class CTrace(object):
    def __init__(self):
        self.mac = 0
        self.net = 0
    pass

Trace = CTrace()
