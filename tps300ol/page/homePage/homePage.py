from ..base_page import BasePage

class HomePage(BasePage):

    def switch_to_alarmView(self, xpath, seletor):
        self.move_to_element(xpath)
        self.wait(1)
        self.click(self.switch_to_element(seletor))
        self.wait(2)
