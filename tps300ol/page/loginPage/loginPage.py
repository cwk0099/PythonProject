from ..base_page import BasePage
from ..homePage.homePage import HomePage

# 登录模块的Page，继承BasePage，封装所用的到元素、方法和步骤，三者分开
class LoginPage(BasePage):
    def user_name(self):
        return self.css_selector('input[placeholder = "请输入用户名"]')

    def user_password(self):
        return self.css_selector('input[placeholder = "请输入密码"]')

    def err_msg(self):
        return self.css_selector('div.el-message')

    def login_btn(self):
        return self.xpath('//span[contains(text(),"登录")]')

# 用例步骤，用前面说封装的方法和步骤，进行步骤的编写
    def login_fail(self, username, password):
        self.input_text(self.user_name(), username)
        self.input_text(self.user_password(), password)
        self.element_click(self.login_btn())
        self.wait(1)
        alert_text = self.get_text(self.err_msg())
        self.wait(3)
        return alert_text

# 注意，如果方法中进行了页面的跳转，如登陆之后跳转到首页，方法中要return到对应页面的Page
    def login_success(self, username, password):
        self.input_text(self.user_name(), username)
        self.input_text(self.user_password(), password)
        self.element_click(self.login_btn())
        self.wait(1)
        return HomePage(self.driver)
