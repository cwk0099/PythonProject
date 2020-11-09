import os
import sys
import allure
import pytest

sys.path.append(os.getcwd())
from page.home import loginPage
from safe_general import eventPage


@pytest.mark.usefixtures('get_driver', 'open_url')
@allure.feature('事件窗')
class Test_TPS300_A03_事件窗:
    @allure.story('查询展示栏检查')
    @allure.title('增加/隐藏查询展示栏')
    def test_tps300_A03_UI01_查询展示栏检查用例(self, get_driver):
        login_page = loginPage.LoginPage(get_driver)
        home_page = login_page.login_success('admin2', '123456')
        event_page = home_page.switch_to_eventView()
        bol = event_page.search_show_check()
        pytest.assume(bol)

    @allure.story('修改事件表格')
    @allure.title('增加/隐藏事件表格列，不保存')
    def test_tps300_A03_UI02_表格列展示(self, get_driver):
        event_page = eventPage.EventPage(get_driver)
        bol = event_page.table_list_check()
        pytest.assume(bol)

    @allure.story('修改事件列表')
    @allure.title('增加/隐藏事件表格列并保存')
    def test_tps300_A03_UI03_编辑表格列保存(self, get_driver):
        event_page = eventPage.EventPage(get_driver)
        bol = event_page.list_save_check()
        pytest.assume(bol)

    @allure.story('修改事件列表')
    @allure.title('增加/隐藏事件表格列并保存')
    def test_tps300_A03_UI04_翻页(self, get_driver):
        event_page = eventPage.EventPage(get_driver)
        bol = event_page.page_turn()
        pytest.assume(bol)


if __name__ == '__main__':
    # pytest.main(['-s'])
    # 执行用例，且每次运行都清空用例结果数据
    # -k：指定运行某一个文件
    # --instafail --tb=line，调试时候用，打印详细错误信息，遇到用例失败会停止，pytest-instafail插件
    # --reruns=2 --reruns-delay=1 ，用例失败重新运行该用例两次，并且每次间隔一秒，pytest-rerunsfailures插件
    # --alluredir ./reports --clean-alluredir ,pytest-allure插件，生成报告在本级目录的report文件夹
    pytest.main(
        ['-s', '-q', '-k test_tps300_A03_事件窗.py', '--instafail', '--tb=line', '--reruns=2', '--reruns-delay=1',
         '--alluredir', './reports', '--clean-alluredir'])
    # 生成报告，每次执行都清空数据
    os.system('allure generate reports -o allure-reports --clean')
