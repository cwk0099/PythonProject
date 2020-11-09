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

    # 使用css选择器定位元素，传入css选择器和s参数，s默认为0
    # 当s为0时，应返回一个元素，如果定位不到或者定位到了多个元素，则会返回False
    # 当s为1时，返回一个元素列表，若定位不到，则返回False
    def css_selector(self, selector, s=0):
        ele = self.driver.find_elements_by_css_selector(selector)
        if s == 0 and len(ele) == 1:
            return ele[0]
        elif len(ele) == 0:
            print('找不到对应元素')
            return False
        elif s == 1 and len(ele) != 0:
            return ele
        elif s == 0 and len(ele) > 1:
            print('找到多个相同的元素')
            return False

    # 使用xpath定位元素，传入xpath路径和s参数，s默认为0
    # 当s为0时，应返回一个元素，如果定位不到或者定位到了多个元素，则会返回False
    # 当s为1时，返回一个元素列表，若定位不到，则返回False
    def xpath(self, xpath, s=0):
        ele = self.driver.find_elements_by_xpaths(xpath)
        if s == 0 and len(ele) == 1:
            return ele[0]
        elif len(ele) == 0:
            print('找不到对应元素')
            return False
        elif s == 1 and len(ele) != 0:
            return ele
        elif s == 0 and len(ele) > 1:
            print('找到多个相同的元素')
            return False

    # 使用css选择器定位子元素，传入css选择器和s参数,s默认为0
    # 当s为0时，应返回一个子元素，如果定位不到或者定位到了多个子元素，则会返回False
    # 当s为1时，返回一个子元素列表，若定位不到，则返回False
    @staticmethod
    def son_css_selector(element, selector, s=0):
        ele = element.find_elements_by_css_selector(selector)
        if s == 0 and len(ele) == 1:
            return ele[0]
        elif len(ele) == 0:
            print('找不到对应子元素')
            return False
        elif s == 1 and len(ele) != 0:
            return ele
        elif s == 0 and len(ele) > 1:
            print('找到多个相同的子元素')
            return False

    # 使用xpath定位子元素，传入xpath和s参数
    # 当s为0时，应返回一个子元素，如果定位不到或者定位到了多个子元素，则会返回False
    # 当s为1时，返回一个子元素列表，若定位不到，则返回False
    @staticmethod
    def son_xpath(element, xpath, s=0):
        ele = element.find_elements_by_xpath(xpath)
        if s == 0 and len(ele) == 1:
            return ele[0]
        elif len(ele) == 0:
            print('找不到对应子元素')
            return False
        elif s == 1 and len(ele) != 0:
            return ele
        elif s == 0 and len(ele) > 1:
            print('找到多个相同的子元素')
            return False

    # 定位父元素的方法
    @staticmethod
    def father_element(element):
        return element.find_element_by_xpath('..')

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

    # 二次封装公共方法，传入表格编辑选项、名称和选项的class，返回被选中或者未选中的选项的名称
    @staticmethod
    def check_list(options, options_name, status):
        return op_name(options, options_name, status)

    # 页数列表
    def page_list(self):
        return self.css_selector('div > ul > li.number', 1)

    # 后退一页按钮
    def back_btn(self):
        return self.css_selector(' div > button.btn-prev')

    # 向前翻页按钮
    def next_btn(self):
        return self.css_selector(' div > button.btn-next')

    # 页数输入框
    def page_input(self):
        return self.css_selector('span.el-pagination__jump > div > input')

    # 用来检查翻页是否正确的按钮
    def checked_number(self):
        return self.css_selector(' div.el-table__body-wrapper tr:nth-child(1) div', 1)

    # 页数的更多按钮
    def more_btn(self):
        return self.css_selector('div > ul > li.more')

    # 翻页的步骤
    def page_turn(self):
        s = len(self.page_list())
        if s == 1:
            self.input_text(self.page_input(), '2')
            self.input_text(self.page_input(), Keys.ENTER)
            if not self.checked_number():
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
