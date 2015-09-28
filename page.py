from selenium.webdriver.common.by import By
from element import BasePageElement
from locators import MainPageLocators, LoginPageLocators
from locators import SearchResultsPageLocators
from selenium.webdriver.support.ui import WebDriverWait


class SearchTextElement(BasePageElement):

    locator = MainPageLocators.SEARCH_FOR


class LoginElement(BasePageElement):

    locator = LoginPageLocators.PASSWORD


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class LoginPage(BasePage):

    login_element = LoginElement()


class MainPage(BasePage):

    search_text_element = SearchTextElement()

    def does_title_contain(self, page_title):
        return page_title in self.driver.title

    def click_go_button(self):
        # print "Type: " + str(type(MainPageLocators.GO_BUTTON))
        # unpack the arg as it is passed as a tuple
        # https://docs.python.org/2/tutorial/controlflow.html#unpacking-argument-lists
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element = self.driver.find_element(By.CSS_SELECTOR, '#submit')
        element.click()


class SearchResultsPage(BasePage):

    def are_results_found(self):
        # self.driver.page_source
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.driver.find_element(*SearchResultsPageLocators.RESULTS))
        return "PyCon" in self.driver.find_element(*SearchResultsPageLocators.RESULTS).text

    def click_go_home(self):
        element = self.driver.find_element(*SearchResultsPageLocators.GO_HOME)
        element.click()