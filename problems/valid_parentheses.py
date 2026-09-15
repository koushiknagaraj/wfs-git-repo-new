def is_valid(s: str) -> bool:
    """
    LeetCode 20 - Valid Parentheses (Easy)

    Given a string `s` containing just the characters '(', ')', '{', '}',
    '[' and ']', determine if the input string is valid. It's valid if:
      - Every open bracket is closed by the same type of bracket.
      - Open brackets are closed in the correct order.

    Example:
        s = "()[]{}" -> True
        s = "(]"      -> False
        s = "([)]"    -> False
        s = "{[]}"    -> True

    Constraints:
        - 1 <= len(s) <= 10^4
        - s consists only of the characters '()[]{}'.

    Hint: use a Python list as a stack (append / pop). A dict mapping closing
    -> opening bracket keeps the check clean.
    """
    raise NotImplementedError
