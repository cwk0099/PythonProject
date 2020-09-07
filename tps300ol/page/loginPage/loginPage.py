from ..base_page import BasePage
from ..homePage.homePage import HomePage

class LoginPage(BasePage):
    def user_name(self):
        return self.css_seletor('input[placeholder = "请输入用户名"]')

    def user_password(self):
        return self.css_seletor('input[placeholder = "请输入密码"]')

    def err_msg(self):
        return self.css_seletor('div.el-message')

    def login_btn(self):
        return self.x_path('//span[contains(text(),"登录")]')

    def login_fail(self, username, password):
        self.input_text(self.user_name(), username)
        self.input_text(self.user_password(), password)
        self.click(self.login_btn())
        self.wait(1)
        return self.get_text(self.err_msg())

    def login_success(self, username, password):
        self.input_text(self.user_name(), username)
        self.input_text(self.user_password(), password)
        self.click(self.login_btn())
        self.wait(1)
        return HomePage(self.driver)
