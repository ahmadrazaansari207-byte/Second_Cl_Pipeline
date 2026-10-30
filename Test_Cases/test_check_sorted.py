import importlib

module = importlib.import_module("Codes.check_sorted")


def test_sorted_list():
    assert module.check_sorted([1, 2, 3, 4, 5]) is True


def test_unsorted_list():
    assert module.check_sorted([1, 3, 2, 4, 5]) is False


def test_empty_list():
    assert module.check_sorted([]) is True


def test_single_element():
    assert module.check_sorted([5]) is True


def test_duplicate_elements():
    assert module.check_sorted([1, 2, 2, 3]) is True



#python -m pytest Test_Cases\test_check_sorted.py