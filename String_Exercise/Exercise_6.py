"""
    Exercise 6: Create a mixed String using the following rules
    Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.

    Given:

    s1 = "Abc"
    s2 = "Xyz"
    Expected Output:

    AzbycX
"""


input1 = "Abc"
input2 = "Xyz"

output = "".join(c1 + c2 for c1, c2 in zip(input1, input2))
print(output)