def is_element_exist(element_list, s):
    e = element_list
    if len(e) == 0:
        print('元素未能定位到')
        return False
    elif s == 0 and len(e) > 1:
        print('找到多个相同的元素')
        return False
    elif s == 0 and len(e) == 1:
        return True
    elif s == 1 and len(e) != 0:
        return True
