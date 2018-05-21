# -*- coding: utf-8 -*-


class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name + " " + self.cuisine_type)

    def open_restaurant(self):
        print("Opening")


if __name__ == '__main__':
    a_restaurant = Restaurant("qingsonglu", "artist")
    a_restaurant.describe_restaurant()
    a_restaurant.open_restaurant()






