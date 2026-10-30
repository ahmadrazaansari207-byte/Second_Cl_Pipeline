import importlib

module = importlib.import_module("Codes.move_zeros")


def test_zeros_at_end():
    assert module.move_zeros([1, 0, 2, 0, 3]) == [1, 2, 3, 0, 0]


def test_no_zeros():
    assert module.move_zeros([1, 2, 3]) == [1, 2, 3]


def test_all_zeros():
    assert module.move_zeros([0, 0, 0]) == [0, 0, 0]


def test_empty_list():
    assert module.move_zeros([]) == []


def test_negative_numbers():
    assert module.move_zeros([0, -1, 2, 0, -3]) == [-1, 2, -3, 0, 0]



#python -m pytest Test_Cases\test_move_zeros.py