"""
Exercise 14: Print a downward Half-Pyramid Pattern of Star (asterisk)

* * * * *
* * * *
* * *
* *
*
"""


def half_pyamid(rows):
    for i in range(rows,0,-1):
        for j in range(i):
            print("*", end =' ')
        print()

rows = 5
half_pyamid(rows)