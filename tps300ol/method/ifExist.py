from selenium.common.exceptions import NoSuchElementException


def exist_cssSelector(wd, selector):
    try:
        wd.find_element_by_css_selector(selector)
    except NoSuchElementException:
        return True
    else:
        return False

def exist_xPath(wd, xpath):
    try:
        wd.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return True
    else:
        return False
