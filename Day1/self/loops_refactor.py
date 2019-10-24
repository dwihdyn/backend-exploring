# https://code.nextacademy.com/lessons/loops/395

"""
Using list comprehension, try refactoring this method to be more succinct!

hint: You will need to use conditionals within your list comprehension.
"""


def long_words(lst):
    words = []
    for word in lst:
        if len(word) > 5:
            words.append(word)
    return words
