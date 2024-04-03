"""
Write a Python program that outputs all possible strings formed by using the
characters 'c' , 'a' , 't' , 'd' , 'o' ,and 'g' exactly once.
"""

import random


def factorial(n):
    product = 1

    for i in range(2, n + 1):
        product *= i

    return product


if __name__ == '__main__':
    char_list = ['c', 'a', 't', 'd', 'o', 'g']

    word_list = []

    while len(word_list) < factorial(len(char_list)):
        random.shuffle(char_list)

        word = "".join(char_list)

        if word not in word_list:
            word_list.append(word)

    print(word_list)
