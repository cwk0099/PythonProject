from base_page import BasePage

class LogPage(BasePage):
    # 查询列表展示选择按钮
    def search_select_btn(self):
        return self.css_selector('div > div > span > button')

    # 查询列表选择选项
    def search_select_options(self):
        return self.xpaths('//body/div[contains(@class,"el-popover")]//div/ul/li/label')

    # 查询列表展示选项名称
    def search_select_names(self):
        return self.xpaths('//body/div[contains(@class,"el-popover")]//div/ul/li/span')

    # 已展示的查询选项
    def search_showed_options(self):
        return self.xpaths('/html/body/section/main/section/header/form/div/label')

    # 已展示的查询选项的名称
    def search_showed_names(self):
        names = []
        s_lists = self.search_showed_options()
        for s_list in s_lists:
            names.append(self.get_text(s_list))
        return names

    # 查询是否有已展示的项
    def check_showed_options(self):
        return self.is_exist(self.search_showed_options(), 1)

    # 当前显示的表格列，除了操作栏
    def table_list(self):
        list_name = self.xpaths(
            '/html/body/section/main/section/main/section/main/div/div[2]/table/thead/tr/th/div')
        return list_name

    # 当前显示的表格列的名称，除了操作栏
    def list_names(self, elements):
        names = []
        for element in elements:
            names.append(self.get_text(element))
        return names

    # 编辑表格列的选项（点击勾选的按钮）
    def table_list_options(self):
        options = self.xpaths('//div[@x-placement="bottom"]//div//li/label')
        return options

    # 编辑表格列选项对应的名称
    def table_list_names(self):
        names = self.xpaths('//div[@x-placement="bottom"]//div//li/span')
        return names

    # 表格列编辑保存按钮
    def list_save_btn(self):
        return self.xpath('//div[@x-placement]/span/button')

    # 表格编辑确定按钮
    def list_confirm_btn(self):
        return self.xpath('//div[@x-placement]/div[1]/div/button[2]')

    # 操作后的提示窗
    def alert_text(self):
        return self.css_selector('p.el-message__content')

    # 列表修改成功提示窗文本
    @staticmethod
    def edit_success():
        return '保存成功'

    # 查询选择检操作步骤
    def search_show_check(self):
        self.element_click(self.search_select_btn())
        options_1 = self.search_select_options()
        names_1 = self.search_select_names()
        checked_names_1 = self.check_lists(options_1, names_1, 'is-checked')
        c = 0
        if self.check_showed_options():
            check_names_1 = self.search_showed_names()
        else:
            check_names_1 = list()
        ci = 0
        i = 0
        for index, checked_name_1 in enumerate(checked_names_1):
            if checked_name_1 not in check_names_1:
                ci += 1
            i = index
        if ci == (i + 1):
            c += 1
        # self.page_refresh()
        # self.wait(1)
        # self.element_click(self.search_select_btn())
        options_11 = self.search_select_options()
        names_11 = self.search_select_names()
        checked_names_11 = self.check_lists(options_11, names_11, 'el-checkbox')
        check_names_11 = self.search_showed_names()
        ci = 0
        i = 0
        for index, checked_name_11 in enumerate(checked_names_11):
            if checked_name_11 in check_names_11:
                ci += 1
            i = index
        if ci == (i + 1):
            c += 1
        if c == 2:
            return True
        else:
            return False

    # 检查编辑表格列的操作步骤
    def table_list_check(self):
        self.element_click(self.table_list()[0])
        self.wait(1)
        options_2 = self.table_list_options()
        names_2 = self.table_list_names()
        list_names_2 = self.check_lists(options_2, names_2, 'is-checked')
        table_lists_2 = self.table_list()
        table_list_names_2 = self.list_names(table_lists_2)
        i = 0
        index = 0
        k = 0
        for list_name_2 in list_names_2:
            if list_name_2 not in table_list_names_2:
                i += 1
            index += 1
        if i == index:
            k += 1
        list_names_21 = self.check_lists(options_2, names_2, 'el-checkbox')
        table_lists_21 = self.table_list()
        table_list_names_21 = self.list_names(table_lists_21)
        del (table_list_names_21[0])
        i1 = 0
        index = 0
        for list_name_21 in list_names_21:
            if list_name_21 in table_list_names_21:
                i1 += 1
            index += 1
        if i1 == index:
            k += 1
        if k == 2:
            return True
        else:
            return False

    # 列表编辑保存检查操作步骤
    def list_save_check(self):
        # self.element_click(self.table_list()[0])
        # self.wait(1)
        options_3 = self.table_list_options()
        names_3 = self.table_list_names()
        checked_name_3 = self.check_list(options_3, names_3, 'is-checked')
        save_btn = self.list_save_btn()
        self.element_click(save_btn)
        self.wait(1)
        confirm_btn = self.list_confirm_btn()
        self.element_click(confirm_btn)
        alert_text_1 = self.alert_text()
        self.wait(1)
        if self.get_text(alert_text_1) != self.edit_success():
            print('修改失败')
            return False
        self.page_refresh()
        table_list_3 = self.table_list()
        list_names_3 = self.list_names(table_list_3)
        k = 0
        if checked_name_3 not in list_names_3:
            k += 1
        self.element_click(self.table_list()[0])
        options_31 = self.table_list_options()
        names_31 = self.table_list_names()
        checked_name_31 = self.check_list(options_31, names_31, 'el-checkbox')
        save_btn = self.list_save_btn()
        self.element_click(save_btn)
        confirm_btn = self.list_confirm_btn()
        self.element_click(confirm_btn)
        alert_text = self.alert_text()
        self.wait(1)
        if self.get_text(alert_text) != self.edit_success():
            print('修改失败')
            return False
        self.page_refresh()
        table_list_31 = self.table_list()
        list_names_31 = self.list_names(table_list_31)
        if checked_name_31 in list_names_31:
            k += 1
        if k == 2:
            return True
        else:
            return False
