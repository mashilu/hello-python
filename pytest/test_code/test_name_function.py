# -*- coding: utf-8 -*-

import unittest
from name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    """
    测试name_function.py
    """

    # 无middle，且first和last都为小写的测试用例
    def test_first_last_name_1(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    # 有middle, 且都为小写
    def test_first_middle_last_name_1(self):
        formatted_name = get_formatted_name('ma', 'lu', 'shi')
        self.assertEqual(formatted_name, 'Ma Shi Lu')


if __name__ == '__main__':
    unittest.main()
