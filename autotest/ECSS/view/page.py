# -*- coding: utf-8 -*-


class Page(object):
    '''
    基础类，用于月面对象类的继承
    '''

    def __init__(self, selenium_driver, url):
        self.url = url
        self.driver = selenium_driver
        self.timeout = 30

    def on_page(self):
        print(self.driver.current_url)
        print(self.url)
        return self.driver.current_url == self.url

    def _open(self, url):
        self.driver.get(url)

    def open(self):
        self._open(self.url)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

