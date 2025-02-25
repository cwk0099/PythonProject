import os
import sys
import allure
import pytest
# 调用自己写的模块的时候，需要用到这个代码，不然会报错
sys.path.append('../../page')
sys.path.append('../../../readcsv')
from page.home import loginPage
from readcsv.read_csv import ReadCsv


# 使用前后置函数来获取driver和打开网址
@pytest.mark.usefixtures('get_driver', 'open_url')
@allure.feature('一级标题：登陆')
class Test_TPS300_A01_登陆:
    # 参数化传递，用于数据不同，操作一样的用例
    re = ReadCsv('../../../readcsv/csvtest.csv')
    titles = re.readtitle()
    param = re.readline()
    @pytest.mark.parametrize(titles, param)
    @allure.story("二级标题（场景）")
    @allure.title("三级标题（用例标题）")
    # 可用来跳转禅道
    @allure.issue('http://192.168.0.217/', name='点击我跳转禅道')
    @allure.testcase("链接")
    # 优先级可用mark或者severity：blocker（阻塞），critical（重要），normal（一般），minor（轻微），trivial（非常轻微）
    # pytest -m 标签名：运行mark
    # pytest --allure-severity=程度：运行severity
    @pytest.mark.high
    @allure.severity('critical')
    @allure.description('用例描述')
    def test_tps300_A01_UI01_登陆失败用例(self, get_driver, username, password, exword):
        # 将对应的登录Page实例化
        login_page = loginPage.LoginPage(get_driver)
        # 调用对应Page中的方法
        alert_text = login_page.login_fail(username, password)
        # 断言检查是否正确
        pytest.assume(alert_text == exword)

    @allure.title('登陆成功')
    @allure.story('管理员登录')
    @allure.issue('http://192.168.0.217/', name='点击我跳转禅道')
    def test_tps300_A02_UI02_登陆成功用例(self, get_driver):
        login_page = loginPage.LoginPage(get_driver)
        # 实例化主页的Page，这里是用登录Page中的方法返回的值来实例化
        home_page = login_page.login_success('admin', '123456')
        pytest.assume(home_page.get_url() == 'http://192.168.0.237:3000/')


# main函数运行
if __name__ == '__main__':
    # pytest.main(['-s'])
    # 执行用例，且每次运行都清空用例结果数据
    # -k：指定运行某一个文件
    # --instafail --tb=line，调试时候用，打印详细错误信息，遇到用例失败会停止，pytest-instafail插件
    # --reruns=2 --reruns-delay=1 ，用例失败重新运行该用例两次，并且每次间隔一秒，pytest-rerunsfailures插件
    # --alluredir ./reports --clean-alluredir ,pytest-allure插件，生成报告在上一层目录的report文件夹
    pytest.main(['-s', '-q', '-k test_tps300_A01_登陆.py', '--instafail --tb=line', '--reruns=2 --reruns-delay=1',
                 '--alluredir', './reports', '--clean-alluredir'])
    # 生成报告，每次执行都清空数据
    os.system('allure generate reports -o allure-reports --clean')
