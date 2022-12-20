from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Main(Page):
    SEARCH = (By.XPATH, "//*[@class='modal__toggle-open icon icon-search']")
    SEARCH2 = (By.XPATH, "//*[@class='icon icon-search']")
    HEALTHY = (By.ID, 'healthytext')

    def click_search(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.SEARCH)).click()
        sleep(5)


    def verify_open_search(self):
        self.driver.find_element(*self.SEARCH2)

    def verify_main(self):
        self.driver.find_element(*self.HEALTHY)

