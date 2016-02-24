import base_page
from selenium.webdriver.support.ui import Select

class LanguageMenu(base_page.BasePage):
    def __init__(self):
        base_page.BasePage.__init__(self)
        self.page_name = "arguslanguages"
        self.cssmenu = "cssmenu"
        self.xpathlang = "xpathlang"
        self.it = "language-code"

    def open_menu(self):
        cssmenu = self.find_element(self.page_name, self.cssmenu)
        cssmenu.click()

    def select_language(self):
        xpathlang = self.find_element(self.page_name, self.xpathlang)
        xpathlang.click()

    def verify_language_update(self):
        it = self.find_element(self.page_name, self.it)