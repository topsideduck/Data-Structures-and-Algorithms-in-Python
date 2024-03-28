"""
Write a short Python program that takes two arrays a and b of length n
storing int values, and returns the dot product of a and b. That is, it returns
an array c of length n such that c[i] = a[i] · b[i], for i = 0, . . . , n − 1
"""


def dot_product(a, b):
    return [a[i] * b[i] for i in range(len(a))]


if __name__ == '__main__':
    print(dot_product(
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10]
    ))
