import base_page, argus_homepage
from helpers import logs, get_elements


class CookiePage(base_page.BasePage):
    def __init__(self):
        base_page.BasePage.__init__(self)
        self.page_name = "arguscookies"
        self.parent_page = "argushomepage"
        self.link_name = "Cookie Policy"
