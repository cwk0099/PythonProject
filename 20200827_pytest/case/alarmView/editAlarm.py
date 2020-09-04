from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import method
from time import sleep


def edit_alarm(wd=webdriver.Chrome()):
    ActionChains(wd).move_to_element(
        wd.find_element_by_css_selector('li.is-active  div')
    ).perform()
    sleep(2)
    wd.find_element_by_xpath('//li[contains(text(),"告警窗")]').click()
    wd.find_element_by_css_selector('div:nth-child(1) > div > div > div.el-input--suffix > span > span > i').click()
    status_select = wd.find_elements_by_css_selector('body > div.el-select-dropdown> div.el-scrollbar > '
                                                     'div.el-select-dropdown__wrap > ul > li')
    status_select[0].click()
    wd.find_element_by_css_selector('div:nth-child(6) > div > div > button').click()
    if method.exist_cssSeletor(wd, 'div:nth-child(6) > div > div > button'):
        return False
    else:
        alarms = wd.find_elements_by_css_selector('div.el-table__fixed-body-wrapper > table > tbody > tr '
                                                  'i.el-icon-edit')
        alarms[0].click()
        sleep(1)
        wd.find_element_by_xpath('//span[text()="确定"]').click()
        sleep(1)
        exword = wd.find_element_by_css_selector('p.el-message__content').text
        if exword == '修改成功':
            return True
        else:
            return False
