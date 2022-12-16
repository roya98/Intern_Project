from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class Cure(Page):
    CURE_RESULT = (By.XPATH, "//span[@id='ProductCountDesktop' and contains(text(), '23')]")

    def verify_cure_results(self):
        self.find_element(*self.CURE_RESULT)
