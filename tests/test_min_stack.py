from problems.min_stack import MinStack


def test_leetcode_example():
    s = MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    assert s.get_min() == -3
    s.pop()
    assert s.top() == 0
    assert s.get_min() == -2


def test_single_element():
    s = MinStack()
    s.push(5)
    assert s.top() == 5
    assert s.get_min() == 5


def test_min_updates_after_pops():
    s = MinStack()
    for v in [3, 1, 4, 1, 5]:
        s.push(v)
    assert s.get_min() == 1
    s.pop()  # remove 5
    assert s.get_min() == 1
    s.pop()  # remove 1
    assert s.get_min() == 1
    s.pop()  # remove 4
    assert s.get_min() == 1
    s.pop()  # remove 1
    assert s.get_min() == 3


def test_duplicate_minimums():
    s = MinStack()
    s.push(0)
    s.push(0)
    assert s.get_min() == 0
    s.pop()
    assert s.get_min() == 0
