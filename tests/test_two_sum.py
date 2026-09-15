from problems.two_sum import two_sum


def check(nums, target, expected_sum):
    result = two_sum(nums, target)
    assert isinstance(result, list) and len(result) == 2
    i, j = result
    assert i != j
    assert nums[i] + nums[j] == expected_sum


def test_example_1():
    check([2, 7, 11, 15], 9, 9)


def test_example_2():
    check([3, 2, 4], 6, 6)


def test_duplicate_values():
    check([3, 3], 6, 6)


def test_negative_numbers():
    check([-1, -2, -3, -4, -5], -8, -8)


def test_answer_at_the_end():
    check([1, 2, 3, 4, 5, 9], 14, 14)


def test_returns_indices_not_values():
    result = two_sum([5, 75, 25], 100)
    assert sorted(result) == [1, 2]
