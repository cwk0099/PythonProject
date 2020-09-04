from selenium import webdriver


def med_creat(wd):
    wd.find_element_by_css_selector('a[href="#/medicines"]').click()
    wd.find_element_by_css_selector('button.btn-md').click()
    medicine = wd.find_elements_by_css_selector('input.form-control')
    med_name = medicine[0]
    med_num = medicine[1]
    med_decr = wd.find_element_by_css_selector('textarea.form-control')
    # med_name.claer()
    # med_num.claer()
    # med_decr.clear()
    med_name.send_keys('阿莫西林')
    med_num.send_keys('AM-20200824')
    med_decr.send_keys('阿莫西林1号')
    wd.find_element_by_xpath('//button[contains(text(),"创建")]').click()
    return 0
