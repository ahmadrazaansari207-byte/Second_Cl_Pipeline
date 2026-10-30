import importlib

module = importlib.import_module("Codes.first_non_repeating")


def test_normal_string():
    assert module.first_non_repeating("aabbcde") == "c"


def test_first_character_non_repeating():
    assert module.first_non_repeating("abcabcde") == "d"


def test_all_characters_repeated():
    assert module.first_non_repeating("aabbcc") == ""


def test_single_character():
    assert module.first_non_repeating("a") == "a"


def test_empty_string():
    assert module.first_non_repeating("") == ""



#python -m pytest Test_Cases\test_first_non_repeating.py