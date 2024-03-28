"""
Write a short Python function, is_even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.
"""


def is_even(k):
    return (-1) ** k == 1


if __name__ == '__main__':
    print(is_even(90))
    print(is_even(181))
