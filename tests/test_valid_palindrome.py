from problems.valid_palindrome import is_palindrome


def test_classic_example():
    assert is_palindrome("A man, a plan, a canal: Panama") is True


def test_not_a_palindrome():
    assert is_palindrome("race a car") is False


def test_empty_after_filtering():
    assert is_palindrome(" ") is True


def test_single_character():
    assert is_palindrome("a") is True


def test_numbers_mixed_in():
    assert is_palindrome("0P") is False


def test_all_punctuation_removed():
    assert is_palindrome(".,") is True


def test_mixed_case_palindrome():
    assert is_palindrome("Was it a car or a cat I saw?") is True
