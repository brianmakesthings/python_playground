def add(a, b):
    return a + b


class TestFunction:
    def test_add(self):
        assert add(1, 2) == 3

    def test_fails_to_add(self):
        assert add(1, 2) != 3

    def test_array_equality(self):
        assert set([1, 2, 3]) == set([1, 2, 4])
