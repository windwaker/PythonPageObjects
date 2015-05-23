import unittest
from selenium import webdriver
import page

# http://selenium-python.readthedocs.org/en/latest/page-objects.html

class PythonOrgSearch(unittest.TestCase):

  def setUp(self):
    # TODO: change back to default before commiting
    self.driver = webdriver.Chrome('/Users/colmh/bin/chromedriver')
    #self.driver = webdriver.Chrome()
    self.driver.get("http://www.python.org")
    # self.driver.set_window_size(1920,1080)
    self.driver.maximize_window()

  def test_search_in_python_org(self):
    main_page = page.MainPage(self.driver)
    assert main_page.does_title_contain("Python"), "Title of page is not correct ..."
    main_page.search_text_element = "pycon"
    main_page.click_go_button()
    search_results_page = page.SearchResultsPage(self.driver)
    assert search_results_page.are_results_found(), "No results found."
    search_results_page.click_go_home()

  def tearDown(self):
    self.driver.save_screenshot('screenshot.png')
    self.driver.close()

if __name__ == "__main__":
  unittest.main()
