# -*- coding: utf-8 -*-


class Employee:

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, salary_raise=5000):
        """
        增加年薪
        :param salary_raise:
        :return:
        """
        self.salary += salary_raise
