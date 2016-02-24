import base_page
from selenium.webdriver.support.ui import Select

class LanguageMenu(base_page.BasePage):
    def __init__(self):
        base_page.BasePage.__init__(self)
        self.page_name = "arguslanguages"
        self.menu = "language-menu"
        self.popular_language_item = "popular-language"
        self.popular_expected_translation = "popular-translation"
        self.language_item = "language"
        self.expected_translation = "translation"

    def open_menu(self):
        menu = self.find_element(self.page_name, self.menu)
        menu.click()

    def select_language(self, language):
        language_item = self.find_element(self.page_name, language)
        language_item.click()

    def verify_translation(self, expected_translation):
        updated = self.find_element(self.page_name, expected_translation)