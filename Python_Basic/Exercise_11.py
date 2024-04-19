"""
Exercise 11: Write a Program to extract each digit from an integer in the reverse order.

For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

"""

num = int(input("Enter an integer: "))

num_str = str(num)[::-1]
digits = ' '.join(num_str)

print(digits)
