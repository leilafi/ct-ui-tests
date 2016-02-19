import unittest
from helpers import get_elements, logs

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

    def assert_not_exist(self, element, element_key, page_name):
        self.assertIsNotNone(element, "%s is missing from %s." %(element_key, page_name))

    def tearDown(self):
        print "Finished:", self._testMethodName
        print "\n"
