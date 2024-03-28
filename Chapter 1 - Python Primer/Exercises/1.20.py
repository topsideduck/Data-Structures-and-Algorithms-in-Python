"""
Python’s random module includes a function shuffle(data) that accepts a
list of elements and randomly reorders the elements so that each
possible order occurs with equal probability. The random module includes a
more basic function randint(a, b) that returns a uniformly random integer
from a to b (including both endpoints). Using only the randint function,
implement your own version of the shuffle function.
"""

import random


def shuffle(lst):
    temp_list = lst.copy()

    return [temp_list.pop(random.randint(0, i)) for i in range(len(temp_list) - 1, -1, -1)]


if __name__ == '__main__':
    print(shuffle([1, 2, 3, 4, 5]))
