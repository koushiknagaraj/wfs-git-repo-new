class MinStack:
    """
    LeetCode 155 - Min Stack (Medium)

    Design a stack that supports push, pop, top, and retrieving the minimum
    element in constant time O(1) for every operation.

    Methods to implement:
        __init__(self)          -> initialize the stack
        push(self, val: int)    -> push val onto the stack
        pop(self)               -> remove the element on top of the stack
        top(self) -> int        -> get the top element
        get_min(self) -> int    -> retrieve the minimum element in the stack

    Example:
        s = MinStack()
        s.push(-2)
        s.push(0)
        s.push(-3)
        s.get_min()  -> -3
        s.pop()
        s.top()      -> 0
        s.get_min()  -> -2

    Constraints:
        - Methods are always called on a non-empty stack when required
          (pop/top/get_min are never called on an empty stack in the tests).

    Hint: keep a second internal list that tracks the running minimum
    alongside the main stack, so get_min() is a simple lookup.
    """

    def __init__(self):
        raise NotImplementedError

    def push(self, val: int) -> None:
        raise NotImplementedError

    def pop(self) -> None:
        raise NotImplementedError

    def top(self) -> int:
        raise NotImplementedError

    def get_min(self) -> int:
        raise NotImplementedError
