"""
The birthday paradox says that the probability that two people in a room
will have the same birthday is more than half, provided n, the number of
people in the room, is more than 23. This property is not really a paradox,
but many people find it surprising. Design a Python program that can test
this paradox by a series of experiments on randomly generated birthdays,
which test this paradox for n = 5,10,15,20,...,100.
"""

import random

if __name__ == '__main__':
    for n in range(5, 101, 5):
        birthdays = [(random.randint(0, 31), random.randint(1, 12)) for _ in range(n)]

        if len(set(birthdays)) != len(birthdays):
            print(f"Two or more people have the same birthday for n = {n}")

