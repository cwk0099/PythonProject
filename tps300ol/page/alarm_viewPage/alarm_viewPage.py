from ..base_page import BasePage


class AlarmViewPage(BasePage):
    def search_status(self):
        return self.css_seletor('div:nth-child(1) > div > div > div.el-input--suffix > span > span > i')

    def select_status(self):
        return self.css_seletors('body > div.el-select-dropdown> div.el-scrollbar > '
                                 'div.el-select-dropdown__wrap > ul > li')

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
        return '修改成功!'

    def edit_status(self):
        select = self.search_status()
        options = self.select_status()
        self.click(select)
        self.click(options[0])
        self.click(self.search_btn())
        if self.exist_css_seletor('div:nth-child(6) > div > div > button'):
            self.click(self.edit_status_btn())
            self.wait(1)
            self.click(self.confirm_btn())
            self.wait(1)
            text = self.get_text(self.alert_text())
            self.select_clean(select, options)
            if text == self.edit_success():
                return True
            else:
                return False
        else:
            return False