import importlib

module = importlib.import_module("Codes.count_words")


def test_normal_sentence():
    assert module.count_words("I love Python programming") == 4


def test_single_word():
    assert module.count_words("Python") == 1


def test_empty_sentence():
    assert module.count_words("") == 0


def test_extra_spaces():
    assert module.count_words("I   love   Python") == 3


def test_sentence_with_numbers():
    assert module.count_words("I have 2 books") == 4



#python -m pytest Test_Cases\test_count_words.py 