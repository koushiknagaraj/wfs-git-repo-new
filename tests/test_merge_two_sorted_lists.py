from problems.merge_two_sorted_lists import (
    linked_to_list,
    list_to_linked,
    merge_two_lists,
)


def run(a, b):
    result = merge_two_lists(list_to_linked(a), list_to_linked(b))
    return linked_to_list(result)


def test_classic_example():
    assert run([1, 2, 4], [1, 3, 4]) == [1, 1, 2, 3, 4, 4]


def test_both_empty():
    assert run([], []) == []


def test_one_empty():
    assert run([], [0]) == [0]


def test_disjoint_ranges():
    assert run([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]


def test_interleaved():
    assert run([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]


def test_duplicates_across_lists():
    assert run([1, 1, 1], [1, 1]) == [1, 1, 1, 1, 1]
