import importlib

module = importlib.import_module("Codes.most_frequent")


def test_normal_list():
    assert module.most_frequent([1, 2, 2, 3, 2, 4]) == 2


def test_single_element():
    assert module.most_frequent([5]) == 5


def test_all_elements_same():
    assert module.most_frequent([3, 3, 3]) == 3


def test_tie_returns_first_element():
    assert module.most_frequent([4, 4, 2, 2]) == 4


def test_empty_list():
    assert module.most_frequent([]) is None



#python -m pytest Test_Cases\test_most_frequent.py