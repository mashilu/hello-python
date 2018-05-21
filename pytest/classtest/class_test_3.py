# -*- coding: utf-8 -*-
from pytest.classtest.class_test import Restaurant


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ['Vanilla', 'Chocolate', 'Matcha', 'Green Tea']

    def get_flavours(self):
        print(self.flavours)


if __name__ == '__main__':
    ice_cream_stand = IceCreamStand("test restaurant name", "ice cream")
    ice_cream_stand.get_flavours()
