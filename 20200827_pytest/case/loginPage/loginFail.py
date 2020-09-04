from time import sleep

def loginfail(user_value, password_value, wd):
    # 等待元素操作
    wd.implicitly_wait(10)
    # 输入用户名和密码
    user = wd.find_element_by_css_selector('input[placeholder = "请输入用户名"]')
    password = wd.find_element_by_css_selector('input[placeholder = "请输入密码"]')
    user.send_keys(user_value)
    password.send_keys(password_value)
    # 点击登录
    wd.find_element_by_xpath('//span[contains(text(),"登录")]').click()
    sleep(2)
    # 获取提示窗的文字
    alert_text = wd.find_element_by_css_selector('div.el-message').text
    print(alert_text)
    return alert_text
