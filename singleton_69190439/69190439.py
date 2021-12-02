#!/usr/bin/python3

class SingleTon(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'temp'):
            cls.temp = super().__new__(cls, *args, **kwargs)

        return cls.temp

    def __init__(self):
        if not hasattr(self, 'title'):
            self.title = 5

a = SingleTon()
print(a.title)
a.title = 'lalala'
print(a.title)

b = SingleTon()
print(b.title)