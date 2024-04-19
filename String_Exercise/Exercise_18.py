"""
    Exercise 18: Replace each special symbol with # in the following string
    Given:

    str1 = '/*Jon is @developer & musician!!'
    Expected Output:

    ##Jon is #developer # musician##
"""
import string
str1 = '/*Jon is @developer & musician!!'

replace_chaar = '#'

for char in string.punctuation:
    str1 = str1.replace(char, replace_chaar)
print(str1)