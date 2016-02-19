import base_page
from helpers import get_elements, logs

class Location_Page(base_page.BasePage):
    def __init__(self):
        base_page.BasePage.__init__(self)
        self.page_name = "arguslocation"
        self.destination_key = "popular-destination"
        self.airport_key = "airport"

    def destination_click(self):
        logs.start("start clicking on a popular destination")
        airport = (self.find_elements(self.page_name, self.airport_key))
        airport[0].click()
        logs.done()

    def quit_driver(self):
        self.driver.quit()

