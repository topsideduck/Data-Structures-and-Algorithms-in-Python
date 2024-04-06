"""
Write a Python program that inputs a list of words, separated by whitespace,
and outputs how many times each word appears in the list. You need not worry
about efficiency at this point, however, as this topic is something that will
be addressed later in this book.
"""

if __name__ == '__main__':
    words = input("Enter words separated by whitespace: ")

    words = words.split()
    unique_words = set(words)

    for word in unique_words:
        print(f"{word} appears {words.count(word)} times.")
