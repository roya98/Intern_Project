
from pages.cure_page import Cure



class Application:

    def __init__(self, driver):
        self.driver = driver
        self.cure_page = Cure(self.driver)