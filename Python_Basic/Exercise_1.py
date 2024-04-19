# Q-1 :exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

def cal_fun(num1, num2):
    if num1 * num2 <= 1000:
        return num1 * num2
    else:
        return num1 + num2

num1 = 30
num2 = 40
result = cal_fun(num1, num2)
print(result)
