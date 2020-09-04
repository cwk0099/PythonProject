from selenium.common.exceptions import NoSuchElementException


def exist_cssSeletor(wd, seletor):
    try:
        wd.find_element_by_css_selector(seletor)
    except NoSuchElementException as e:
        return False
    else:
        return True

def exist_xPath(wd, xpath):
    try:
        wd.find_element_by_xpath(xpath)
    except NoSuchElementException as e:
        return False
    else:
        return True

