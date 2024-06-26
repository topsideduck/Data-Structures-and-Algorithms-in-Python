"""
Write a short Python function, is_multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise.
"""


def is_multiple(n, m):
    return n % m == 0


if __name__ == '__main__':
    print(is_multiple(24, 3))
    print(is_multiple(44, 10))
