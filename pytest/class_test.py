# -*- coding: utf-8 -*-


# class Restaurant:
#
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         print(self.restaurant_name + " " + self.cuisine_type)
#
#     def open_restaurant(self):
#         print("Opening")
#
#
# a_restaurant = Restaurant("qingsonglu", "artist")
# a_restaurant.describe_restaurant()
# a_restaurant.open_restaurant()


# class User:
#
#     def __init__(self, first_name, last_name, **attr):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.attr = dict()
#         for key, value in attr.items():
#             self.attr[key] = value
#
#     def describe_user(self):
#         print(self.first_name)
#         print(self.last_name)
#         for key, value in self.attr.items():
#             print(key + "=" + value)
#
#     def greet_user(self):
#         print("hello, " + self.first_name + " " + self.last_name)
#
#
# user = User("ma", "shilu", job="test engineer", sex="male")
# user.describe_user()
# user.greet_user()


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super.__init__(make, model, year)


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
