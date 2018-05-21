# -*- coding: utf-8 -*-

from random import randint


class Die:

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        random_number = randint(1, self.sides)
        return random_number


if __name__ == '__main__':
    a_die = Die(6)
    for i in range(1, 11):
        print(a_die.roll_die())

    print("------------------------")
    a_die = Die(10)
    for i in range(1, 11):
        print(a_die.roll_die())

    print("------------------------")
    a_die = Die(20)
    for i in range(1, 11):
        print(a_die.roll_die())
