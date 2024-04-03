"""
Write a short Python function that counts the number of vowels in a given
character string.
"""


def count_vowels(string: str):
    count = 0

    for char in string:
        if char.lower() in "aeiou":
            count += 1

    return count


if __name__ == '__main__':
    print(count_vowels("Hello, World!"))
