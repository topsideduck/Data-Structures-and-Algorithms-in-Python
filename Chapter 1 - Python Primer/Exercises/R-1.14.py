"""
Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd.
"""


def odd_product_pair(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if (lst[i] * lst[j]) % 2 == 1:
                return True

    return False


if __name__ == '__main__':
    print(odd_product_pair([31, 115, 4488, 982, 762]))
