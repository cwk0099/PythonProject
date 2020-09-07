import os
import sys

import allure
import pytest

sys.path.append(os.getcwd())
from tps300ol.case import alarmView, loginPage


# 使用前后置函数
@pytest.mark.usefixtures('get_driver', 'open_url')
@allure.feature('告警窗')
class Test_告警窗:
    @allure.story('修改告警状态')
    @allure.title('未复归修改为复归')
    @allure.issue('http://192.168.0.217/', name='禅道')
    @pytest.mark.high
    def test_未复归修改为复归(self, get_driver):
        loginPage.login(get_driver, 'admin', '123456')
        bol = alarmView.edit_alarm(get_driver, 0)
        if bol:
            assert 1 == 1
        else:
            assert 0 == 1


if __name__ == '__main__':
    # pytest.main(['-s', '-q', '--alluredir', './reports', '--clean-alluredir'])
    pytest.main(['-s', '-q', '-k test_告警窗.py', '--alluredir', './reports', '--clean-alluredir'])
    # 生成报告，每次执行都清空数据
    os.system('allure generate reports -o allure-reports --clean')
