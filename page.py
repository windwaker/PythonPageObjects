from element import BasePageElement
from locators import MainPageLocators
from locators import SearchResultsPageLocators
from selenium.webdriver.support.ui import WebDriverWait

class SearchTextElement(BasePageElement):

    #locator = 'q'
    locator = MainPageLocators.SEARCH_FOR


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    search_text_element = SearchTextElement()

    def does_title_contain(self, page_title):
        return page_title in self.driver.title

    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()


class SearchResultsPage(BasePage):

    def are_results_found(self):
        #self.driver.page_source
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.driver.find_element(*SearchResultsPageLocators.RESULTS))
        return "PyCon" in self.driver.find_element(*SearchResultsPageLocators.RESULTS).text

    def click_go_home(self):
        element = self.driver.find_element(*SearchResultsPageLocators.GO_HOME)
        element.click()
