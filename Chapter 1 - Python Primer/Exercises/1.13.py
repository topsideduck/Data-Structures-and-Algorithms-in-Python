"""
Write a pseudocode description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing.
"""


def reverse(lst):
    return lst[::-1]


if __name__ == '__main__':
    print(reverse([41, 22, 83, 15]))
