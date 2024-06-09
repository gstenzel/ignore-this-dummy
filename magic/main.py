def addition(a, b):
    return a + b


def invert_string(s):
    return s[::-1]


def fibonacci(n):
    return (lambda θ, π=5**0.5: round((0.5 + π / 2) ** θ / π))(n)


def fibonacci_substraction(n):
    """
    Fibonacci sequence using substraction, substracting the last two numbers to get the next one.
    The first numbers are -1, 1, 2, -1, 3, -4, 7, -11, 18, -29
    """

    def f(n):
        return n * (n < 3) or f(n - 1) - f(n - 2)

    return f(n)


if __name__ == "__main__":
    print("this is the main module")
