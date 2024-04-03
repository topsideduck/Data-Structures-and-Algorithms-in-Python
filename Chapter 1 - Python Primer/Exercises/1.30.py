"""
Write a Python program that can take a positive integer greater than 2 as
input and write out the number of times one must repeatedly divide this number
by 2 before getting a value less than 2.
"""


def division(num):
    i = 1

    while True:
        if 2 ** i < num:
            i += 1
            continue

        elif 2 ** i == num:
            return i

        else:
            return i - 1


if __name__ == '__main__':
    print(division(20))
