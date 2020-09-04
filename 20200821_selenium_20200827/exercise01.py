from selenium import webdriver
import time


def login(wd):
    wd.get('http://127.0.0.1/mgr/sign.html')

    username = wd.find_element_by_id('username')
    password = wd.find_element_by_id('password')

    username.send_keys('byhy')
    password.send_keys('88888888')

    wd.find_element_by_class_name('btn').click()
    return


