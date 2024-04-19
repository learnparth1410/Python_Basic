"""
Exercise 9: Check Palindrome Number
Write a program to check if the given number is a palindrome number.

A palindrome number is a number that is the same after reverse. For example, 545, is the palindrome numbers
"""

def is_palindrome(s):
    return s == s[::-1]

s = "parth"
ans = is_palindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")