from selenium import webdriver
import time

wd = webdriver.Chrome()
wd.get('http://192.168.0.237:3000')
##设置最长等待时间为10s
wd.implicitly_wait(10)
#查找用户名输入框
username_element = wd.find_element_by_xpath('//input[@placeholder="请输入用户名"]')
# print(username_element.text)
# 查找密码输入框
password_element = wd.find_element_by_xpath('//input[@placeholder="请输入密码"]')
# 清除输入内容
username_element.clear()
password_element.clear()
# print(password_element.text)
# 输入用户名和密码
username_element.send_keys('admin')
password_element.send_keys('123456')
# 点击登录
wd.find_element_by_class_name('btn-login').click()
# 等待5秒后退出
time.sleep(5)
wd.quit()
##wd.find_element_by_xpath('/html/body/section/main/div/div/div/button[@class="el-button btn-login el-button--primary"]').click()
