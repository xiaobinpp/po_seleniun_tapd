# -*- coding: utf-8 -*-
from pages.base_page import BasePage
from pages.login_page import Login_Page
from pages.workstation_page import WorkStation_Page


class Test_login():

    def setup(self):
        self.loginpage = Login_Page()
        self.username = 'xxxx'
        self.pwd = 'xxxx'

    def teardown(self):
        pass


    def test_login(self):
        workstation = self.loginpage.goto_workstation(self.username,self.pwd)
        assert '工作台' in workstation.workstation()


