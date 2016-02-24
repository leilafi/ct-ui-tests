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
