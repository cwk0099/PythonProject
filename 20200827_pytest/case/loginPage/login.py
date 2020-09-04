from time import sleep

def login(wd, user, password):
    # 等待元素操作
    wd.implicitly_wait(10)
    # 输入用户名和密码
    user_input = wd.find_element_by_css_selector('input[placeholder = "请输入用户名"]')
    password_input = wd.find_element_by_css_selector('input[placeholder = "请输入密码"]')
    user_input.send_keys(user)
    password_input.send_keys(password)
    # 点击登录
    wd.find_element_by_xpath('//span[contains(text(),"登录")]').click()
    sleep(1)
    print(wd.current_url)
    if wd.current_url == 'http://192.168.0.237:3000/':
        return True
    else:
        return False