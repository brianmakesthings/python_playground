import pytest


def add(a, b):
    return a + b


testdata = [
    [1, 2, 3],
    [4, 5, 9],
    [-1, 4, 3],
]


class TestFunction:
    @pytest.mark.parametrize("a,b,expected", testdata)
    def test_add(self, a, b, expected):
        assert add(a, b) == expected

    def test_fails_to_add(self):
        assert add(1, 2) != 4
