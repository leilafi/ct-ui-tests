import base_page
from helpers import get_elements, logs
import selenium

class ArgusHomepage(base_page.BasePage):

    def __init__(self):
        # initialising - test
        base_page.BasePage.__init__(self)
        self.page_name = "argushomepage"
        self.city_key = "popular-city"
        self.country_key = "popular-country"
        self.all_locations = "all-countries"

    # def element_click(self, link_text, element):
    #     logs.start("clicking on an %s" %link_text)
    #     element.click()

    def location_name(self):
        logs.start("finding the name of the location which is clicked")
        name = self.find_element(self.page_name, self.country_key)