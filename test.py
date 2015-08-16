import unittest
from selenium import webdriver
import page
import time

# http://selenium-python.readthedocs.org/en/latest/page-objects.html

# run from command line to get XML report
# https://github.com/xmlrunner/unittest-xml-reporting

class PythonOrgSearch(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Chrome()
    self.driver.get("http://www.python.org")
    # self.driver.set_window_size(1920,1080)
    self.driver.maximize_window()

  def test_search_in_python_org(self):
    main_page = page.MainPage(self.driver)
    assert main_page.does_title_contain("Python"), "Title of page is not correct ..."
    main_page.search_text_element = "pycon" # calls __set__ descriptor
    # calls __get__ descriptor
    self.assertEqual(main_page.search_text_element, "pycon", "Wrong text in field.")
    main_page.click_go_button()
    search_results_page = page.SearchResultsPage(self.driver)
    assert search_results_page.are_results_found(), "No results found."
    search_results_page.click_go_home()

  def tearDown(self):
    self.driver.save_screenshot('screenshot.png')
    # self.driver.close()
    self.driver.quit()

if __name__ == "__main__":
  #unittest.main()
  import xmlrunner
  unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))