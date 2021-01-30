from base_page import BasePage
from running_manager.asset_page import AssetPage

class AlarmViewPage(BasePage):

    # 获取当前页面URL
    def page_url(self):
        return self.get_url()

    # 运行管理菜单
    def running_manager(self):
        return self.css_selector('span.menu > ul > li', 1)[2]

    # 资产台账
    def asset_menu(self):
        return self.xpath('//li[contains(text(),"资产台帐")]')

    # 状态选择框
    def search_status(self):
        return self.css_selector('form > div:nth-child(1) > div > div > div.el-input.el-input--small.el-input--suffix '
                                 '> span > span > i')

    # 状态选择栏：未复归和复归列表
    def select_status(self):
        return self.css_selector('body > div.el-select-dropdown.el-popper.is-multiple > div.el-scrollbar > '
                                  'div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li', 1)

    # 查询按钮
    def search_btn(self):
        return self.css_selector('div:nth-child(6) > div > div > button')

    # 第一个告警的编辑按钮
    def edit_status_btn(self):
        return self.css_selector('div.el-table__fixed-body-wrapper > table > tbody > tr '
                                  'i.el-icon-edit', 1)[0]

    # 提示窗的确定按钮
    def confirm_btn(self):
        return self.css_selector('body > div.el-message-box__wrapper > div > div.el-message-box__btns > '
                                 'button.el-button.el-button--default.el-button--small.el-button--primary'
                                 '')

    # 操作后的提示窗
    def alert_text(self):
        return self.css_selector('p.el-message__content')

    # 编辑表格列的选项（点击勾选的按钮）
    def table_list_options(self):
        options = self.xpath('//div[@x-placement="bottom"]//div//li/label', 1)
        options.pop()
        return options

    # 编辑表格列选项对应的名称
    def table_list_names(self):
        names = self.xpath('//div[@x-placement="bottom"]//div//li/span', 1)
        names.pop()
        return names

    # 当前显示的表格列，除了操作栏
    def table_list(self):
        list_name = self.xpath(
            '/html/body/section/main/section/main/div/section/main/div/div/table/thead/tr/th/div', 1)
        list_name.pop()
        return list_name

    # 当前显示的表格列的名称，除了操作栏
    def list_names(self, elements):
        names = list()
        for element in elements:
            text = self.get_text(element)
            names.append(text)
        return names

    # 修改成功提示窗文本
    @staticmethod
    def edit_success():
        return '修改成功！'

    # 表格列编辑保存按钮
    def list_save_btn(self):
        return self.xpath('//div[@x-placement]/span/button')

    # 表格编辑确定按钮
    def list_confirm_btn(self):
        return self.xpath('//div[@x-placement]/div[1]/div/button[2]')

    # 查询选择展示按钮
    def search_show_btn(self):
        return self.xpath('/html/body/section/main/section/header/form/div[6]/div/div/span/button')

    # 查询选择展示勾选按钮
    def search_show_options(self):
        return self.xpath('//body/div[contains(@class,"el-popover")]//div/ul/li/label', 1)

    # 查询选择展示名称
    def search_show_name(self):
        return self.xpath('//body/div[contains(@class,"el-popover")]//div/ul/li/span', 1)

    # 已展示的查询框
    def search_showed_list(self):
        return self.xpath('/html/body/section/main/section/header/form/div/label', 1)

    # 已展示的查询框名称
    def search_showed_names(self):
        names = []
        s_lists = self.search_showed_list()
        for s_list in s_lists:
            names.append(self.get_text(s_list))
        return names

    # 查询为空的元素
    def no_search_result(self):
        return self.css_selector('div > section > main > div > div.el-table__body-wrapper.is-scrolling-none '
                                  '> div > span', 1)

    # 查询选择检操作步骤
    def search_show_check(self):
        self.element_click(self.search_show_btn())
        options_1 = self.search_show_options()
        names_1 = self.search_show_name()
        checked_names_1 = self.check_lists(options_1, names_1, 'is-checked')
        c = 0
        if not self.search_showed_list():
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
        self.page_refresh()
        self.wait(1)
        self.element_click(self.search_show_btn())
        options_11 = self.search_show_options()
        names_11 = self.search_show_name()
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
        del (table_lists_2[0])
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
        del (table_lists_21[0])
        table_list_names_21 = self.list_names(table_lists_21)
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

    # 列表编辑保存按钮检查操作步骤
    def list_save_check(self):
        # edit_btn = self.table_list()[0]
        # self.element_click(edit_btn)
        # self.wait(1)
        options_3 = self.table_list_options()
        names_3 = self.table_list_names()
        checked_name_3 = self.check_list(options_3, names_3, 'is-checked')
        save_btn = self.list_save_btn()
        self.element_click(save_btn)
        self.wait(1)
        confirm_btn = self.list_confirm_btn()
        self.element_click(confirm_btn)
        self.page_refresh()
        table_list_3 = self.table_list()
        del (table_list_3[0])
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
        self.page_refresh()
        table_list_31 = self.table_list()
        del (table_list_31[0])
        list_names_31 = self.list_names(table_list_31)
        if checked_name_31 in list_names_31:
            k += 1
        if k == 2:
            return True
        else:
            return False

    # 修改告警状态的操作步骤
    def edit_status(self, s):
        select = self.search_status()
        self.element_click(select)
        self.wait(1)
        options_4 = self.select_status()
        self.element_click(options_4[s])
        search = self.search_btn()
        self.element_click(search)
        self.wait(1)
        bol = not self.no_search_result()
        if bol:
            self.element_click(self.edit_status_btn())
            self.wait(1)
            self.element_click(self.confirm_btn())
            self.wait(1)
            text = self.get_text(self.alert_text())
            self.select_clean(select, options_4, search)
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

    # 切换到资产台账窗口
    def switch_to_assets(self):
        self.mouse_move(self.running_manager())
        self.wait(2)
        self.element_click(self.asset_menu())
        return AssetPage(self.driver)