from selenium.webdriver.support.ui import WebDriverWait

class BasePageElement(object):

    def __set__(self, obj, value):
        driver = obj.driver
        #WebDriverWait(driver, 100).until(
        #    lambda driver: driver.find_element_by_name(self.locator))
        #    driver.find_element_by_name(self.locator).send_keys(value)
        print "Using descriptor to set page element text ..."
        WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element(*self.locator))
        driver.find_element(*self.locator).send_keys(value)

    # update __get__ to use more generic find_element
    def __get__(self, obj, owner):
        driver = obj.driver
        print "getting ..."
        WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_name(self.locator))
        element = driver.find_element_by_name(self.locator)
        return element.get_attribute("value")
