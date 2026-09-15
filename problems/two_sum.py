def two_sum(nums: list[int], target: int) -> list[int]:
    """
    LeetCode 1 - Two Sum (Easy)

    Given an array of integers `nums` and an integer `target`, return the
    indices of the two numbers that add up to `target`.

    You may assume each input has exactly one solution, and you may not use
    the same element twice. Return the indices in any order.

    Example:
        nums = [2, 7, 11, 15], target = 9
        -> [0, 1]   because nums[0] + nums[1] == 9

    Constraints:
        - 2 <= len(nums) <= 10^4
        - Only one valid answer exists.

    Target complexity: O(n) time using a dict (hash map).
    """
    seen = {}  # the "notebook": number -> position where we saw it
    for i, n in enumerate(nums):
        complement = target - n          # the number we'd need to pair with n
        if complement in seen:
            return [seen[complement], i]  # found a match: earlier position + current position
        seen[n] = i                       # not found yet, write n into the notebook
