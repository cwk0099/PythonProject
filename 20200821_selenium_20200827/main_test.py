from selenium import webdriver
from time import sleep
import exercise01
import exercise02
import exercise03
import exercise04
import exercise05
from Is_exist import exist

wd = webdriver.Chrome()
wd.implicitly_wait(4)
exercise01.login(wd)
# exercise02.modify(wd)
# exercise03.med_creat(wd)
# exercise04.print_menu(wd)
wd.find_element_by_css_selector('a[href="#/orders"]').click()
items = wd.find_elements_by_css_selector('div.search-result-item')
main_windows = wd.current_window_handle
if exist(wd):
    for item in items:
        wd.find_element_by_xpath('//label[contains(text(),"删除")]').click()
        wd.switch_to.alert.accept()
        wd.switch_to.window(main_windows)
wd.find_element_by_css_selector('a[href="#/customers"]').click()
customers = [['南京中医院1', '2551867851', '江苏省-南京市-秦淮区-汉中路-501'],
             ['南京中医院2', '2551867852', '江苏省-南京市-秦淮区-汉中路-502'],
             ['南京中医院3', '2551867853', '江苏省-南京市-秦淮区-汉中路-503']
             ]
medicines = [['青霉素盒装1', 'YP-32342341', '青霉素注射液，每支15ml，20支装'],
             ['青霉素盒装2', 'YP-32342342', '青霉素注射液，每支15ml，30支装'],
             ['青霉素盒装3', 'YP-32342343', '青霉素注射液，每支15ml，40支装']
             ]
if exist(wd) and wd.current_url != 'http://127.0.0.1/mgr/index.html#/orders':
    exercise05.del_item(wd, main_windows)
sleep(1)
wd.find_element_by_xpath('//button[contains(text(),"添加")]').click()
if not exist(wd):
    for customer in customers:
        print(customer)
        exercise05.add_item(wd, customer)
wd.find_element_by_css_selector('a[href="#/medicines"]').click()
exercise05.del_item(wd, main_windows)
sleep(1)
wd.find_element_by_xpath('//button[contains(text(),"添加")]').click()
for medicine in medicines:
    exercise05.add_item(wd, medicine)
wd.find_element_by_css_selector('a[href="#/orders"]').click()
order_name = '测试订单'
exercise05.add_order(wd, order_name)
