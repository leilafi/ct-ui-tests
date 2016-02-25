import base_page, argus_homepage
from helpers import logs, get_elements

class ContactUsPage(base_page.BasePage):
    def __init__(self):
        base_page.BasePage.__init__(self)
        self.page_name = "arguscontactus"
        self.header = "page-header"
        self.parent_page = "argushomepage"
        self.basic_links = "basic_links"
        self.link_name = "contact-us"
