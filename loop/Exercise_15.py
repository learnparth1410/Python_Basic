"""
    Exercise 15: Use a loop to display elements from a given list present at odd index positions

    Given:

    my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    Note: list index always starts at 0

    Expected output:
    20 40 60 80 100

"""

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

odd_list = my_list[1::2]
print(odd_list)

for i in odd_list:
    print(i,end=" ")