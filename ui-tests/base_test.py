import unittest
from helpers import get_elements, logs
#from page_objects import base_page.BasePage as this_page
from string import lower


class BaseTest(unittest.TestCase):

    def setUp(self):
        print "\nStarted:", self._testMethodName

    def verify_title(self, current_title, page_name, title_key, partly_equal=False):
        # Only interested in [1] because the format of returned data is in [key, value]=[key, title]
        expected = get_elements.return_element_data(page_name, title_key)[1]
        if partly_equal:
            self.assertIn(expected, current_title, "%s was not in expected: %s" % (current_title, expected))
        else:
            self.assertEqual(current_title, expected, "%s did not match expected: %s" % (current_title,expected))

    def remove_keys(self, all_elements, clicked_links):
        logs.start("remove_key")
        r = dict(all_elements)
        for key in clicked_links:
            del r[key]
        return r

    def assert_not_exist(self, element, page_name, element_name):
        self.assertIsNotNone(element, "%s is missing from %s." %(element_name, page_name))

    def verify_all_location_links(self, this_page):
        clicked_history = []
        this_page.land_page(this_page.page_name)
        element = this_page.all_locations
        all_location_links = this_page.get_link_text_and_element(this_page.page_name,this_page.all_locations) # this is only to get the number of links
        number_links = len(all_location_links)
        for i in range(0, number_links): # For number of links do these steps
            this_page.land_page(this_page.page_name) # Go to homepage to get a fresh dict of links_text and elements
            location_dict = this_page.get_locations_text_and_element(this_page.page_name,this_page.all_locations)
            if len(clicked_history) > 0: # Already clicked links has to be removed
                location_dict_cut = self.remove_keys(location_dict,clicked_history)
            else:location_dict_cut = location_dict
            link_text = location_dict_cut.keys()[0] # Get the first link_text element pair in the dict
            this_page.element_click(link_text, location_dict_cut.values()[0])
            clicked_history.append(location_dict_cut.keys()[0]) # Append the clicked link_text to clicked_history list
            print "check if %s is in %s" %(link_text, this_page.get_title())
            self.assertIn(lower(link_text), lower(this_page.get_title()), "%s was not in expected: %s" % (link_text, this_page.get_title()))


    def tearDown(self):
        print "Finished:", self._testMethodName
        print "\n"
