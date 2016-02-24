from selenium import webdriver
from helpers import get_elements, logs


class BasePage(object):

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5) # wait for the elements to load
        self.page_name = "basepage"
        self.url_key = "url"
        self.title_key = "page-title"

    def land_page(self, page_name):
        url = get_elements.return_element_data(page_name, self.url_key)[1]
        self.driver.get(url)

    def get_title(self):
        title = self.driver.title
        return title

    def get_locations_text_and_element(self, page_name, element_key):
        # Returns a dictionary of country element and country text
        logs.start("finding_locations %s in %s" %(element_key, page_name))
        element_data = get_elements.return_element_data(page_name, element_key)
        dict_links = {}
        for i in range(0, len(element_data[1])):
            element = self.driver.find_element(element_data[0],element_data[1][i]) # Find_element(By, value) By is link_text and value is the location names
            dict_links[element_data[1][i]] = element
        logs.done()
        print "dict_links"
        print dict_links.items()
        return dict_links

    def find_element(self, page_name, element_key):
        logs.start("finding %s in %s" %(element_key, page_name))
        element_data = get_elements.return_element_data(page_name, element_key)
        element = self.driver.find_element(*element_data)
        logs.done()
        return element

    def find_elements(self, page_name, element_key):
        logs.start("finding %s in %s" %(element_key, page_name))
        element_data = get_elements.return_element_data(page_name, element_key)
        element = self.driver.find_elements(*element_data)
        logs.done()
        return element

    def select_menu_option(self, page_name, menu, menu_item):
        logs.start("selecting %s in %s" %(menu_item, "menu"))
        print menu
        element_data = get_elements.return_element_data(page_name, menu_item)
        menu.select_by_visible_text(element_data[1])
        #return item

    def element_click(self, element_text, element):
        logs.start("clicking on %s" %element_text)
        element.click()

    def __del__(self):
        self.driver.quit()