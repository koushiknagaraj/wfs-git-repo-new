from problems.single_number import single_number


def test_example_1():
    assert single_number([2, 2, 1]) == 1


def test_example_2():
    assert single_number([4, 1, 2, 1, 2]) == 4


def test_single_element():
    assert single_number([7]) == 7


def test_negative_numbers():
    assert single_number([-1, -1, -2]) == -2


def test_larger_list():
    assert single_number([1, 2, 3, 2, 1, 4, 3]) == 4
