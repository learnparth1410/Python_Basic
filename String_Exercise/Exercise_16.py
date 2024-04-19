"""
    Exercise 16: Removal all characters from a string except integers
    Given:

    str1 = 'I am 25 years and 10 months old'
    Expected Output:

    2510
"""

str1 = 'I am 25 years and 10 months old'
digit = 0

res = "".join([char for char in str1 if char.isdigit()])

print(res)