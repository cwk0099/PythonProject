from selenium.webdriver.common.action_chains import ActionChains
from method import *
from time import sleep

# 基本的Page,二次封装所有用例都要用到的方法，用多少写多少，如：元素定位，隐形等待，等待，获取文本等等
# 之后所有的Page都要继承BasePage
class BasePage:
    # 构造方法，传递driver和隐形等待
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    @staticmethod
    def wait(second):
        sleep(second)

    def css_selectors(self, selector):
        return self.driver.find_elements_by_css_selector(selector)

    def xpaths(self, xpath):
        return self.driver.find_elements_by_xpath(xpath)

    def css_selector(self, selector):
        return self.driver.find_element_by_css_selector(selector)

    def xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    @staticmethod
    def son_css_selector(element, selector):
        return element.find_element_by_css_selector(selector)

    @staticmethod
    def son_css_selectors(element, selector):
        return element.find_elements_by_css_selector(selector)

    @staticmethod
    def son_xpath(element, xpath):
        return element.find_element_by_xpath(xpath)

    @staticmethod
    def son_xpaths(element, xpath):
        return element.find_elements_by_xpath(xpath)

    @staticmethod
    def get_text(element):
        return element.text

    def get_url(self):
        return self.driver.current_url

    def mouse_move(self, element):
        ActionChains(self.driver).move_to_element(
            element
        ).perform()

    # 二次封装公共方法
    def exist_css_selector(self, selector):
        return exist_cssSelector(self.driver, selector)

    def exist_xpath(self, xpath):
        return exist_xPath(self.driver, xpath)

    @staticmethod
    def select_clean(select, options, search):
        select_clean(select, options, search)

    @staticmethod
    def input_text(element, text):
        element.send_keys(text)

    @staticmethod
    def element_click(element):
        element.click()

    @staticmethod
    def check_tableList(options, options_name, status):
        return table_options(options, options_name, status)