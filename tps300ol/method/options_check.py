def table_options(options, options_name, status):
    names = []
    index = 0
    for option in options:
        op_status = option.get_attribute('class')
        if status == 'is-checked':
            if status in op_status:
                names.append(options_name[index].text)
                option.click()
        else:
            if status == op_status:
                names.append(options_name[index].text)
                option.click()
        index += 1
    return names
