from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def exist(wd):
    try:
        wd.find_element_by_css_selector('div.row>h4')
    except NoSuchElementException as e:
        return True
    else:
        return False


