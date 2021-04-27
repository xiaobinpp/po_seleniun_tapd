# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self,driver:WebDriver = None):
        if driver is None:
            self.driver = webdriver.Chrome()
            self.driver.get('https://www.tapd.cn/cloud_logins/login')
            self.driver.implicitly_wait(10)
        else:
            self.driver = driver

    # def by_xpath(self,xpath):
    #     return self.driver.find_element_by_xpath(xpath)
    #
    #
    # def by_css(self,css):
    #     return self.driver.find_element_by_css_selector(css)
    #
    #
    # def by_id(self,id):
    #     return self.driver.find_element_by_id(id)


    def find(self,by,locator):
        return self.driver.find_element(by,locator)


    def wait_for_element(self,conditions,time=10,):
        WebDriverWait(self.driver,time).until(conditions)











