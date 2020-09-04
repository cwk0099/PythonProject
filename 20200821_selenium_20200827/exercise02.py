import exercise01
from selenium import webdriver


def creat(wd):
    wd.find_element_by_class_name('btn-md').click()
    client = wd.find_elements_by_css_selector('input[class="form-control"]')
    client_name = client[0]
    client_phone = client[1]
    client_address = wd.find_element_by_css_selector('textarea[class="form-control"]')
    client_name.send_keys('南京市中医院')
    client_phone.send_keys('15217841131')
    client_address.send_keys('广东省-广州市-天河区-高唐路22号')
    wd.find_element_by_xpath("//button[contains(text(),'创建')]").click()
    return


def modify(wd):
    wd.find_element_by_css_selector('input[placeholder="请输入关键词搜索"]').send_keys('南京市中医院')
    wd.find_element_by_id('btn_search_exams').click()
    wd.find_element_by_xpath("//*[contains(text(),'编辑')]").click()
    cn = wd.find_elements_by_css_selector('input[class="form-control"]')
    cn[1].clear()
    cn[1].send_keys('南京省中医院')
    wd.find_element_by_xpath("//*[contains(text(),'确定')]").click()
    return
