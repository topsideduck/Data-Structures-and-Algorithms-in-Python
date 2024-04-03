"""
Write a Python program that outputs all possible strings formed by using the
characters 'c' , 'a' , 't' , 'd' , 'o' ,and 'g' exactly once.
"""


# Inefficient
#
# import random
#
#
# def factorial(n):
#     product = 1
#
#     for i in range(2, n + 1):
#         product *= i
#
#     return product
#
#
# if __name__ == '__main__':
#     char_list = ['c', 'a', 't', 'd', 'o', 'g']
#
#     word_list = []
#
#     while len(word_list) < factorial(len(char_list)):
#         random.shuffle(char_list)
#
#         word = "".join(char_list)
#
#         if word not in word_list:
#             word_list.append(word)
#
#     print(word_list)


# Correct way (using recursion) (saw online)

def permutations(l):
    if len(l) == 1:
        yield l

    else:
        for i in range(len(l)):
            for p in permutations(l[:i] + l[i + 1:]):
                yield l[i] + "".join(p)


if __name__ == '__main__':
    char_list = ['c', 'a', 't', 'd', 'o', 'g']

    word_list = []

    for i in permutations(char_list):
        word_list.append(i)

    print(word_list)
