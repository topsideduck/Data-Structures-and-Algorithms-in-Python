"""
Write a short program that takes as input three integers, a, b, and c,
 from the console and determines if they can be used in a correct
 arithmetic formula (in the given order), like “a+b = c,” “a = b−c,” or “a∗b = c.”
"""


def determine(a, b, c):
    if a + b == c:
        return "Satisfies summation!"

    elif a == b - c:
        return "Satisfies difference!"

    elif a * b == c:
        return "Satisfies product!"

    else:
        return "Does not satisfy any criteria."


if __name__ == '__main__':
    a = int(input("number 1: "))
    b = int(input("number 2: "))
    c = int(input("number 3: "))

    print(determine(a, b, c))
