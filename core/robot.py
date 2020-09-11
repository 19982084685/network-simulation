import sys
import queue
import threading
import time

class CRobot(object):
    """事件调度器"""
    def  __init__(self):
        self.queue = queue.PriorityQueue()   # 创建事件队列，以时间优先级队列，时间越小越在前
        self._count = 0
        self.realtime = 1

    def doLater(_self, _delay, _method, *_args, **_kw):
        t = vTime.get()                             #  当前仿真时间
        _self.queue.put((t+_delay, _self._count, _method, _args, _kw))    # 按事件发生时间‘近-远’优先级排队
        _self._count += 1

    def start(self):
        self._thread = threading.Thread(target=self.run)
        self._thread.daemon = True
        self._thread.start()

    def run(self):
        while True:
            e = self.queue.get(True, None)
            t1 = e[0]  # 事件发生时间=当前仿真时间+延迟
            if self.realtime != 0:
                t0 = vTime.get()                # 当前仿真时间
                time.sleep(t1-t0)
            vTime.set(t1)
            e[2](*e[3], **e[4])
            self.queue.task_done()
    def RealTime(self,v):
        self.realtime = v

class CVtime(object):
    """虚拟仿真时间
    set(时间）：设置当前仿真时间
    get(): 取当前仿真时间 """
    def __init__(self):
        self.vtime = 0.0
    def get(self):
        return self.vtime
    def set(self,time):
        self.vtime = time

vTime = CVtime()
robot = CRobot()

