from ..base_page import BasePage
from page.alarm_viewPage.alarm_viewPage import AlarmViewPage

class HomePage(BasePage):

    def switch_to_alarmView(self, seletor, xpath):
        self.mouse_move(self.css_selector(seletor))
        self.wait(1)
        self.element_click(self.xpath(xpath))
        self.wait(1)
        return AlarmViewPage(self.driver)