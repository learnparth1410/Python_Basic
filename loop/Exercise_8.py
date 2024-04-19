"""
    Exercise 8: Print list in reverse order using a loop

    list1 = [10, 20, 30, 40, 50]
    Expected output:

    50
    40
    30
    20
    10
"""

list1 = [10, 20, 30, 40, 50]

rev_list1 = reversed(list1)


for i in rev_list1:
    print(i)