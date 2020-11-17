from page.base_page import BasePage

class Switch_page(BasePage):
    def switch_page(self, f_menu, s_menu, t_menu=None, fo_menu=None):
        self.wait(1)
        self.mouse_move(f_menu)
        self.wait(1)
        self.mouse_move(s_menu)
        if t_menu is None:
            self.wait(1)
            self.element_click(s_menu)
            return
        else:
            self.wait(1)
            self.mouse_move(t_menu)
        if fo_menu is None:
            self.wait(1)
            self.element_click(t_menu)
            return
        else:
            self.wait(1)
            self.element_click(fo_menu)
            self.element_click(fo_menu)
            return
