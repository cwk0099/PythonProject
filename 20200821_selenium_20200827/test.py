from selenium import webdriver
import exercise01
import exercise05

wd = webdriver.Chrome()
wd.implicitly_wait(3)
exercise01.login(wd)
wd.find_element_by_css_selector('a[href="#/customers"]').click()
print(exercise05.exist(wd))