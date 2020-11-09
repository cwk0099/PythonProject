import os
import sys
import pytest
from selenium import webdriver
import allure
import time
import re

sys.path.append(os.getcwd())

# 前置函数，创建driver并且打开链接
@pytest.fixture(scope='class')
def get_driver():
    global wd
    wd = webdriver.Chrome()
    wd.maximize_window()
    return wd

@pytest.fixture(scope='class')
def open_url():
    wd.get("http://192.168.0.237:3000")
    def close_driver():
        wd.quit()
    yield
    close_driver()

# 获取用例结果，若失败就截图并关联用例
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
     获取每个用例状态的钩子函数
     :param item:
     :param call:
     :return:
     """
    # 获取用例结果
    outcome = yield
    rep = outcome.get_result()
    # 如果结果为失败，则打印失败结果和截图保存
    if rep.when == 'call' and rep.failed:
        ## 定义图片截图时间
        pic_time = time.strftime("%Y-%m-%d-%H_%M", time.localtime(time.time()))
        names = re.findall('\w+[\u4e00-\u9fa5]+', item.name)
        name = names[0]
        print(name + '用例执行失败')
        ## 检查图片父目录是否存在，若不存在则创建
        file_purl = '..\\test_picture\\'
        if not os.path.exists(file_purl):
            os.mkdir(file_purl)
        file_url = file_purl + name + '_' + pic_time + '.png'
        ## 截图保存
        bol = wd.get_screenshot_as_file(file_url)
        ## 读取图片为bytes文件并且附加到对应测试用例的报告上
        with allure.step("添加用例失败截图"):
            with open(file_url, mode='rb') as f:
                file = f.read()
            allure.attach(file, '失败截图',
                          allure.attachment_type.PNG)
