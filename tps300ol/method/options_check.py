# 选所有未被选中或已经被选中的列表选项进行操作，返回所操作选项的名称
def option_names(options, options_name, status):
    names = list()
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

# 选一个未被选中或已经被选中的列表选项进行操作，返回那个选项的名称
def op_name(options, options_name, status):
    index = 0
    name = None
    for option in options:
        option_status = option.get_attribute('class')
        if status == 'is-checked':
            if status in option_status:
                name = options_name[index].text
                option.click()
                break
        else:
            if status == option_status:
                name = options_name[index].text
                option.click()
                break
    return name