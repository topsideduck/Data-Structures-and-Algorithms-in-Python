"""
Write a Python program that repeatedly reads lines from standard input
until an EOFError is raised, and then outputs those lines in reverse order
(a user can indicate end of input by typing ctrl-D).
"""

if __name__ == '__main__':
    lst = []

    while True:
        try:
            lst.append(input("> "))

        except (EOFError, KeyboardInterrupt):
            break

    print()

    for i in reversed(lst):
        print(i)
