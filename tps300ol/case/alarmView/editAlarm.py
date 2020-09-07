from selenium.webdriver.common.action_chains import ActionChains
from tps300ol import method
from time import sleep
from tps300ol.method import select_clean

def edit_alarm(wd, s):
    wd.implicitly_wait(10)
    ActionChains(wd).move_to_element(
        wd.find_element_by_css_selector('li.is-active  div')
    ).perform()
    sleep(1)
    wd.find_element_by_xpath('//li[contains(text(),"告警窗")]').click()
    sleep(2)
    select = wd.find_element_by_css_selector('div:nth-child(1) > div > div > div.el-input--suffix > span > span > i')
    select.click()
    status_select = wd.find_elements_by_css_selector('body > div.el-select-dropdown> div.el-scrollbar > '
                                                     'div.el-select-dropdown__wrap > ul > li')
    status_select[s].click()
    wd.find_element_by_css_selector('div:nth-child(6) > div > div > button').click()
    bol = method.exist_cssSeletor(wd, 'div:nth-child(6) > div > div > button')
    if not bol:
        select_clean(select, status_select)
        return False
    else:
        alarms = wd.find_elements_by_css_selector('div.el-table__fixed-body-wrapper > table > tbody > tr '
                                                  'i.el-icon-edit')
        alarms[0].click()
        sleep(1)
        wd.find_element_by_css_selector('body > div.el-message-box__wrapper > div > div.el-message-box__btns > '
                                        'button.el-button.el-button--default.el-button--small.el-button--primary'
                                        '').click()
        sleep(1)
        exword = wd.find_element_by_css_selector('p.el-message__content').text
        select_clean(select, status_select)
        if exword == '修改成功!':
            return True
        else:
            return False
