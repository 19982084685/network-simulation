


class CFirst(object):
    def __init__(self,nmstr):
        self.nm=nmstr
        self.x1=0
        self.x2="hello"

    def name(self):
        return self.nm

    def rmb(self,value=None):
        if value != None:
            self.x1 = value
        else:
            return self.x1

    def hi(self):
        return self.x2

class CSecond(CFirst):
    def __init__(self, nmstr):
        super().__init__(nmstr)
        self.counter = 0
        self.msg="there is mail for you"

    def ask(self):
        return self.msg
    def dollar(self,value=None):
        if value != None:
            self.x1 = value*6.5
        else:
            return  self.x1/6.5