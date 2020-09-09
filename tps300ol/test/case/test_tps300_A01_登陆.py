import os
import sys
import allure
import pytest
# 调用自己写的模块的时候，需要用到这个代码，不然会报错
sys.path.append(os.getcwd())
from page import loginPage

# 使用前后置函数来获取driver和打开网址
@pytest.mark.usefixtures('get_driver', 'open_url')
# 功能
@allure.feature('登陆功能（一级标题）')
class Test_tps300_A01_登陆:
    # 参数化传递，用于数据不同，操作一样的用例
    @pytest.mark.parametrize('username,password,exword',
                             [('', '', '用户名不能为'), ('123', '', '密码不能为空'),
                              ('', '123', '用户名不能为空'), ('123', '123', '密码长度不能少于6位')
                              ])
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
    def test_tps300_A01_UI01_登陆失败(self, get_driver, username, password, exword):
        """
        用例描述
        """
        # 将对应的登录Page实例化
        login_page = loginPage.LoginPage(get_driver)
        # 调用对应Page中的方法
        alert_text = login_page.login_fail(username, password)
        # 断言检查是否正确
        assert alert_text == exword

    @allure.title('登陆成功')
    @allure.story('管理员登录')
    @allure.issue('http://192.168.0.217/', name='点击我跳转禅道')
    def test_tps300_A02_UI02_登陆成功(self, get_driver):
        login_page = loginPage.LoginPage(get_driver)
        # 实例化主页的Page，这里是用登录Page中的方法返回的值来实例化
        home_page = login_page.login_success('admin', '123456')
        assert home_page.get_url() == 'http://192.168.0.237:3000/'


# main函数运行
if __name__ == '__main__':
    # pytest.main(['-s'])
    # 执行用例，且每次运行都清空用例结果数据
    pytest.main(['-s', '-q', '-k test_登陆.py', '--instafail --tb=line', '--return 2 --returns-delay 1',
                 '--alluredir', './reports', '--clean-alluredir'])
    # 生成报告，每次执行都清空数据
    os.system('allure generate reports -o allure-reports --clean')
