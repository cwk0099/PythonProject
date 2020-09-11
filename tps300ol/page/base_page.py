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

    # 显性等待方法
    @staticmethod
    def wait(second):
        sleep(second)

    # 使用css选择器选择多个元素，返回的是一个列表，封装了selenium的方法
    def css_selectors(self, selector):
        return self.driver.find_elements_by_css_selector(selector)

    # 使用xpath选择多个元素，返回的是一个列表，封装了selenium的方法
    def xpaths(self, xpath):
        return self.driver.find_elements_by_xpath(xpath)

    # 使用css选择器选择一个，封装了selenium的方法
    def css_selector(self, selector):
        return self.driver.find_element_by_css_selector(selector)

    # 使用xpath选择一，封装了selenium的方法
    def xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    # 使用css选择器择一个子元素的方法
    @staticmethod
    def son_css_selector(element, selector):
        return element.find_element_by_css_selector(selector)

    # 使用css选择器择多个子元素的方法，返回一个列表
    @staticmethod
    def son_css_selectors(element, selector):
        return element.find_elements_by_css_selector(selector)

    # xpath选择一个子元素的方法
    @staticmethod
    def son_xpath(element, xpath):
        return element.find_element_by_xpath(xpath)

    # xpath选择多个子元素的方法，返回一个列表
    @staticmethod
    def son_xpaths(element, xpath):
        return element.find_elements_by_xpath(xpath)

    # 获取元素文本的办法，封装了selenium的方法
    @staticmethod
    def get_text(element):
        return element.text

    # 获取元素url的办法，封装了selenium的方法
    def get_url(self):
        return self.driver.current_url

    def mouse_move(self, element):
        ActionChains(self.driver).move_to_element(
            element
        ).perform()

    # 二次封装公共方法,判断元素是否存在,传入一个element列表和一个整数,若是0则是寻找单个元素,若是1则寻找多个元素
    # 存在则返回True,否则False
    @staticmethod
    def is_exist(element_list, s):
        return is_element_exist(element_list, s)

    # 二次封装公共方法，清除查询选择框的选项，并点击查询
    @staticmethod
    def select_clean(select, options, search):
        select_clean(select, options, search)

    # 二次封装selenium的方法，向输入框传输文字
    @staticmethod
    def input_text(element, text):
        element.send_keys(text)

    # 二次封装selenium的click()方法
    @staticmethod
    def element_click(element):
        element.click()

    # 二次封装selenium的refresh方法，刷新当前页面
    def page_refresh(self):
        self.driver.refresh()

    # 二次封装公共方法，传入表格编辑选项、名称和选项的class，返回被选中或者未选中的选项的名称的列表
    @staticmethod
    def check_lists(options, options_name, status):
        return option_names(options, options_name, status)

    #  二次封装公共方法，传入表格编辑选项、名称和选项的class，返回被选中或者未选中的选项的名称
    @staticmethod
    def check_list(options, options_name, status):
        return op_name(options, options_name, status)