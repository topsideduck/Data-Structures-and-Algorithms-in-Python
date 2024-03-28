"""
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.
"""


def sum_of_odd_squares(n):
    return sum(i ** 2 for i in range(1, n) if i % 2 == 1)


if __name__ == '__main__':
    print(sum_of_odd_squares(5))
