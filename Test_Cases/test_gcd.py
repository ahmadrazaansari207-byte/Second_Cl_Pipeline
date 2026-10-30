import importlib

module = importlib.import_module("Codes.gcd")


def test_common_divisor():
    assert module.gcd(12, 18) == 6


def test_coprime_numbers():
    assert module.gcd(7, 9) == 1


def test_same_numbers():
    assert module.gcd(5, 5) == 5


def test_zero():
    assert module.gcd(10, 0) == 10


def test_negative_numbers():
    assert module.gcd(-12, 18) == 6



#python -m pytest Test_Cases\test_gcd.py