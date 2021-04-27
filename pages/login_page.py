# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.workstation_page import WorkStation_Page


class Login_Page(BasePage):

    def form_username(self):
        return self.find(By.ID,'username')

    def form_pwd(self):
        return self.find(By.ID,'password_input')

    def button_login(self):
        return self.find(By.ID,'tcloud_login_button')

    def goto_workstation(self,username,pwd):
        self.form_username().send_keys(username)
        self.form_pwd().send_keys(pwd)
        self.button_login().click()
        return WorkStation_Page(self.driver)









