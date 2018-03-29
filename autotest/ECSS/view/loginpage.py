# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from autotest.ECSS.view.page import Page


class LoginPage(Page):
    '''
    ECSS登陆页面模型
    '''
    username_loc = (By.ID, 'userId')
    password_loc = (By.ID, 'password')
    jcaptcha_loc = (By.ID, 'jcaptcha')
    submit_loc = (By.ID, 'loginBtn')

    # Action
    def input_username(self, username):
        self.find_element(*self.username_loc).send_keys(username)

    def input_password(self, password):
        self.find_element(*self.password_loc).send_keys(password)

    def input_jcaptcha(self, jcaptcha):
        self.find_element(*self.jcaptcha_loc).send_keys(jcaptcha)

    def click_submit(self):
        self.find_element(*self.submit_loc).click()
