class ListNode:
    """A node in a singly linked list, as used by LeetCode linked-list problems."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val})"


def list_to_linked(values: list[int]) -> ListNode | None:
    """Helper (already implemented): build a linked list from a Python list."""
    head = None
    tail = None
    for v in values:
        node = ListNode(v)
        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node
    return head


def linked_to_list(node: ListNode | None) -> list[int]:
    """Helper (already implemented): convert a linked list back to a Python list."""
    values = []
    while node is not None:
        values.append(node.val)
        node = node.next
    return values


def merge_two_lists(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    """
    LeetCode 21 - Merge Two Sorted Lists (Easy)

    You are given the heads of two sorted linked lists `list1` and `list2`.
    Merge the two lists into one sorted linked list by splicing together the
    nodes of the two lists, and return the head of the merged list.

    Example:
        list1 = [1,2,4], list2 = [1,3,4]
        -> [1,1,2,3,4,4]
        list1 = [], list2 = []
        -> []
        list1 = [], list2 = [0]
        -> [0]

    Constraints:
        - The number of nodes in both lists is in the range [0, 50].
        - -100 <= Node.val <= 100
        - Both list1 and list2 are sorted in non-decreasing order.

    Hint: use a dummy head node and a `tail` pointer you advance in a loop,
    always attaching the smaller of the two current nodes.
    """
    raise NotImplementedError
