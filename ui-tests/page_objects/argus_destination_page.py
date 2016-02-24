import base_page
from helpers import logs


class DestinationPage(base_page.BasePage):
    def __init__(self):
        base_page.BasePage.__init__(self)
        self.page_name = "argusdestination"
        self.page_header = "page-header"
        self.parent_page = "arguslocation"
        self.link_name = "airport"

    def land_page_from_parent(self):
        self.land_page(self.parent_page)
        self.element_click(self.link_name, self.find_element(self.parent_page, self.link_name))

    def get_header(self):
        header = self.find_element(self.page_name, self.page_header)
        return header.text
