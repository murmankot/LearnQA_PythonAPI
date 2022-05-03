from ma import *


class B(Second):
    def __init__(self, o):
        self.o = o

    def fnc(self, r, t):
        return r * t * self.o

    @staticmethod
    def is_first():
        return 0
