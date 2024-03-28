"""
Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct).
"""


def distinct_elements(lst):
    return len(set(lst)) == len(lst)


if __name__ == '__main__':
    print(distinct_elements([1, 4, 554, 382]))
    print(distinct_elements([12, 9872, 12, 76]))
