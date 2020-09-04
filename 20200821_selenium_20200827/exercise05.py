from selenium import webdriver
from selenium.webdriver.support.select import Select
from Is_exist import exist
from time import sleep


def add_order(wd, name):
    wd.find_element_by_xpath('//button[contains(text(),"添加")]').click()
    order_name = wd.find_element_by_css_selector('div.col-lg-8.col-md-8.col-sm-8 > div:nth-child(1) > input')
    order_name.send_keys(name)
    select = Select(wd.find_element_by_css_selector('div.col-lg-8.col-md-8.col-sm-8 > div:nth-child(2) > select'))
    select.select_by_visible_text('南京中医院2')
    select_medicine = Select(wd.find_element_by_css_selector('div.col-lg-8.col-md-8.col-sm-8 > div:nth-child(3) > '
                                                             'select'))
    select_medicine.select_by_visible_text('青霉素盒装1')
    wd.find_element_by_css_selector('div.col-lg-8.col-md-8.col-sm-8 > div:nth-child(3) > input').send_keys('100')
    wd.find_element_by_xpath('//button[contains(text(),"创建")]').click()
    return 0


def del_item(wd, main_windows):
    items = wd.find_elements_by_css_selector('div.search-result-item')
    for item in items:
        sleep(2)
        wd.find_element_by_xpath('//label[contains(text(),"删除")]').click()
        wd.switch_to.alert.accept()
        wd.switch_to.window(main_windows)
    return 0


def add_item(wd, attributes):
    sleep(2)
    item_set = wd.find_elements_by_css_selector(' div.col-lg-8 input')
    i = 0
    for it_s in item_set:
        it_s.send_keys(attributes[i])
        i += 1
    wd.find_element_by_css_selector('div:nth-child(3) > textarea').send_keys(attributes[i])
    wd.find_element_by_xpath('//button[contains(text(),"创建")]').click()
    return 0
