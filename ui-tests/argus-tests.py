from page_objects import argus_homepage, argus_location_page, argus_destination_page, argus_car_hire_page, argus_language_menu, argus_contact_us_page
import base_test
import unittest


class ArgusTests(base_test.BaseTest):

    def test_argus_locations_from_homepage(self):
        this_page = argus_homepage.ArgusHomepage() # Loads homepage and then redirects to a location page
        self.verify_all_location_links(this_page)

    def test_argus_locationas_from_car_hire(self):
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

    def test_argus_destination_from_location(self):
        this_destination = argus_destination_page.DestinationPage()
        this_destination.land_page_from_parent()
        self.verify_title(this_destination.get_header(),
                          this_destination.page_name,
                          this_destination.title_key, True)

    def test_argus_contact_us_from_homepage(self):
        this_contact = argus_contact_us_page.ContactUsPage()
        this_contact.land_page_from_parent()
        self.verify_title(this_contact.get_header(),
                          this_contact.page_name,
                          this_contact.title_key)


if __name__ == '__main__':
    unittest.main()
#alltests = unittest.TestSuite(tests)