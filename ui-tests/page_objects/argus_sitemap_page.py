import base_page, argus_homepage
from helpers import logs, get_elements


class SiteMapPage(base_page.BasePage):
    def __init__(self):
        base_page.BasePage.__init__(self)
        self.page_name = "argussitemap"
        self.parent_page = "argushomepage"
        self.link_name = "sitemap"
        self.links = "links"
        self.expected_links = "expectedlinks"

    def get_map_links(self):
        links = self.find_elements(self.page_name, self.links)
        links_text = []
        for l in links:
            links_text.append(l.text)
        return links_text

    def get_expected_links(self):
        expected = get_elements.return_element_data(self.page_name, self.expected_links)
        return expected[1]

    def verify_links(self):
        if self.get_map_links()!= self.get_expected_links():
            return False
        else:
            return True


