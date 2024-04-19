"""
    OOP Exercise 1: Create a Class with instance attributes
    Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

    Refer:

    Classes and Objects in Python
    Instance variables in Python
"""


class Vehicle:
    def __init__(self, max_spped, milage):
        self.max_speed = max_spped
        self.mileage = milage

modelx = Vehicle(210,40)

print(modelx.max_speed, modelx.mileage)