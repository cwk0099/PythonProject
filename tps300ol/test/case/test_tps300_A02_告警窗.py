import os
import sys
import allure
import pytest
sys.path.append(os.getcwd())
from page.home import loginPage
from page.safe_general import alarm_viewPage


# 使用前后置函数
@pytest.mark.usefixtures('get_driver', 'open_url')
@allure.feature('告警窗')
class Test_TPS300_A02_告警窗:
    @allure.story('修改查询展示栏')
    @allure.title('增加/隐藏告警展示列')
    def test_tps300_A02_UI01_检查查询栏展示用例(self, get_driver):
        login_page = loginPage.LoginPage(get_driver)
        home_page = login_page.login_success('admin1', '123456')
        alarm_page = home_page.switch_to_alarmView()
        bol = alarm_page.search_show_check()
        pytest.assume(bol)

    @allure.story('修改告警表格')
    @allure.title('增加/隐藏告警表格列')
    @allure.issue('http://192.168.0.217/', name='禅道')
    @pytest.mark.normal
    def test_tps300_A02_UI02_修改告警表格用例(self, get_driver):
        # login_page = loginPage.LoginPage(get_driver)
        # home_page = login_page.login_success('admin', '123456')
        # alarm_page = home_page.switch_to_alarmView('li.is-active  div', '//li[contains(text(),"告警窗")]')
        alarm_page = alarm_viewPage.AlarmViewPage(get_driver)
        if alarm_page.get_url() != 'http://192.168.0.237:3000/main/alarm':
            print(f'页面跳转错误，目前页面为{alarm_page.get_url()}')
            pytest.assume(1 == 0)
        bol = alarm_page.table_list_check()
        pytest.assume(bol)

    @allure.story('修改告警表格')
    @allure.title('修改告警表格列表保存')
    @allure.issue('http://192.168.0.217/', name='禅道')
    @pytest.mark.normal
    def test_tps300_A02_UI03_修改告警列表保存用例(self, get_driver):
        # login_page = loginPage.LoginPage(get_driver)
        # home_page = login_page.login_success('admin', '123456')
        # alarm_page = home_page.switch_to_alarmView('li.is-active  div', '//li[contains(text(),"告警窗")]')
        alarm_page = alarm_viewPage.AlarmViewPage(get_driver)
        if alarm_page.get_url() != 'http://192.168.0.237:3000/main/alarm':
            print(f'页面跳转错误，目前页面为{alarm_page.get_url()}')
            pytest.assume(1 == 0)
        alarm_page.wait(1)
        bol = alarm_page.list_save_check()
        pytest.assume(bol)

    @allure.story('修改告警状态')
    @allure.title('未复归修改为复归')
    @allure.issue('http://192.168.0.217/', name='禅道')
    @pytest.mark.high
    def test_tps300_A02_UI04_未复归修改为复归用例(self, get_driver):
        # login_page = loginPage.LoginPage(get_driver)
        # home_page = login_page.login_success('admin', '123456')
        alarm_page = alarm_viewPage.AlarmViewPage(get_driver)
        bol = alarm_page.edit_status(0)
        pytest.assume(bol)

    @allure.story('修改告警状态')
    @allure.title('未复归修改为复归')
    @allure.issue('http://192.168.0.217/', name='禅道')
    @pytest.mark.high
    def test_tps300_A02_UI05_复归修改为未复归用例(self, get_driver):
        # login_page = loginPage.LoginPage(get_driver)
        # home_page = login_page.login_success('admin1', '123456')
        alarm_page = alarm_viewPage.AlarmViewPage(get_driver)
        bol = alarm_page.edit_status(1)
        pytest.assume(bol)

    @allure.story('修改告警状态')
    @allure.title('未复归修改为复归')
    @allure.issue('http://192.168.0.217/', name='禅道')
    @pytest.mark.normal
    def test_tps300_A02_UI06_翻页(self, get_driver):
        alarm_page = alarm_viewPage.AlarmViewPage(get_driver)
        bol = alarm_page.page_turn()
        pytest.assume(bol)


if __name__ == '__main__':
    # 自动执行用例及生成报告,失败自动重新执行两次，并且延迟1s执行，并且每条用例执行完若出错立马打印出错信息
    # pytest.main(['-s', '-q', '--alluredir', './reports', '--clean-alluredir'])
    pytest.main(['-s', '-q', '-k test_tps300_A02_告警窗.py', '--instafail --tb=line', '--return 2 --returns-delay 1',
                 '--alluredir', './reports', '--clean-alluredir'])
    # 生成报告，每次执行都清空数据
    os.system('allure generate reports -o allure-reports --clean')
