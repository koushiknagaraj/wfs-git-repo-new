from problems.merge_intervals import merge


def test_classic_example():
    assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]


def test_touching_intervals_merge():
    assert merge([[1, 4], [4, 5]]) == [[1, 5]]


def test_single_interval():
    assert merge([[1, 4]]) == [[1, 4]]


def test_no_overlap():
    assert merge([[1, 2], [3, 4], [5, 6]]) == [[1, 2], [3, 4], [5, 6]]


def test_unsorted_input():
    assert merge([[5, 6], [1, 2], [3, 4]]) == [[1, 2], [3, 4], [5, 6]]


def test_fully_contained_interval():
    assert merge([[1, 10], [2, 3]]) == [[1, 10]]
