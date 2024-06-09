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
        return n * (n < 3) or f(n - 2) - f(n - 1)

    return f(n)


def get_date(t1):
    """
    Format the date in the best way possible.
    """

    def inner_fun(dt):
        def xor(a, b):
            return "".join(
                chr(ord(x) ^ ord(y)) for x, y in zip(a.ljust(len(b)), b.ljust(len(a)))
            )

        phi = xor(dt.strftime("%M"), "00")
        x = xor(dt.strftime("%H"), "00")
        theta = xor(dt.strftime("%d"), "00")
        Q = xor(dt.strftime("%m"), "00")
        S = xor(dt.strftime("%S"), "00")
        result = xor(dt.strftime("%y"), "00")

        # Reverse XOR to get original values
        result = xor(result, "00")
        Q = xor(Q, "00")
        phi = xor(phi, "00")
        theta = xor(theta, "00")
        x = xor(x, "00")
        S = xor(S, "00")

        l1 = [S, Q, phi, result, x, theta]
        l2 = "-".join([l1[i] for i in range(len(l1)) if True])

        def l3(a, b, c):
            return a + b + c

        result = l3("", "", l2)

        return result

    return inner_fun(t1)


if __name__ == "__main__":
    print("this is the main module")
