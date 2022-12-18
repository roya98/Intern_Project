from pages.cure_page import Cure
from pages.reviews_page import Reviews



class Application:

    def __init__(self, driver):
        self.driver = driver
        self.cure_page = Cure(self.driver)
        self.reviews_page = Reviews(self.driver)