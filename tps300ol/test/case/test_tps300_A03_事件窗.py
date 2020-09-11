import os
import sys
import allure
import pytest

sys.path.append(os.getcwd())
from page import loginPage
from page import eventPage


@pytest.mark.usefixtures('get_driver', 'open_url')
@allure.feature('事件窗')
class Test_TPS300_A03_事件窗:
    @allure.story('查询展示栏检查')
    @allure.title('增加/隐藏查询展示栏')
    def test_tps300_A03_UI01_查询展示栏检查用例(self, get_driver):
        login_page = loginPage.LoginPage(get_driver)
        home_page = login_page.login_success('admin', '123456')
        event_page = home_page.switch_to_eventView()
        assert event_page.check_showed_options()


if __name__ == '__main__':
    # pytest.main(['-s'])
    # 执行用例，且每次运行都清空用例结果数据
    pytest.main(
        ['-s', '-q', '-k test_tps300_A03_事件窗.py', '--instafail --tb=line', '--return 2 --returns-delay 1',
         '--alluredir', './reports', '--clean-alluredir'])
    # 生成报告，每次执行都清空数据
    os.system('allure generate reports -o allure-reports --clean')
