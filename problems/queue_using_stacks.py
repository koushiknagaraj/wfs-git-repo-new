class MyQueue:
    """
    LeetCode 232 - Implement Queue using Stacks (Easy)

    Implement a first-in-first-out (FIFO) queue using only two stacks (plain
    Python lists used with append/pop). The queue must support:

        push(x)     -> push element x to the back of the queue
        pop()  -> int  -> removes and returns the element from the front
        peek() -> int  -> returns the element at the front
        empty() -> bool -> returns True if the queue is empty

    Example:
        q = MyQueue()
        q.push(1)
        q.push(2)
        q.peek()   -> 1
        q.pop()    -> 1
        q.empty()  -> False

    Constraints:
        - 1 <= x <= 9
        - pop and peek are only called when the queue is non-empty.

    Hint: use two internal lists, `in_stack` and `out_stack`. Push always
    goes to `in_stack`. When `out_stack` is empty and you need to pop/peek,
    transfer everything from `in_stack` to `out_stack` (this reverses order,
    turning stack order into queue order), one element per loop iteration.
    """

    def __init__(self):
        raise NotImplementedError

    def push(self, x: int) -> None:
        raise NotImplementedError

    def pop(self) -> int:
        raise NotImplementedError

    def peek(self) -> int:
        raise NotImplementedError

    def empty(self) -> bool:
        raise NotImplementedError
