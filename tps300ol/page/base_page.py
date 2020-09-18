from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

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

    # 使用xpath选择一个，封装了selenium的方法
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

    # 二次封装selenium的execute_script方法，实现页面滚动至某元素可见
    def page_scroll(self, ele):
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)

    # 二次封装公共方法，传入表格编辑选项、名称和选项的class，返回被选中或者未选中的选项的名称的列表
    @staticmethod
    def check_lists(options, options_name, status):
        return option_names(options, options_name, status)

    #  二次封装公共方法，传入表格编辑选项、名称和选项的class，返回被选中或者未选中的选项的名称
    @staticmethod
    def check_list(options, options_name, status):
        return op_name(options, options_name, status)

    def page_list(self):
        return self.css_selectors('div > ul > li.number')

    def back_btn(self):
        return self.css_selector(' div > button.btn-prev')

    def next_btn(self):
        return self.css_selector(' div > button.btn-next')

    def page_input(self):
        return self.css_selector('span.el-pagination__jump > div > input')

    def checked_number(self):
        return self.css_selectors(' div.el-table__body-wrapper tr:nth-child(1) div')

    def more_btn(self):
        return self.css_selector('div > ul > li.more')

    def page_turn(self):
        s = len(self.page_list())
        if s == 1:
            self.input_text(self.page_input(), '2')
            self.input_text(self.page_input(), Keys.ENTER)
            if self.is_exist(self.checked_number(), 1):
                c = self.get_text(self.checked_number()[0])
            else:
                c = []
            if c == [] or c == '1':
                return True
        elif 4 >= s > 1:
            self.input_text(self.page_input(), f'{s+1}')
            self.input_text(self.page_input(), Keys.ENTER)
            c1 = self.get_text(self.checked_number()[0])
            k = 0
            if c1 == f'{((s-1)*20)+1}':
                k += 1
            self.element_click(self.back_btn())
            if self.get_text(self.checked_number()[0]) == '1':
                k += 1
            self.element_click(self.next_btn())
            if self.get_text(self.checked_number()[0]) == '21':
                k += 1
            self.element_click(self.page_list()[0])
            if self.get_text(self.checked_number()[0]) == '1':
                k += 1
            self.element_click(self.page_list()[1])
            if self.get_text(self.checked_number()[0]) == '21':
                k += 1
            if k == 5:
                return True
            else:
                return False
        elif s > 4:
            num = self.get_text(self.page_list()[4])
            self.input_text(self.page_input(), num)
            self.input_text(self.page_input(), Keys.ENTER)
            num1 = int(num)
            c2 = self.get_text(self.checked_number()[0])
            k1 = 0
            num2 = ((num1 - 1) * 20) + 1
            if c2 == f'{num2}':
                k1 += 1
            self.element_click(self.back_btn())
            if self.get_text(self.checked_number()[0]) == f'{num2-20}':
                k1 += 1
            self.element_click(self.next_btn())
            if self.get_text(self.checked_number()[0]) == f'{num2}':
                k1 += 1
            self.element_click(self.page_list()[0])
            if self.get_text(self.checked_number()[0]) == '1':
                k1 += 1
            self.element_click(self.page_list()[1])
            if self.get_text(self.checked_number()[0]) == '21':
                k1 += 1
            self.element_click(self.more_btn())
            if self.get_text(self.checked_number()[0]) == '81':
                k1 += 1
            if k1 == 6:
                return True
            else:
                return False