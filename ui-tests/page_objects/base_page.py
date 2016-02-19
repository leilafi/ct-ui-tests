from selenium import webdriver
from helpers import get_elements, logs
import selenium.webdriver.support.ui as ui


class BasePage(object):

    def __init__(self):
        #self.driver = webdriver.Chrome('/usr/bin/chromedriver')
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5) # wait for the elements to load
        self.url_key = "url"
        self.title_key = "page-title"

    def land_page(self, page_name):
        url = get_elements.return_element_data(page_name, self.url_key)[1]
        self.driver.get(url)

    def get_title(self):
        title = self.driver.title
        print "title%s" %title
        return title

    def find_locations(self, page_name, element_key):
        logs.start("finding_locations %s in %s" %(element_key, page_name))
        element_data = get_elements.return_element_data(page_name, element_key)
        print 'element data'
        print element_data[1][0]
        print type(element_data[1])
        dict_links = {}
        print len(element_data[1])
        for i in range(0, len(element_data[1])):
            #print i
            #print element_data[0]
            #print element_data[1][i]
            element = self.driver.find_element(element_data[0],element_data[1][i]) # Find_element(By, value) By is link_text and value is the location names
            dict_links[element_data[1][i]] = element
        logs.done()
        #return (element, element_data[1]) # return the element and the name(value) of the element
        #print "dict_links"
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


    def switch_windows(self):
        print "switched"

    def __del__(self):
        self.driver.quit()