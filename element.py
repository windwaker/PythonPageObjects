from selenium.webdriver.support.ui import WebDriverWait


class BasePageElement(object):

    def __set__(self, obj, val):
        driver = obj.driver
        print ("Sending '{0}' value to [{1}]".format(val, self.locator[1]))
        WebDriverWait(driver, 10).until(
            lambda browser: browser.find_element(*self.locator))
        driver.find_element(*self.locator).send_keys(val)

    def __get__(self, obj, typ=None):
        driver = obj.driver
        print ("Getting a value from [{0}]".format(self.locator))
        WebDriverWait(driver, 10).until(
            lambda browser: browser.find_element(*self.locator))
        element = driver.find_element(*self.locator)
        return element.get_attribute("value")
