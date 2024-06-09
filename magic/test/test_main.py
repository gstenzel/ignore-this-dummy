import magic


def test_addition():
    assert magic.main.addition(1, 2) == 3


def test_string_inversion_1():
    assert magic.main.invert_string("hello") == "olleh"


def test_string_inversion_2():
    assert magic.main.invert_string("Hello, World!") == "!dlroW ,olleH"


def test_fibonacci_1():
    assert magic.main.fibonacci(0) == 0
    assert magic.main.fibonacci(1) == 1


def test_fibonacci_2():
    assert magic.main.fibonacci(2) == 1
    assert magic.main.fibonacci(3) == 2
    assert magic.main.fibonacci(4) == 3


def test_fibonacci_substraction_1():
    assert magic.main.fibonacci_substraction(1) == 1
    assert magic.main.fibonacci_substraction(2) == 2


def test_fibonacci_substraction_2():
    assert magic.main.fibonacci_substraction(3) == -1
    assert magic.main.fibonacci_substraction(4) == 3
    assert magic.main.fibonacci_substraction(5) == -4
