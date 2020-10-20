from page.base_page import BasePage
from safe_general.alarm_viewPage import AlarmViewPage
from safe_general.eventPage import EventPage
from safe_general.logPage import LogPage
from running_monitor.asset_monitor.unknown_assetPage import UnknownAssetPage

class HomePage(BasePage):
    # 安全概况
    def safe_general(self):
        return self.css_selector('li.is-active div')

    # 运行监测
    def running_monitor(self):
        return self.css_selector('span.menu > ul > li', 1)[1]

    # 资产监测
    def asset_monitor(self):
        return self.css_selector('body > div:nth-child(5) > ul > div > li:nth-child(2) > div.el-submenu__title')

    # 未知资产
    def unknown_asset(self):
        return self.css_selector('div > li:nth-child(2) > div.el-menu--horizontal > ul > div > li:nth-child(1)')

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
    def switch_to_eventView(self):
        self.wait(1)
        self.mouse_move(self.safe_general())
        self.wait(1)
        self.element_click(self.eventView())
        self.wait(1)
        return EventPage(self.driver)

    # 切换到日志窗页面
    def switch_to_logView(self):
        self.wait(1)
        self.mouse_move(self.safe_general())
        self.wait(1)
        self.element_click(self.logView())
        self.wait(1)
        return LogPage(self.driver)

    # 切换到未知资产
    def switch_to_unknown_assetView(self):
        self.wait(1)
        self.mouse_move(self.running_monitor())
        self.wait(1)
        self.mouse_move(self.asset_monitor())
        self.wait(1)
        self.element_click(self.unknown_asset())
        return UnknownAssetPage(self.driver)