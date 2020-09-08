
def select_clean(select, options, search):
    select.click()
    status = 'selected'
    for option in options:
        s = option.get_attribute("class")
        if status in s:
            option.click()
    search.click()

