"""
Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution.
"""


def minmax(data):
    data = sorted(data)
    return data[0], data[-1]


if __name__ == '__main__':
    print(minmax([3849, 324, 832947, 8923, 10103, 19, 1333, 456]))
