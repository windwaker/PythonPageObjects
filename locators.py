from selenium.webdriver.common.by import By

class MainPageLocators(object):
    GO_BUTTON  = (By.CSS_SELECTOR, '#submit')
    SEARCH_FOR = (By.CSS_SELECTOR, '#id-search-field')


class SearchResultsPageLocators(object):
    GO_HOME = (By.CSS_SELECTOR, '.python-logo')
    RESULTS = (By.CSS_SELECTOR, '.list-recent-events')  