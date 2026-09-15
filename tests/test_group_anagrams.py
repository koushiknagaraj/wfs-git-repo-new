from problems.group_anagrams import group_anagrams


def normalize(groups):
    return sorted(sorted(group) for group in groups)


def test_classic_example():
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    expected = [["ate", "eat", "tea"], ["nat", "tan"], ["bat"]]
    assert normalize(result) == normalize(expected)


def test_empty_string():
    result = group_anagrams([""])
    assert normalize(result) == normalize([[""]])


def test_single_word():
    result = group_anagrams(["a"])
    assert normalize(result) == normalize([["a"]])


def test_no_anagrams():
    result = group_anagrams(["abc", "def", "ghi"])
    assert normalize(result) == normalize([["abc"], ["def"], ["ghi"]])


def test_all_same_word():
    result = group_anagrams(["abc", "abc", "abc"])
    assert normalize(result) == normalize([["abc", "abc", "abc"]])
