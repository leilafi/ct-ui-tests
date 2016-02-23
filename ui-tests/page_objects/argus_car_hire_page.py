import base_page


class CarHirePage(base_page.BasePage):
    def __init__(self):
        base_page.BasePage.__init__(self)
        self.page_name = "arguscarhire"
        self.all_locations = "all-countries"

    #def cli