import os
import sys

import allure
import pytest

sys.path.append(os.getcwd())
from case import loginPage


# 使用前后置函数
@pytest.mark.usefixtures('get_driver', 'open_url')
# 功能
@allure.feature('登陆功能（一级标题）')
class Test_登陆:
    # 参数化传递，用于数据不同，操作一样的用例
    @pytest.mark.parametrize('username,password,exword', [('', '', '用户名不能为'), ('123', '', '密码不能为空'),
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
    @allure.severity('minor')
    def test_tps300_UI0001_登陆失败(self, get_driver, username, password, exword):
        """
        用例描述
        """

        # 调用Case中的logincheck
        alert_text = loginPage.loginfail(username, password, get_driver)
        # 断言检查是否正确
        assert alert_text == exword

    @allure.title('登陆成功')
    @allure.story('管理员登录')
    @allure.issue('http://192.168.0.217/', name='点击我跳转禅道')
    def test_tps300_UI0002_登陆成功(self, get_driver):
        bol = loginPage.login(get_driver, 'admin', '123456')
        if bol:
            assert 1 == 1
        else:
            assert 1 == 0


# main函数运行
if __name__ == '__main__':
    # pytest.main(['-s'])
    # 执行用例，且每次运行都清空用例结果数据
    pytest.main(['-s', '-q', '--alluredir', './reports', '--clean-alluredir'])
    # 生成报告，每次执行都清空数据
    os.system('allure generate reports -o allure-reports --clean')
