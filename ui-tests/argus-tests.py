from helpers import verify_things, get_elements
from page_objects import argus_homepage, argus_location_page, argus_destination_page, argus_car_hire_page, argus_language_menu
import base_test
import unittest
from string import lower


#tests = []
class ArgusTests(base_test.BaseTest):

    def test_argus_homepage_title(self):
        this_homepage = argus_homepage.ArgusHomepage()
        this_homepage.land_page(this_homepage.page_name)
        self.verify_title(this_homepage.get_title(),
                          this_homepage.page_name,
                          this_homepage.title_key)

    def test_argus_homepage_all_location(self):
        this_page = argus_homepage.ArgusHomepage() # Loads homepage and then redirects to a location page
        self.verify_all_location_links(this_page)

    def test_argus_destination_exist(self):
        this_location = argus_location_page.Location_Page()
        this_location.land_page(this_location.page_name)
        destination = this_location.find_element(this_location.page_name, this_location.destination_key)
        self.assert_not_exist(destination,this_location.destination_key, this_location.page_name)

    def test_argus_car_hire_all_location(self):
        this_page = argus_car_hire_page.CarHirePage()
        self.verify_all_location_links(this_page)

    def test_argus_language(self):
        language_menu = argus_language_menu.LanguageMenu()
        language_menu.land_page(language_menu.page_name)
        language_menu.open_menu()
        language_menu.select_language()
        language_menu.verify_language_update()

    # def test_argus_destination_load(self):
    #     this_destination = argus_destination_page.DestinationPage()
    #     this_location = argus_location_page.Location_Page()
    #     this_location.land_page(this_location.page_name)
    #     this_location.destination_click()
    #     self.verify_title(this_location.get_title(),
    #                       this_destination.page_name,
    #                       this_location.title_key, True)

if __name__ == '__main__':
    unittest.main()
#alltests = unittest.TestSuite(tests)