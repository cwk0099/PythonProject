from ..base_page import BasePage


class AlarmViewPage(BasePage):
    def search_status(self):
        return self.css_selector('form > div:nth-child(1) > div > div > div.el-input.el-input--small.el-input--suffix '
                                 '> span > span > i')

    # return self.css_seletor('form > div:nth-child(7) > div > button > span')

    def select_status(self):
        return self.css_selectors('body > div.el-select-dropdown.el-popper.is-multiple > div.el-scrollbar > '
                                  'div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li')

    def search_btn(self):
        return self.css_selector('div:nth-child(6) > div > div > button')

    def edit_status_btn(self):
        return self.css_selectors('div.el-table__fixed-body-wrapper > table > tbody > tr '
                                  'i.el-icon-edit')[0]

    def confirm_btn(self):
        return self.css_selector('body > div.el-message-box__wrapper > div > div.el-message-box__btns > '
                                 'button.el-button.el-button--default.el-button--small.el-button--primary'
                                 '')

    def alert_text(self):
        return self.css_selector('p.el-message__content')

    def table_list_options(self):
        options = self.xpaths('//div[@x-placement="bottom"]//div//li/label')
        options.pop()
        return options

    def table_list_names(self):
        names = self.xpaths('//div[@x-placement="bottom"]//div//li/span')
        names.pop()
        return names

    def table_list(self):
        list_name = self.xpaths(
            '/html/body/section/main/section/main/div/section/main/div/div/table/thead/tr/th/div')
        list_name.pop()
        return list_name

    def list_names(self, elements):
        names = []
        for element in elements:
            names.append(self.get_text(element))
        return names

    @staticmethod
    def edit_success():
        return '修改成功！'

    def edit_status(self, s):
        select = self.search_status()
        self.element_click(select)
        self.wait(1)
        options = self.select_status()
        self.element_click(options[s])
        search = self.search_btn()
        self.element_click(search)
        self.wait(1)
        bol = self.exist_css_selector('div > section > main > div > div.el-table__body-wrapper.is-scrolling-none > div '
                                      '> span')
        if bol:
            self.element_click(self.edit_status_btn())
            self.wait(1)
            self.element_click(self.confirm_btn())
            self.wait(1)
            text = self.get_text(self.alert_text())
            self.select_clean(select, options, search)
            exword = self.edit_success()
            b = bool(text == exword)
            if b:
                return True
            else:
                print('修改告警状态失败')
                return False
        else:
            print('无测试数据')
            return False

    def table_list_check(self):
        self.element_click(self.table_list()[0])
        self.wait(1)
        options = self.table_list_options()
        names = self.table_list_names()
        list_names = self.check_tableList(options, names, 'is-checked')
        table_lists = self.table_list()
        del (table_lists[0])
        table_list_names = self.list_names(table_lists)
        i = 0
        index = 0
        k = 0
        for list_name in list_names:
            if list_name not in table_list_names:
                i += 1
            index += 1
        if i == index:
            k += 1
        list_names1 = self.check_tableList(options, names, 'el-checkbox')
        table_lists1 = self.table_list()
        del (table_lists1[0])
        table_list1_names = self.list_names(table_lists1)
        i1 = 0
        index = 0
        for list_name1 in list_names1:
            if list_name1 in table_list1_names:
                i1 += 1
            index += 1
        if i1 == index:
            k += 1
        if k == 2:
            return True
        else:
            return False