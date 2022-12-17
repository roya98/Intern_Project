from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class Cure(Page):

    CURE_RESULT = (By.XPATH, "//span[@id='ProductCountDesktop' and contains(text(), '23')]")
    FIRST_CURE_IMG = (By.XPATH,"//img[contains(@srcset, 'cdn.shopify.com/s/files/1/0293/8775/1508/products/UnderEye1_165x.jpg?v=1663131411')]")
    # $x("//a[contains(text(), 'CureSkin Under Eye Gel')]")

    FIRST_CURE_TEXT = (By.XPATH,"//a[contains(text(), 'CureSkin Under Eye Gel')]")
    # $x("//span[@class='price-item price-item--sale price-item--last' and contains(text(), 'Rs. 450.00')]")
    FIRST_CURE_PRICE = (By.XPATH, "//span[@class='price-item price-item--sale price-item--last' and contains(text(), 'Rs. 450.00')]")

    def verify_cure_results(self):
        self.find_element(*self.CURE_RESULT)


    def verify_infor_img(self):
        self.find_element(*self.FIRST_CURE_IMG)
        self.find_element(*self.FIRST_CURE_TEXT)
        length_links = len(self.driver.find_elements(*self.FIRST_CURE_PRICE))
        assert length_links, f'Expected 3 but got {length_links}'
