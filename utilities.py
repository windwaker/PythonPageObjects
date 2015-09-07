__author__ = 'colmh'


class Utility(object):

    # def __init__(self, driver):
    #     self.driver = driver

    @staticmethod
    def fill_in(web_element, text):
        web_element.clear()
        web_element.send_keys(text)
