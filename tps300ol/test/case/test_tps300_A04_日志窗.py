import os
import sys
import allure
import pytest

sys.path.append(os.getcwd())
from page import loginPage
from page import logPage


@pytest.mark.usefixtures('get_driver', 'open_url')
@allure.feature('日志窗')
class Test_TPS300_A04_日志窗:
    @allure.story('查询展示栏检查')
    @allure.title('增加/隐藏查询展示栏')
    def test_tps300_A04_UI01_查询展示栏检查用例(self, get_driver):
        login_page = loginPage.LoginPage(get_driver)
        home_page = login_page.login_success('admin', '123456')
        log_page = home_page.switch_to_logView()
        bol = log_page.search_show_check()
        pytest.assume(bol)

    @allure.story('修改日志表格')
    @allure.title('增加/隐藏日志表格列，不保存')
    def test_tps300_A04_UI02_表格列展示(self, get_driver):
        log_page = logPage.LogPage(get_driver)
        bol = log_page.table_list_check()
        pytest.assume(bol)

    @allure.story('修改日志列表')
    @allure.title('增加/隐藏日志表格列并保存')
    def test_tps300_A04_UI03_编辑日志列保存(self, get_driver):
        log_page = logPage.LogPage(get_driver)
        bol = log_page.list_save_check()
        pytest.assume(bol)


if __name__ == '__main__':
    # pytest.main(['-s'])
    # 执行用例，且每次运行都清空用例结果数据
    pytest.main(
        ['-s', '-q', '-k test_tps300_A03_事件窗.py', '--instafail', '--tb=line', '--reruns=2', '--reruns-delay=1',
         '--alluredir', './reports', '--clean-alluredir'])
    # 生成报告，每次执行都清空数据
    os.system('allure generate reports -o allure-reports --clean')
