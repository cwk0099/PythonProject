import os
import sys
import allure
import pytest

sys.path.append(os.getcwd())
from page import loginPage

# 使用前后置函数
@pytest.mark.usefixtures('get_driver', 'open_url')
@allure.feature('告警窗')
class Test_tps300_B02_告警窗:
    @allure.story('修改告警状态')
    @allure.title('未复归修改为复归')
    @allure.issue('http://192.168.0.217/', name='禅道')
    @pytest.mark.high
    def test_tps300_B02_UI01_未复归修改为复归(self, get_driver):
        login_page = loginPage.LoginPage(get_driver)
        home_page = login_page.login_success('admin', '123456')
        if home_page.get_url() != 'http://192.168.0.237:3000/':
            assert 1 == 0
        alarm_page = home_page.switch_to_alarmView('li.is-active  div', '//li[contains(text(),"告警窗")]')
        bol = alarm_page.edit_status(0)
        assert bol

    @allure.story('修改告警状态')
    @allure.title('未复归修改为复归')
    @allure.issue('http://192.168.0.217/', name='禅道')
    @pytest.mark.high
    def test_tps300_B02_UI02_未复归修改为复归(self, get_driver):
        login_page = loginPage.LoginPage(get_driver)
        home_page = login_page.login_success('admin', '123456')
        if home_page.get_url() != 'http://192.168.0.237:3000/':
            assert 1 == 0
        alarm_page = home_page.switch_to_alarmView('li.is-active  div', '//li[contains(text(),"告警窗")]')
        bol = alarm_page.edit_status(1)
        assert bol


if __name__ == '__main__':
    # 自动执行用例及生成报告
    # pytest.main(['-s', '-q', '--alluredir', './reports', '--clean-alluredir'])
    pytest.main(['-s', '-q', '-k test_告警窗.py', '--alluredir', './reports', '--clean-alluredir'])
    # 生成报告，每次执行都清空数据
    os.system('allure generate reports -o allure-reports --clean')
