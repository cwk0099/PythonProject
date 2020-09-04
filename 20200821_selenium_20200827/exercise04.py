from selenium import webdriver


def print_menu(wd):
    wd.find_element_by_css_selector('a[href="http://www.python3.vip"]').click()
    login_windows = wd.current_window_handle
    for handle in wd.window_handles:
        wd.switch_to.window(handle)
        if 'http://www.python3.vip/' in wd.current_url:
            break
    menus = wd.find_elements_by_css_selector('a.nav-link span')
    for menu in menus:
        print(f'{menu.text}\n')
    wd.switch_to.window(login_windows)
    wd.find_element_by_css_selector('li.user-menu  a').click()
    wd.find_element_by_xpath('//a[contains(text(),"退出登录")]').click()
    return 0
