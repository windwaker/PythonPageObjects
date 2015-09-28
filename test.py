import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from data import Data
from locators import LoginPageLocators
import page
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.events import AbstractEventListener
from datetime import datetime, time
import logging
import utilities

'''
Python is becoming a more and more important component in the testing toolkit.
The WebDriver API bindings for Python provide a very convenient mechanism
for leveraging the simplicity of the Python syntax and allows testers to 'ramp up' quickly
when introducing automation into their workflow.
This talk will touch on the basics of using the WebDriver API
as well as topics like Page Objects.
More advanced features of Python such as Decorators and Descriptors will also be introduced.
'''


class TestDemos(unittest.TestCase):

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    handler = logging.FileHandler('selenium.log')
    handler.setLevel(logging.INFO)
    logger.addHandler(handler)

    def setUp(self):
        self.logger.info('Starting test ...')
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_login_internet_original(self):
        # arrange
        self.logger.info('Instantiating driver ...')
        self.logger.info('Wait time set to 5 seconds ...')
        wait = WebDriverWait(self.driver, 5)
        # d = EventFiringWebDriver(self.driver, ScreenshotListener())
        self.driver.get("http://the-internet.dev/login")

        # act
        self.logger.info('Filling in username')
        username = self.driver.find_element_by_id("username")
        username.clear()
        username.send_keys("tomsmith")

        self.logger.info('Filling in password')
        password = self.driver.find_element_by_id("password")
        password.clear()
        password.send_keys("SuperSecretPassword!")

        self.logger.info('Clicking the submit button')
        login_button = self.driver.find_element_by_id("submit")
        login_button.click()

        # assert
        self.logger.info('Waiting for logged in message on screen')
        wait.until(ec.text_to_be_present_in_element((By.ID, 'flash-messages'), "You logged into a secure area!"))
        logout = wait.until(ec.element_to_be_clickable((By.ID, 'logout')))
        self.logger.info('Clicking logout button')
        logout.click()
        self.logger.info('Waiting for username textfield on screen')
        wait.until(ec.element_to_be_clickable((By.ID, 'username')))

    def test_login_internet_refactored(self):

        # arrange
        wait = WebDriverWait(self.driver, 5)
        self.driver.get(Data.HOME_PAGE)
        util = utilities.Utility(self.driver)
        login_page = page.LoginPage(self.driver)

        # Decorator
        username_locator = (By.CSS_SELECTOR, '#username')
        util.fill_in(username_locator, Data.USER_NAME_STRING)

        # Descriptor
        login_page.login_element = Data.PASSWORD_STRING

        # Vanilla
        login_button = self.driver.find_element(*LoginPageLocators.SUBMIT)
        login_button.click()

        # # assert
        logout = wait.until(ec.element_to_be_clickable((By.ID, 'logout')))
        logout.click()
        wait.until(ec.element_to_be_clickable((By.ID, 'username')))

    def test_login_upsource(self):
        # arrange
        self.logger.info('Instantiating driver ...')
        self.logger.info('Wait time set to 5 seconds ...')
        wait = WebDriverWait(self.driver, 5)
        self.driver.get("http://colms-macbook-pro.local:8080")
        wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.ring-btn_blue')))
        self.driver.find_element_by_css_selector(".ring-btn_blue").click()

        # act
        username = self.driver.find_element_by_css_selector("#username")
        username.clear()
        username.send_keys("admin")
        password = self.driver.find_element_by_css_selector("#password")
        password.clear()
        password.send_keys("rovers")
        login_button = self.driver.find_element_by_css_selector(".login-button")
        login_button.submit()

        # assert
        wait.until(ec.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'create a project')))

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
