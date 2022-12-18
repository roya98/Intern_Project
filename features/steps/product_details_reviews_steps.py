from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep



@given('Open Product Details page')
def open_product_page(context):
     context.app.reviews_page.open_product_page()


@when('Click on reviews stars')
def click_on_reviews_product(context):
     context.app.reviews_page.click_on_reviews_product()


@then('Verify reviews are shown')
def reviews_shown(context):
     context.app.reviews_page.reviews_shown()





