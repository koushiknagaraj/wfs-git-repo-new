from problems.reverse_integer import reverse


def test_positive():
    assert reverse(123) == 321


def test_negative():
    assert reverse(-123) == -321


def test_trailing_zero():
    assert reverse(120) == 21


def test_zero():
    assert reverse(0) == 0


def test_overflow_returns_zero():
    assert reverse(1534236469) == 0


def test_negative_overflow_returns_zero():
    assert reverse(-2147483648) == 0


def test_single_digit():
    assert reverse(5) == 5
