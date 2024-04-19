"""
    Exercise 17: Find words with both alphabets and numbers
    Write a program to find words with both alphabets and numbers from an input string.

    Given:

    str1 = "Emma25 is Data scientist50 and AI Expert"
    Expected Output:

    Emma25
    scientist50
"""


# Find words with both alphabets and numbers
str1 = "Emma25 is Data scientist50 and AI Expert"

digit = []
alpha = []

for char in str1:
    if char.isdigit():
        digit.append(char)
    elif char.isalpha:
        alpha.append(char)
ter = (digit + alpha)
print(ter)
print(digit)
print(char)


