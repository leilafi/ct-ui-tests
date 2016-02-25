from page_objects import argus_homepage, argus_location_page, argus_destination_page, \
    argus_car_hire_page, argus_language_menu, argus_contact_us_page, argus_faq_page,\
    argus_tandc_page, argus_policy_page, argus_sitemap_page
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
        this_destination.land_page_from_parent(this_destination.parent_page, this_destination.link_name)
        self.verify_title(this_destination.get_header(this_destination.page_name),
                          this_destination.page_name,
                          this_destination.title_key, True)

    def test_argus_contact_us_from_homepage(self):
        this_contact = argus_contact_us_page.ContactUsPage()
        this_contact.land_page_from_parent(this_contact.parent_page, this_contact.link_name)
        self.verify_title(this_contact.get_header(this_contact.page_name),
                          this_contact.page_name,
                          this_contact.title_key)

    def test_argus_faq_from_homepage(self):
        this_faqs = argus_faq_page.FAQPage()
        this_faqs.land_page_from_parent(this_faqs.parent_page, this_faqs.link_name)
        self.verify_title(this_faqs.get_header(this_faqs.page_name),
                          this_faqs.page_name,
                          this_faqs.title_key)

    def test_argus_tandc_from_homepage(self):
        this_tandc = argus_tandc_page.TANDCPage()
        this_tandc.land_page_from_parent(this_tandc.parent_page, this_tandc.link_name)
        self.verify_title(this_tandc.get_header(this_tandc.page_name),
                          this_tandc.page_name,
                          this_tandc.title_key)

    def test_argus_policy_from_homepage(self):
        this_policy = argus_policy_page.PolicyPage()
        this_policy.land_page_from_parent(this_policy.parent_page, this_policy.link_name)
        self.verify_title(this_policy.get_header(this_policy.page_name),
                          this_policy.page_name,
                          this_policy.title_key)

    def test_argus_sitemap_from_homepage(self):
        this_sitemap = argus_sitemap_page.SiteMapPage()
        this_sitemap.land_page_from_parent(this_sitemap.parent_page, this_sitemap.link_name)
        self.verify_title(this_sitemap.get_header(this_sitemap.page_name),
                          this_sitemap.page_name,
                          this_sitemap.title_key)

    def test_argus_sitemap_links(self):
        this_sitemap = argus_sitemap_page.SiteMapPage()
        this_sitemap.land_page(this_sitemap.page_name)
        self.assertTrue(this_sitemap.verify_links(),"Links in the SiteMap: %s does not match the expected: %s!" %(this_sitemap.get_map_links(),this_sitemap.get_expected_links()))


if __name__ == '__main__':
    unittest.main()
#alltests = unittest.TestSuite(tests)