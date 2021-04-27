# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class WorkStation_Page(BasePage):

    def ele_workstation(self):
        return self.find(By.CSS_SELECTOR,'#top_nav_worktable>div')


    def workstation(self):
        return self.ele_workstation().text

