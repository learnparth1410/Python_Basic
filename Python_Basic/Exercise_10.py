"""
Exercise 10: Create a new list from two list using the following condition

Create a new list from two list using the following condition

Given two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.

"""


list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]


new_list = []

for num1 in list1:
    if num1 % 2 != 0:  
        new_list.append(num1)


for num2 in list2:
    if num2 % 2 == 0:  
        new_list.append(num2)

print(new_list)
