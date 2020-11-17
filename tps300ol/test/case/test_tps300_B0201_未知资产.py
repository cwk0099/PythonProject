import os
import sys
import pytest
import allure
sys.path.append(os.getcwd())
from page.home.loginPage import LoginPage
from page.running_monitor.asset_monitor.unknown_assetPage import UnknownAssetPage

@pytest.mark.usefixtures('get_driver', 'open_url')
@allure.feature('运行监测-资产监测-未知资产')
class Test_TPS300_B0201_未知资产:
    @allure.story('修改查询展示')
    @allure.title('增加/隐藏查询展示栏')
    def test_tps300_B0201_UI01_修改查询展示(self, get_driver):
        login_page = LoginPage(get_driver)
        home_page = login_page.login_success('admin1', '123456')
        unknown_asset_page = home_page.switch_to_unknown_assetView()
        bol = unknown_asset_page.search_show_check()
        pytest.assume(bol)

    @allure.story('修改表格列')
    @allure.title('表格列选择展示不保存')
    def test_tps300_B0201_UI02_修改表格展示(self, get_driver):
        unknown_asset_page = UnknownAssetPage(get_driver)
        bol = unknown_asset_page.table_list_check()
        pytest.assume(bol)

    @allure.story('修改表格列')
    @allure.title('修改并保存')
    def test_tps300_B0201_UI03_修改表格列表并保存(self, get_driver):
        unknown_asset_page = UnknownAssetPage(get_driver)
        bol = unknown_asset_page.list_save_check()
        pytest.assume(bol)

    @allure.story('资产操作')
    @allure.title('资产删除')
    def test_tps300_B0201_UI04_资产删除(self, get_driver):
        unknown_asset_page = UnknownAssetPage(get_driver)
        bol = unknown_asset_page.delete_asset()
        pytest.assume(bol)

    @allure.story('资产操作')
    @allure.title('资产不填写必填项注册')
    def test_tps300_B0201_UI05_资产异常注册(self, get_driver):
        unknown_asset_page = UnknownAssetPage(get_driver)
        bol = unknown_asset_page.err_register()
        pytest.assume(bol)

    @allure.story('翻页')
    @allure.title('翻页')
    def test_tps300_B0201_UI06_翻页(self, get_driver):
        unknown_asset_page = UnknownAssetPage(get_driver)
        bol = unknown_asset_page.page_turn()
        pytest.assume(bol)


if __name__ == '__main__':
    # 自动执行用例及生成报告,失败自动重新执行两次，并且延迟1s执行，并且每条用例执行完若出错立马打印出错信息
    # pytest.main(['-s', '-q', '--alluredir', './reports', '--clean-alluredir'])
    pytest.main(['-s', '-q', '-k test_tps300_B0201_未知资产.py', '--instafail --tb=line', '--return 2 --returns-delay 1',
                 '--alluredir', './reports', '--clean-alluredir'])
    # 生成报告，每次执行都清空数据
    os.system('allure generate reports -o allure-reports --clean')
