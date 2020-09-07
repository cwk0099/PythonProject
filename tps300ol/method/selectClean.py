
def select_clean(select, options):
    select.click()
    status = 'selected'
    for option in options:
        s = option.get_attribute("class")
        if status in s:
            option.click()
    return 0
