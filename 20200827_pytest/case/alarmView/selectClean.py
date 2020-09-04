
def select_clean(select, options):
    select.click()
    status = 'selected'
    for option in options:
        if option.get_attribute("class") == status:
            option.click()
    return 0
