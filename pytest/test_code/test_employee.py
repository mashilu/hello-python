# -*- coding: utf-8 -*-

import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee = Employee('Ma', 'Shilu', 10000)
        print('setUp')

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 15000)
        print('test_give_default_raise')

    def test_give_custom_raise(self):
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.salary, 20000)
        print('test_give_custom_raise')


if __name__ == '__main__':
    unittest.main()
