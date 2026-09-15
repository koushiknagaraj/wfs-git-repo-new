from problems.queue_using_stacks import MyQueue


def test_leetcode_example():
    q = MyQueue()
    q.push(1)
    q.push(2)
    assert q.peek() == 1
    assert q.pop() == 1
    assert q.empty() is False


def test_fifo_order_preserved():
    q = MyQueue()
    q.push(1)
    q.push(2)
    q.push(3)
    assert q.pop() == 1
    assert q.pop() == 2
    assert q.pop() == 3
    assert q.empty() is True


def test_interleaved_push_pop():
    q = MyQueue()
    q.push(1)
    q.push(2)
    assert q.pop() == 1
    q.push(3)
    assert q.pop() == 2
    assert q.pop() == 3
    assert q.empty() is True


def test_empty_after_all_popped():
    q = MyQueue()
    q.push(9)
    q.pop()
    assert q.empty() is True
