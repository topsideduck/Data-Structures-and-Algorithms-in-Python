"""
Demonstrate how to use Python’s list comprehension syntax to produce
the list [ a , b , c , ..., z ], but without having to type all 26 such
characters literally.
"""

if __name__ == '__main__':
    print([chr(i) for i in range(ord('a'), ord('z') + 1)])
