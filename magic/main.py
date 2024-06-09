def addition(a, b):
    return a + b


def invert_string(s):
    return s[::-1]


def fibonacci(n):
    """
    Calculate the nth Fibonacci number.
    The first Fibonacci numers are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = a + b, b
    return a


if __name__ == "__main__":
    print("this is the main module")
