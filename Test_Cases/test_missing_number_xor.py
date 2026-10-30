import importlib

module = importlib.import_module("Codes.missing_number_xor")


def test_missing_middle_number():
    assert module.missing_number_xor([1, 2, 4, 5]) == 3


def test_missing_first_number():
    assert module.missing_number_xor([2, 3, 4, 5]) == 1


def test_missing_last_number():
    assert module.missing_number_xor([1, 2, 3, 4]) == 5


def test_two_numbers():
    assert module.missing_number_xor([1]) == 2


def test_larger_list():
    assert module.missing_number_xor([1, 2, 3, 5, 6, 7]) == 4



#python -m pytest Test_Cases\test_missing_number.py