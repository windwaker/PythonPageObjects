from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import LoginPageLocators
import logging


class Utility(object):

    def __init__(self, driver):
        self.driver = driver

    def logging(inner):
        def inner_func(*args, **kwargs):
            # TODO replace with logging
            print "typing: " + str(args[2]) + " in field: " + str(args[1][1])
            inner(*args, **kwargs)
        return inner_func

    @logging
    def fill_in(self, locator, text):
        web_element = self.driver.find_element(*locator)
        web_element.clear()
        web_element.send_keys(text)
