import base_page, argus_homepage


class ContactUsPage(base_page.BasePage):
    def __init__(self):
        base_page.BasePage.__init__(self)
        self.page_name = "arguscontactus"
        self.header = "page-header"
        self.parent_page = "argushomepage"
        self.link_name = "contact-us"

    def land_page_from_parent(self):
        self.land_page(self.parent_page)
        self.element_click(self.link_name, self.find_element(self.parent_page, self.link_name))

    def get_header(self):
        title =  self.find_element(self.page_name, self.header)
        return title.text