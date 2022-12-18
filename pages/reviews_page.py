from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Reviews(Page):
    # $x("//span[@class='jdgm-prev-badge__stars']")
    # $x("//h2[@class='jdgm-rev-widg__title']")
    REVIEWS = (By.XPATH, "//span[@class='jdgm-prev-badge__stars']")
    REVIEWS_SHOWN = (By.XPATH, "//h2[@class='jdgm-rev-widg__title']")

    def open_product_page(self):
        self.open_url('products/cureskin-gentle-cleanse-face-foam')


    def click_on_reviews_product(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.REVIEWS)).click()
        sleep(4)


    def reviews_shown(self):
        self.driver.find_element(*self.REVIEWS_SHOWN)







