from selenium.webdriver.support.ui import WebDriverWait
import logging


class BasePageElement(object):

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    handler = logging.FileHandler('selenium.log')
    handler.setLevel(logging.INFO)
    logger.addHandler(handler)

    def __get__(self, instance, owner=None):
        driver = instance.driver
        self.logger.info("Getting a value from [{0}]".format(self.locator))
        WebDriverWait(driver, 10).until(
            lambda browser: browser.find_element(*self.locator))
        element = driver.find_element(*self.locator)
        return element.get_attribute("value")

    def __set__(self, instance, value):
        driver = instance.driver
        self.logger.info('Sending \'{0}\' value to [{1}]'.format(value, self.locator[1]))
        WebDriverWait(driver, 10).until(
            lambda browser: browser.find_element(*self.locator))
        driver.find_element(*self.locator).send_keys(value)

    def __del__(self, instance):
        pass


