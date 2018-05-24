# -*- coding: utf-8 -*-

from unittest import TestCase
from unittest import main
from city_functions import get_city_country_name


class CityNameTestCase(TestCase):

    # def test_city_country(self):
    #     self.assertEqual(get_city_country_name('Santiago', 'Chile'), 'Santiago, Chile')

    def test_city_country_population(self):
        self.assertEqual(get_city_country_name('Santiago', 'Chile', 5000000), 'Santiago, Chile - population 5000000')


if __name__ == '__main__':
    main()
