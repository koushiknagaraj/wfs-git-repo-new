from problems.valid_parentheses import is_valid


def test_simple_valid():
    assert is_valid("()[]{}") is True


def test_mismatched_types():
    assert is_valid("(]") is False


def test_wrong_order():
    assert is_valid("([)]") is False


def test_nested_valid():
    assert is_valid("{[]}") is True


def test_single_open_bracket():
    assert is_valid("(") is False


def test_single_close_bracket():
    assert is_valid("]") is False


def test_empty_string():
    assert is_valid("") is True
