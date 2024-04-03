"""
Write a short Python function that takes a string s, representing a sentence,
and returns a copy of the string with all punctuation removed. For example,
if given the string "Let s try, Mike.", this function would return "Lets try Mike".
"""

import string


def strip_punctuation(s):
    char_list = []

    for char in s:
        if char in string.punctuation:
            continue

        char_list.append(char)

    return "".join(char_list)


if __name__ == '__main__':
    print(strip_punctuation("Let's try, Mike."))
