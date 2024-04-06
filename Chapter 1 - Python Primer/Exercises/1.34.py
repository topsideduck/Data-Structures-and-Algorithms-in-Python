"""
A common punishment for school children is to write out a sentence multiple
times. Write a Python stand-alone program that will write out the following
sentence one hundred times: “I will never spam my friends again.” Your program
should number each of the sentences and it should make eight different
random-looking typos.
"""


import random
import string


if __name__ == '__main__':
    char_list = [i for i in "I will never spam my friends again"]
    random_sentence_numbers = random.choices(range(0, 101), k=8)

    for i in range(100):
        if i in random_sentence_numbers:
            random_character_position = random.randint(0, len(char_list) - 1)
            char_list_copy = char_list.copy()
            char_list_copy[random_character_position] = random.choice(string.ascii_letters)
            print("".join(char_list_copy))

        else:
            print("".join(char_list))
