# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from autotest.ECSS.view import loginpage
import time


class Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        print("setup")

    def test_login(self):
        print("test_login")
        login_page = loginpage(self.driver)
        login_page.input_username(self, 'ec_10102464')
        login_page.input_password(self, '1234')
        login_page.input_jcaptcha(self, '1234')
        login_page.click_submit()
        time.sleep(10)

    def tearDown(self):
        self.driver.quit()
        print("tearDown")


if __name__ == '__main__':
    unittest.main()
