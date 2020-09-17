from page.base_page import BasePage
from page.alarm_viewPage import AlarmViewPage
from page.eventPage import EventPage
from page.logPage import LogPage

class HomePage(BasePage):
    # 安全概况
    def safe_general(self):
        return self.css_selector('li.is-active div')

    # 告警窗
    def alarmView(self):
        return self.xpath('//li[contains(text(),"告警窗")]')

    # 事件窗
    def eventView(self):
        return self.xpath('//li[contains(text(),"事件窗")]')

    # 日志窗
    def logView(self):
        return self.xpath('//li[contains(text(),"日志窗")]')

    # 切换到告警窗页面
    def switch_to_alarmView(self):
        self.wait(1)
        self.mouse_move(self.safe_general())
        self.wait(1)
        self.element_click(self.alarmView())
        self.wait(1)
        return AlarmViewPage(self.driver)

    # 切换到事件窗页面
    def switch_to_eventView(self ,):
        self.wait(1)
        self.mouse_move(self.safe_general())
        self.wait(1)
        self.element_click(self.eventView())
        self.wait(1)
        return EventPage(self.driver)

    # 切换到日志窗页面
    def switch_to_logView(self ,):
        self.wait(1)
        self.mouse_move(self.safe_general())
        self.wait(1)
        self.element_click(self.logView())
        self.wait(1)
        return LogPage(self.driver)