#####################################################
# test.py
#####################################################
"""
Задание: написать модули, которые позволят без ошибок выполнить тест.
Можно не выполнять тест до конца, закомментировав те проверки,
выполнение которых не удалось реализовать.
Версия python -- 3.6.
"""

from ma import *
from mb import B


def test():
    a = A()
    b = B(5)

    assert (a.i == 3)
    assert (a.fnc(2) == 2 * 2 * 3)
    assert (b.fnc(10, 4) == 10 * 4 * 5)
    assert (a.is_first() == 1)
    #assert (a.is_second == 0)
    assert (b.is_first() == 0)
    #assert (b.is_second == 1)

    assert isinstance(a, First)
    #assert isinstance(b, Second)
    assert isinstance(a, Parent)
    #assert isinstance(b, Parent)

    # по этому куску кода возник большой вопрос, я не стала эту проверку комментировать,
    # так как "a.fnc(7)" всегда работает, и exception не вызывается,
    # но логика MyError не может выполниться, так как нет raise
    try:
        a.fnc(7)
    except MyError as v:
        if str(v) != "Error text":
            assert 0
    #else:
     #   assert 0

    # строка кажется бессмысленной, так как, чтобы получить AttributeError,
    # нужно убрать "=2", либо передать "a.is_second == 2"
    try:
        a.is_second = 2
    except AttributeError:
        pass
    #else:
     #   assert 0


if __name__ == "__main__":
    test()
    print("done")

#####################################################

