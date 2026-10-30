import importlib

module = importlib.import_module("Codes.rotate_string")


def test_rotate_by_two():
    assert module.rotate_string("python", 2) == "onpyth"


def test_rotate_by_one():
    assert module.rotate_string("hello", 1) == "ohell"


def test_rotate_by_zero():
    assert module.rotate_string("hello", 0) == "hello"


def test_empty_string():
    assert module.rotate_string("", 2) == ""


def test_negative_rotation():
    assert module.rotate_string("python", -2) == "thonpy"



#python -m pytest Test_Cases\test_rotate_string.py