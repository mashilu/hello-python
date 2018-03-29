# -*- coding: utf-8 -*-
from selenium import webdriver
from autotest.ECSS.view.loginpage import LoginPage

import time

url = "http://192.168.156.17:8808"

driver = webdriver.Firefox()
driver.implicitly_wait(10)
login_page = LoginPage(driver, url)
login_page.open()
login_page.input_username('ec_10102464')
login_page.input_password('1234')
login_page.input_jcaptcha('1234')
login_page.click_submit()

driver.quit()


