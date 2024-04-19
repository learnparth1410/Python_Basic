# Exercise 2: Print the sum of the current number and the previous number
# Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.


for i in range(10):
    if i == 0:
        current_num = i
        previous_num = 0
    else:
        current_num = i
        sum_nums = current_num + previous_num
        print(f'Sum of {current_num} and {previous_num} is: {sum_nums}')
        previous_num = current_num
