class Parent:
    pass


class First(Parent):
    pass


class Second(Parent):
    pass


class A(First):
    i = 3

    @staticmethod
    def fnc(w):
        return w * 6

    @staticmethod
    def is_first():
        return 1

    #@staticmethod
    #def is_second():
        #return 0


class MyError(Exception):
    def __init__(self, text):
        self.text = text
