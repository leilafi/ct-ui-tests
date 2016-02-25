import base_page
from helpers import logs


class DestinationPage(base_page.BasePage):
    def __init__(self):
        base_page.BasePage.__init__(self)
        self.page_name = "argusdestination"
        self.page_header = "page-header"
        self.parent_page = "arguslocation"
        self.link_name = "airport"
