from problems.majority_element import majority_element


def test_example_1():
    assert majority_element([3, 2, 3]) == 3


def test_example_2():
    assert majority_element([2, 2, 1, 1, 1, 2, 2]) == 2


def test_single_element():
    assert majority_element([1]) == 1


def test_all_same():
    assert majority_element([5, 5, 5, 5]) == 5


def test_majority_at_end():
    assert majority_element([1, 1, 2, 2, 2]) == 2
