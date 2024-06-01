import magic


def test_addition():
    assert magic.main.addition(1, 2) == 3


def test_string_inversion_1():
    assert magic.main.invert_string("hello") == "olleh"


def test_string_inversion_2():
    assert magic.main.invert_string("Hello, World!") == "!dlroW ,olleH"
