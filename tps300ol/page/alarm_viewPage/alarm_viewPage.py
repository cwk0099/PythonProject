from ..base_page import BasePage


class AlarmViewPage(BasePage):
    def search_status(self):
        return self.css_seletor('form > div:nth-child(1) > div > div > div.el-input.el-input--small.el-input--suffix '
                                '> span > span > i')

    # return self.css_seletor('form > div:nth-child(7) > div > button > span')

    def select_status(self):
        return self.css_seletors('body > div.el-select-dropdown.el-popper.is-multiple > div.el-scrollbar > '
                                 'div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li')

    def search_btn(self):
        return self.css_seletor('div:nth-child(6) > div > div > button')

    def edit_status_btn(self):
        return self.css_seletors('div.el-table__fixed-body-wrapper > table > tbody > tr '
                                 'i.el-icon-edit')[0]

    def confirm_btn(self):
        return self.css_seletor('body > div.el-message-box__wrapper > div > div.el-message-box__btns > '
                                'button.el-button.el-button--default.el-button--small.el-button--primary'
                                '')

    def alert_text(self):
        return self.css_seletor('p.el-message__content')

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
        bol = self.exist_css_seletor('div > section > main > div > div.el-table__body-wrapper.is-scrolling-none > div '
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
