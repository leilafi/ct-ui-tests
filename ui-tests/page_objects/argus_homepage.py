import base_page
from helpers import get_elements, logs
import selenium

class ArgusHomepage(base_page.BasePage):

    def __init__(self):
        # initialising
        base_page.BasePage.__init__(self)
        self.page_name = "argushomepage"
        self.city_key = "popular-city"
        self.country_key = "popular-country"

    def element_click(self, element):
        logs.start("clicking on %s" %element)
        element.click()
    # def location_click(self):
    #     logs.start("clicking on location")
    #     locations = self.find_element(self.page_name, self.country_key)
    #     print "location to click:::"
    #     print locations
    #     print type(locations)
    #     for location_text, element in locations.items():
    #         print 'locations'
    #         print location_text
    #         print 'elem'
    #         print element
    #         element.click()
    #     #locations[0].click()
    #     logs.done()

    def location_name(self):
        logs.start("finding the name of the location which is clicked")
        name = self.find_element(self.page_name, self.country_key)