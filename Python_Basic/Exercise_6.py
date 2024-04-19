"""
Exercise 6: Display numbers divisible by 5 from a list
Iterate the given list of numbers and print only those numbers which are divisible by 5

"""




numbers = [10, 15, 20, 25, 30, 35, 40]

for number in numbers:
    if number % 5 == 0:
        print(number)
