def group_anagrams(strs: list[str]) -> list[list[str]]:
    """
    LeetCode 49 - Group Anagrams (Medium)

    Given an array of strings `strs`, group the anagrams together. You can
    return the answer in any order (the tests sort groups/elements before
    comparing, so exact ordering doesn't matter).

    Example:
        strs = ["eat","tea","tan","ate","nat","bat"]
        -> [["eat","tea","ate"], ["tan","nat"], ["bat"]]   (any order)

    Constraints:
        - 1 <= len(strs) <= 10^4
        - strs[i] consists of lowercase English letters.

    Hint: group strings by a canonical key. Two natural choices:
      - sorted(word) as the key (uses `sorted`, which can take a `key=lambda`
        for other problems too)
      - a dict mapping key -> list of original words
    """
    raise NotImplementedError
