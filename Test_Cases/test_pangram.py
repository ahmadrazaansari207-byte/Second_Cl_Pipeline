import importlib

module = importlib.import_module("Codes.pangram")


def test_pangram_true():
    assert module.pangram("The quick brown fox jumps over the lazy dog") is True


def test_pangram_false():
    assert module.pangram("Hello World") is False


def test_uppercase_pangram():
    assert module.pangram("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG") is True


def test_empty_sentence():
    assert module.pangram("") is False


def test_alphabet():
    assert module.pangram("abcdefghijklmnopqrstuvwxyz") is True



#python -m pytest Test_Cases\test_pangram.py