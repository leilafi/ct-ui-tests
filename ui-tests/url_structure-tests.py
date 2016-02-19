from helpers import verify_things, get_elements
from page_objects import argus_homepage, argus_location_page, argus_destination_page
import base_test
import unittest
from string import lower


#tests = []
class URLTests(base_test.BaseTest):

    # def test_argus_homepage_title(self):
    #     this_homepage = argus_homepage.ArgusHomepage()
    #     this_homepage.land_page(this_homepage.page_name)
    #     self.verify_title(this_homepage.get_title(),
    #                       this_homepage.page_name,
    #                       this_homepage.title_key)

    def test_argus_homepage_locations_exist(self):
        this_homepage = argus_homepage.ArgusHomepage()
        this_homepage.land_page(this_homepage.page_name)
        city = this_homepage.find_element(this_homepage.page_name, this_homepage.city_key)
        self.assert_not_exist(city,this_homepage.city_key, this_homepage.page_name)
        country = this_homepage.find_element(this_homepage.page_name, this_homepage.country_key)
        self.assert_not_exist(country,this_homepage.country_key, this_homepage.page_name)

    def test_argus_location_load(self):
        clicked_history = []
        this_page = argus_homepage.ArgusHomepage() # Loads homepage and then redirects to a location page
        this_page.land_page(this_page.page_name)
        all_location_links = this_page.find_locations(this_page.page_name,this_page.all_locations) # this is only to get the number of links
        number_links = len(all_location_links)
        for i in range(0, number_links): # For number of links do these steps
            this_page.land_page(this_page.page_name) # Go to homepage to get a fresh dict of links_text and elements
            location_dict = this_page.find_locations(this_page.page_name,this_page.all_locations)
            if len(clicked_history) > 0: # Already clicked links has to be removed
                location_dict_cut = self.remove_keys(location_dict,clicked_history)
            else:location_dict_cut = location_dict
            link_text = location_dict_cut.keys()[0] # Get the first link_text element pair in the dict
            this_page.element_click(link_text, location_dict_cut.values()[0])
            clicked_history.append(location_dict_cut.keys()[0]) # Append the clicked link_text to clicked_history list
            print "check if %s is in %s" %(link_text, this_page.get_title())
            self.assertIn(lower(link_text), lower(this_page.get_title()), "%s was not in expected: %s" % (link_text, this_page.get_title()))

    def test_argus_destination_exist(self):
        this_location = argus_location_page.Location_Page()
        this_location.land_page(this_location.page_name)
        destination = this_location.find_element(this_location.page_name, this_location.destination_key)
        self.assert_not_exist(destination,this_location.destination_key, this_location.page_name)

    def test_argus_destination_load(self):
        this_destination = argus_destination_page.DestinationPage()
        this_location = argus_location_page.Location_Page()
        this_location.land_page(this_location.page_name)
        this_location.destination_click()
        self.verify_title(this_location.get_title(),
                          this_destination.page_name,
                          this_location.title_key, True)

if __name__ == '__main__':
    unittest.main()
#alltests = unittest.TestSuite(tests)