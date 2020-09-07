from selenium.webdriver.common.action_chains import ActionChains
from tps300ol.method import *
from time import sleep

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    @staticmethod
    def wait(second):
        sleep(second)

    def css_seletors(self, selector):
        return self.driver.find_elements_by_css_selector(selector)

    def x_paths(self, xpath):
        return self.driver.find_elements_by_xpath(xpath)

    def css_seletor(self, selector):
        return self.driver.find_element_by_css_selector(selector)

    def x_path(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    @staticmethod
    def get_text(element):
        return element.text

    def get_url(self):
        return self.driver.current_url

    def mouse_move(self, element):
        ActionChains(self.driver).move_to_element(
            element
        )

    def move_to_element(self, xpath):
        return self.x_path(xpath)

    def switch_to_element(self, selector):
        return self.css_seletor(selector)

    def exist_css_seletor(self, selector):
        return exist_cssSeletor(self.driver, selector)

    def exist_xpath(self, xpath):
        return exist_xPath(self.driver, xpath)

    @staticmethod
    def select_clean(select, options):
        select_clean(select, options)

    @staticmethod
    def input_text(element, text):
        element.send_keys(text)

    @staticmethod
    def click(element):
        element.click()