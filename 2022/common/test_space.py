from .space import Space
from common.space import line


def test_dump():
    s = Space(False, to_str=lambda v: "#" if v else ".")
    s[(0, 0)] = True
    s[(1, 0)] = True
    s[(1, 1)] = True
    s[(0, 2)] = True
    s[(2, 2)] = True
    assert list(range(3)) == list(s.range(0))
    assert list(range(3)) == list(s.range(1))
    assert (
        str(s)
        == """##.
.#.
#.#
"""
    )


def test_simple_line():
    assert [(10, 10)] == list(line((10, 10), (10, 10)))
    assert [(10, 10), (10, 11), (10, 12), (10, 13)] == list(line((10, 10), (10, 13)))
    assert [(10, 10), (11, 10), (12, 10), (13, 10)] == list(line((10, 10), (13, 10)))


def test_complex_line():
    start = (10, 20, 30)
    end = (11, 22, 35)
    actual = list(line(start, end))
    assert actual[-1] == end
    expected = [
        (10, 20, 30),
        (10, 20, 31),
        (10, 21, 32),
        (11, 21, 33),
        (11, 22, 34),
        (11, 22, 35),
    ]
    assert actual == expected
