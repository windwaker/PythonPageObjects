import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from data import Data
from locators import LoginPageLocators
import page
import sys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.events import EventFiringWebDriver
from selenium.webdriver.support.events import AbstractEventListener
from datetime import datetime

'''
Python is becoming a more and more important component in the testing toolkit.
The WebDriver API bindings for Python provide a very convenient mechanism
for leveraging the simplicity of the Python syntax and allows testers to 'ramp up' quickly
when introducing automation into their workflow.
This talk will touch on the basics of using the WebDriver API
as well as topics like Page Objects.
More advanced features of Python such as Decorators and Descriptors will also be introduced.
'''

# http://selenium-python.readthedocs.org/en/latest/page-objects.html
# http://blog.likewise.org/2015/01/automatically-capture-browser-screenshots-after-failed-python-ghostdriver-tests/

# run from command line to get XML report
# https://github.com/xmlrunner/unittest-xml-reporting
from utilities import Utility
import utilities


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        print "Starting test ..."
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_login_internet(self):

        # d = EventFiringWebDriver(self.driver, ScreenshotListener())
        self.driver.get("http://the-internet.dev/login")
        username = self.driver.find_element_by_name("username")
        username.clear()
        username.send_keys("tomsmith")
        password = self.driver.find_element_by_name("password")
        password.clear()
        password.send_keys("SuperSecretPassword!")
        login_button = self.driver.find_element_by_id("submit")
        login_button.click()
        wait = WebDriverWait(self.driver, 5)
        logout = wait.until(EC.element_to_be_clickable((By.ID, 'logout')))
        logout.click()
        wait.until(EC.element_to_be_clickable((By.ID, 'username')))

    def test_login_internet2(self):

        self.driver.get(Data.HOME_PAGE)
        username = self.driver.find_element(*LoginPageLocators.USER_NAME)
        Utility.fill_in(username, Data.USER_NAME_STRING)
        password = self.driver.find_element(*LoginPageLocators.PASSWORD)
        Utility.fill_in(password, Data.PASSWORD_STRING)
        login_button = self.driver.find_element(*LoginPageLocators.SUBMIT)
        login_button.click()
        wait = WebDriverWait(self.driver, 5)
        logout = wait.until(EC.element_to_be_clickable((By.ID, 'logout')))
        logout.click()
        wait.until(EC.element_to_be_clickable((By.ID, 'username')))

        # all_cookies = self.driver.get_cookies()
        #
        # for cookie in all_cookies:
        #     print cookie

    def test_search_in_python_org(self):
        self.driver.get("http://www.python.org")
        main_page = page.MainPage(self.driver)
        # use built in python asserts
        assert main_page.does_title_contain("Python"), "Title of page is not correct ..."
        # use the unittest assertions
        self.assertTrue(main_page.does_title_contain("Python"), "Title of page is not correct ...")
        # calls __set__ descriptor
        main_page.search_text_element = "pycon"
        # calls __get__ descriptor
        self.assertEqual(main_page.search_text_element, "pycon", "Wrong text in field.")
        main_page.click_go_button()
        search_results_page = page.SearchResultsPage(self.driver)
        assert search_results_page.are_results_found(), "No results found."
        search_results_page.click_go_home()

    def tearDown(self):
        # if COMMAND_PARAM == "capture":
        #     self.driver.get_screenshot_as_file('screenshot-%s.png' % datetime.now())
        self.driver.quit()


class ScreenshotListener(AbstractEventListener):

    def on_exception(self, exception, driver):
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        driver.get_screenshot_as_file('screenshot-%s.png' % now)

    def before_navigate_to(self, url, driver):
        print "Navigating to %s" % url

    def before_quit(self, driver):
        print "Getting ready to quit"

    def after_quit(self, driver):
        print "I have officially quit"

    def before_click(self, element, driver):
        print "I clicked %s" % element


if __name__ == "__main__":
    # if len(sys.argv) != 2:
    #     sys.exit("ERROR command-line parameter must be supplied for these tests")
    # COMMAND_PARAM = sys.argv[1]
    # del sys.argv[1:]
    unittest.main()
