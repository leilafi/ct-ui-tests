from page_objects import argus_homepage, argus_location_page, argus_destination_page, argus_car_hire_page, argus_language_menu, argus_contact_us_page
import base_test
import unittest

#tests = []
class ArgusTests(base_test.BaseTest):

    def test_argus_verify_homepage_title(self):
        this_homepage = argus_homepage.ArgusHomepage()
        this_homepage.land_page(this_homepage.page_name)
        self.verify_title(this_homepage.get_title(),
                          this_homepage.page_name,
                          this_homepage.title_key)

    def test_argus_homepage_verify_locations(self):
        this_page = argus_homepage.ArgusHomepage() # Loads homepage and then redirects to a location page
        self.verify_all_location_links(this_page)

    def test_argus_destination_exist(self):
        this_location = argus_location_page.Location_Page()
        this_location.land_page(this_location.page_name)
        self.assert_not_exist(this_location.find_destination_link(),this_location.page_name,this_location.destination_key)

    def test_argus_car_hire_verify_locations(self):
        this_page = argus_car_hire_page.CarHirePage()
        self.verify_all_location_links(this_page)

    def test_argus_change_language_popular(self):
        language_menu = argus_language_menu.LanguageMenu()
        language_menu.land_page(language_menu.page_name)
        language_menu.open_menu()
        language_menu.select_language(language_menu.popular_language_item)
        language_menu.verify_translation(language_menu.popular_expected_translation)

    def test_argus_change_language(self):
        language_menu = argus_language_menu.LanguageMenu()
        language_menu.land_page(language_menu.page_name)
        language_menu.open_menu()
        language_menu.select_language(language_menu.language_item)
        language_menu.verify_translation(language_menu.expected_translation)

    def test_argus_destination_load(self):
        this_destination = argus_destination_page.DestinationPage()
        this_destination.land_page_from_parent()
        self.verify_title(this_destination.get_header(),
                          this_destination.page_name,
                          this_destination.title_key, True)

    def test_argus_contact_us_title(self):
        this_contact = argus_contact_us_page.ContactUsPage()
        this_contact.land_page_from_parent()
        self.verify_title(this_contact.get_header(), this_contact.page_name,this_contact.title_key)


if __name__ == '__main__':
    unittest.main()
#alltests = unittest.TestSuite(tests)